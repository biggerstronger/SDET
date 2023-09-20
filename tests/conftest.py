"""
Conftest for UI tests
"""

import os
import random
import string

import allure
import pytest
from selenium import webdriver

from page_objects.estimates_page_object import EstimatesPageObject
from page_objects.login_page_object import LoginPageObject
from page_objects.new_estimate_page import NewEstimatePageObject


@pytest.fixture()
def generate_data_for_tests() -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(30))


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: chrome, firefox or MicrosoftEdge")
    parser.addoption("--remote", dest="remote", action="store", default=False,
                     help="Use option to run local tests")


@pytest.fixture
def remote(request):
    return request.config.getoption("--remote")


@pytest.fixture()
def driver(request, remote):
    ip_address = os.getenv("APP_URL")
    browser_name = request.config.getoption("browser_name")
    if not remote:
        match browser_name:
            case "chrome":
                _driver = webdriver.Chrome()
            case "firefox":
                _driver = webdriver.Firefox()
            case _:
                _driver = webdriver.Edge()
    else:
        match browser_name:
            case "chrome":
                driver_options = webdriver.ChromeOptions()
            case "firefox":
                driver_options = webdriver.FirefoxOptions()
            case _:
                driver_options = webdriver.EdgeOptions()
        _driver = webdriver.Remote(
            command_executor=remote,
            options=driver_options)
    _driver.get(f"{ip_address}login")

    yield _driver

    _driver.quit()


@pytest.fixture()
def authorize(driver) -> None:
    login_page_object = LoginPageObject(driver)
    login_page_object.do_login(os.getenv("VALID_LOGIN"), os.getenv("VALID_PASSWORD"))


@pytest.fixture()
def created_estimate(driver, authorize, generate_data_for_tests):
    estimates_page = EstimatesPageObject(driver)
    estimates_page.open_new_estimate_page()
    new_estimate_page = NewEstimatePageObject(driver)
    valid_data = generate_data_for_tests
    new_estimate_page.fill_fields(valid_data)
    new_estimate_page.submit_form()
    new_estimate_page.interact_with_phase_window()
    new_estimate_page.return_to_estimates_page()
    return valid_data


@pytest.fixture()
def created_phase(driver, created_estimate):
    estimates_page = EstimatesPageObject(driver)
    estimates_page.add_phase(created_estimate, created_estimate)
    return estimates_page.get_added_phase_name()


@pytest.fixture()
def created_feature(driver, created_estimate, created_phase):
    estimates_page = EstimatesPageObject(driver)
    estimates_page.add_feature(created_estimate)
    return estimates_page.get_added_feature_name()


@pytest.fixture()
def added_task_to_phase(driver, created_phase):
    estimates_page = EstimatesPageObject(driver)
    estimates_page.add_task_to_phase(created_phase)
    return estimates_page.get_task_name_from_phase()


def pytest_exception_interact(node, call, report):
    if driver_object := node.funcargs.get("driver"):
        allure.attach(
            body=driver_object.get_screenshot_as_png(),
            name=node.nodeid,
            attachment_type=allure.attachment_type.PNG
        )
