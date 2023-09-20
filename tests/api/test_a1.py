"""
A1 Test suit
"""


import os
import allure
import pytest

from api_helper.authorize_request import AuthorizeRequest
from api_helper.change_role_request import ChangeRoleRequest
from data.schemas import authorize_schema


class TestA1:
    """
    A1 Test class
    """

    @allure.title("QAA-48: Авторизация по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_api_login(self):
        authorize_response = AuthorizeRequest().authorize(
            authorize_schema.AuthorizeRequestSchema(
                os.getenv("ADMIN_LOGIN"),
                os.getenv("ADMIN_PASSWORD"),
            ),
        )
        assert authorize_response.status_code == 200 and authorize_response.token

    @allure.title("QAA-57: Изменение роли пользователя по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_change_user_role_to_moderator(self, get_bearer_token, get_moderator_role_id):
        change_role_request = ChangeRoleRequest(get_bearer_token).change_role(get_moderator_role_id)
        assert change_role_request.role_name == "moderator"

    @allure.title("QAA-57: Изменение роли пользователя по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_change_user_role_to_estimator(self, get_bearer_token, get_estimator_role_id):
        change_role_request = ChangeRoleRequest(get_bearer_token).change_role(get_estimator_role_id)
        assert change_role_request.role_name == "estimator"
