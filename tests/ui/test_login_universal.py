# -*- coding: utf-8 -*-

"""
Test Suit for QAA-2...QAA-4
"""
import os

import allure
import pytest

from page_objects.login_page_object import LoginPageObject


class TestS4:
    ERROR_MESSAGE = "User not found"

    @allure.title("S4: Универсальный тест")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "login, password, expected",
        [
            (
                    os.getenv("VALID_LOGIN"),
                    os.getenv("VALID_PASSWORD"),
                    (f"{os.getenv('APP_URL')}estimates", ""),
            ),
            (
                    os.getenv("INVALID_LOGIN"),
                    os.getenv("INVALID_PASSWORD"),
                    (f"{os.getenv('APP_URL')}login", "User not found"),
            ),
            (
                    os.getenv("VALID_LOGIN"),
                    os.getenv("EMPTY_PASSWORD"),
                    (f"{os.getenv('APP_URL')}login", ""),
            ),
            (
                    os.getenv("EMPTY_LOGIN"),
                    os.getenv("EMPTY_PASSWORD"),
                    (f"{os.getenv('APP_URL')}login", ""),
            ),
        ]
    )
    def test_login_with_different_credentials(
            self,
            driver,
            login,
            password,
            expected,
    ):
        """
        Universal test for login
        """
        login_page_object = LoginPageObject(driver)
        login_page_object.do_login(login, password)
        page_url = login_page_object.get_url()
        error_message = login_page_object.get_message_error()
        assert (page_url, error_message) == expected
