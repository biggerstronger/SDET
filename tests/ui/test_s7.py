# -*- coding: utf-8 -*-

"""
Test Suit QAA-6...QAA-20
"""
from random import randint

import allure
import pytest

from page_objects.estimates_page_object import EstimatesPageObject


class TestS7:
    @allure.title("QAA-6:Удаление оценки")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_delete_estimate(self, driver, created_estimate):
        estimates_page = EstimatesPageObject(driver)
        assert estimates_page.delete_estimate(created_estimate)

    @allure.title("QAA-7:Добавление фазы из справочника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_phase_to_estimate(self, driver, created_estimate):
        estimates_page = EstimatesPageObject(driver)
        phase_name = "Мобильное приложение"
        estimates_page.add_phase(created_estimate, phase_name)
        assert estimates_page.get_added_phase_name() == phase_name.upper()

    @allure.title("QAA-8:Добавление кастомной фазы не из справочника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_custom_phase_to_estimate(self, driver, created_estimate):
        estimates_page = EstimatesPageObject(driver)
        estimates_page.add_phase(created_estimate, created_estimate)
        assert estimates_page.get_added_phase_name() == created_estimate.upper()

    @allure.title("QAA-9:Добавление фичи в фазу из справочника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_feature_from_catalog_to_estimate(self, driver, created_phase):
        estimates_page = EstimatesPageObject(driver)
        feature_from_catalog = "Реализация http (json) запросов с парсингом"
        estimates_page.add_feature(feature_from_catalog)
        assert estimates_page.get_added_feature_name() == feature_from_catalog

    @allure.title("QAA-10:Добавление фичи в фазу вручную не из справочника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_custom_feature_to_estimate(self, driver, created_phase):
        estimates_page = EstimatesPageObject(driver)
        estimates_page.add_feature(created_phase)
        assert estimates_page.get_added_feature_name() == created_phase

    @allure.title("QAA-11:Добавление описания фичи")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_comment_to_feature(self, driver, created_feature):
        estimates_page = EstimatesPageObject(driver)
        estimates_page.add_comment_to_feature(created_feature)
        assert estimates_page.get_feature_comment() == created_feature

    @allure.title("QAA-15:Добавление описания задачи")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_comment_to_task_in_phase(self, driver, added_task_to_phase):
        estimates_page = EstimatesPageObject(driver)
        estimates_page.add_comment_to_feature(added_task_to_phase)
        assert estimates_page.get_feature_comment() == added_task_to_phase

    @allure.title("QAA-16:Добавление задачи в фазу вручную не из справочника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_custom_task_to_phase(self, driver, added_task_to_phase):
        estimates_page = EstimatesPageObject(driver)
        assert estimates_page.get_task_name_from_phase() == added_task_to_phase

    @allure.title("QAA-17:Добавление задачи в фазу из справочника")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_task_to_phase(self, driver, created_phase):
        estimates_page = EstimatesPageObject(driver)
        task_name = "Реализация http (json) запросов с парсингом"
        estimates_page.add_task_to_phase(task_name)
        assert estimates_page.get_task_name_from_phase() == task_name

    @allure.title("QAA-18:Добавление часов в поле 'ОТ'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_min_hours(self, driver, added_task_to_phase):
        estimates_page = EstimatesPageObject(driver)
        expected_time = randint(1, 80) / 10
        estimates_page.add_min_hours(expected_time)
        assert estimates_page.get_evaluated_hours()[0] == str(round(expected_time * 1.15, 1))

    @allure.title("QAA-19::Добавление часов в поле 'ДО'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_add_max_hours(self, driver, added_task_to_phase):
        estimates_page = EstimatesPageObject(driver)
        expected_time = randint(1, 80) / 10
        estimates_page.add_max_hours(expected_time)
        assert estimates_page.get_evaluated_hours()[1] == str(round(expected_time * 1.15, 1))

    @allure.title("QAA-20:Удаление фазы")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_remove_phase_from_estimate(self, driver, created_phase):
        estimates_page = EstimatesPageObject(driver)
        estimates_page.remove_phase_from_estimate()
        assert estimates_page.check_buttons_on_estimate_page()
