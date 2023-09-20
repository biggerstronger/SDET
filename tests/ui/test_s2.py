# -*- coding: utf-8 -*-

"""
Test Suit QAA-5
"""

import allure
import pytest

from page_objects.estimates_page_object import EstimatesPageObject
from page_objects.new_estimate_page import NewEstimatePageObject


class TestS2:
    @allure.title("QAA-5:Создание оценки")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_grade_creation(self, driver, authorize, generate_data_for_tests):
        estimates_page = EstimatesPageObject(driver)
        estimates_page.open_new_estimate_page()
        new_estimate_page = NewEstimatePageObject(driver)
        valid_data = generate_data_for_tests
        new_estimate_page.fill_fields(valid_data)
        new_estimate_page.submit_form()
        new_estimate_page.interact_with_phase_window()
        new_estimate_page.return_to_estimates_page()
        new_estimate_name = estimates_page.get_new_estimate_name(valid_data)
        assert new_estimate_name == valid_data
