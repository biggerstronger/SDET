# -*- coding: utf-8 -*-

"""
Test Suit for QAA-2...QAA-4
"""
import os
import socket
import pytest

import allure
from page_objects.login_page_object import LoginPageObject


class TestS1:
    TARGET_URL = f"{os.getenv('APP_URL')}login"
    ERROR_MESSAGE = "User not found"

    @allure.title("QAA-2:Авторизация с несуществующим логином и паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_login_with_wrong_credentials(self, driver):
        login_page_object = LoginPageObject(driver)
        login_page_object.do_login(os.getenv("INVALID_LOGIN"), os.getenv("INVALID_PASSWORD"))
        param_url = login_page_object.get_url()

        assert login_page_object.get_message_error() == self.ERROR_MESSAGE
        assert str(param_url) == self.TARGET_URL

    @allure.title("QAA-3:Авторизация с корректным логином и пустым паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_login_with_empty_password_field(self, driver):
        login_page_object = LoginPageObject(driver)
        login_page_object.do_login(os.getenv("VALID_LOGIN"), os.getenv("EMPTY_PASSWORD"))
        param_url = LoginPageObject(driver).get_url()

        assert login_page_object.get_login_input_value() == os.getenv("VALID_LOGIN")
        assert login_page_object.get_pass_input_value() == os.getenv("EMPTY_PASSWORD")
        assert str(param_url) == self.TARGET_URL

    @allure.title("QAA-4:Авторизация с пустыми логином и паролем")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_login_with_empty_fields(self, driver):
        login_page_object = LoginPageObject(driver)
        login_page_object.do_login(os.getenv("EMPTY_LOGIN"), os.getenv("EMPTY_PASSWORD"))
        param_url = LoginPageObject(driver).get_url()

        assert login_page_object.get_login_input_value() == os.getenv("EMPTY_LOGIN")
        assert login_page_object.get_pass_input_value() == os.getenv("EMPTY_PASSWORD")
        assert str(param_url) == self.TARGET_URL
