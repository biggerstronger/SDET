
import allure
import pytest

from api_helper.estimates_requests import EstimatesRequests
from api_helper.validate_json import validate_json


class TestJsonSchema:

    @allure.title("QAA-5029: Создание оценки по API")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.schema
    def test_api_create_estimate(self, get_bearer_token):
        create_estimate_response = EstimatesRequests(get_bearer_token).create_estimate_json()
        assert validate_json(create_estimate_response)
