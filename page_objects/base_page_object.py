# -*- coding: utf-8 -*-

"""
Base Page Object
"""

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePageObject:
    def __init__(self, driver):
        self._driver = driver

    def title(self):
        return self._driver.title

    def page_source(self):
        return self._driver.page_source

    def find_element(self, element_locator, time=20) -> any:
        return WebDriverWait(self._driver, time).until(
            ec.presence_of_element_located(element_locator),
            message=f"Can't find element by locator {element_locator}",
        )

    def find_elements(self, element_locator, time=20) -> any:
        return WebDriverWait(self._driver, time).until(
            ec.presence_of_all_elements_located(element_locator),
            message=f"Can't find elements by locator {element_locator}",
        )

    def find_clickable_element(self, element_locator, time=5):
        try:
            return WebDriverWait(self._driver, time).until(
                ec.element_to_be_clickable(element_locator),
                message=f"Can't find element by locator {element_locator}",
            )
        except (TimeoutException, ElementClickInterceptedException):
            return None

    def wait_until_element_invisible(self, element_locator, time=3):
        return WebDriverWait(self._driver, time).until(
            ec.invisibility_of_element(element_locator),
            message=f"Can't find element by locator {element_locator}",
        )

    def wait_until_element_located(self, element_locator, exception_message=None):
        try:
            return WebDriverWait(self._driver, 3).until(
                ec.presence_of_element_located(element_locator))
        except TimeoutException:
            print(exception_message)
        return None

    def is_url_changes_to(self, url):
        try:
            WebDriverWait(self._driver, 3).until(ec.url_to_be(url), message=f"URL не изменился на {url}")
            return True
        except TimeoutException:
            return False

    def click_button(self, element_locator: tuple) -> None:
        self.find_clickable_element(element_locator=element_locator).click()
