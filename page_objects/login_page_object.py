# -*- coding: utf-8 -*-

"""
Page Object for Login page
"""
import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from page_objects.base_page_object import BasePageObject


class LoginPageObject(BasePageObject):
    """
    The class implements the login page
    """

    _input_login = "//input[@id = 'input_0']"
    _input_pass = "//input[@id = 'input_1']"
    _button_login = "//button['login-btn']"
    _button_rating_in_title = "//button[@id='toggle-side-nav-button']"
    _message_error = "//div[@class='error-msg ng-binding']"

    @allure.step("Получение текущего адреса страницы")
    def get_url(self):
        self.wait_until_element_located((By.XPATH, self._button_rating_in_title), "Вход на сайт не осуществлен")
        return self._driver.current_url

    @allure.step("Логин")
    def do_login(self, login, password):
        self._driver.find_element(By.XPATH, self._input_login).send_keys(login)
        self._driver.find_element(By.XPATH, self._input_pass).send_keys(password)
        self._driver.find_element(By.XPATH, self._button_login).click()

    @allure.step("Получение данных из поля Логин")
    def get_login_input_value(self):
        return self._driver.find_elements(By.XPATH, self._input_login)[0].get_attribute("value")

    @allure.step("Получение данных из поля Пароль")
    def get_pass_input_value(self):
        return self._driver.find_elements(By.XPATH, self._input_pass)[0].get_attribute("value")

    @allure.step("Получение ошибки Неправильного пользователя")
    def get_message_error(self):
        try:
            WebDriverWait(self._driver, 1).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, self._message_error), "User not found"))
        except TimeoutException:
            print("Timed out waiting for element to load 'User not found'")
            return ""
        return str(self._driver.find_elements(By.XPATH, self._message_error)[0].text)
