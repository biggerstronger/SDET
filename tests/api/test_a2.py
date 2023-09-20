"""
A2 Test suit
"""

import allure
import pytest

from api_helper.estimates_requests import EstimatesRequests


class TestA2:
    """
    A2 Test class
    """

    @allure.title("QAA-5029: Создание оценки по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_api_create_estimate(self, get_bearer_token):
        create_estimate_response = EstimatesRequests(get_bearer_token).create_estimate()
        assert create_estimate_response.status_code == 200 and create_estimate_response._id

    @allure.title("QAA-5030: Удаление оценки по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_api_delete_estimate(self, get_bearer_token, create_new_estimate):
        delete_estimate_request = EstimatesRequests(get_bearer_token).delete_estimate(create_new_estimate)
        assert delete_estimate_request == f"{create_new_estimate} removed"

    @allure.title("QAA-5031: Копирование оценки по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_api_copy_estimate(self, get_bearer_token, create_new_estimate):
        copy_estimate_request = EstimatesRequests(get_bearer_token).copy_estimate(create_new_estimate)
        assert "копия" in copy_estimate_request.name
