# -*- coding: utf-8 -*-

"""
Page Object for New estimate page
"""
import allure
from selenium.webdriver.common.by import By
from page_objects.base_page_object import BasePageObject


class NewEstimatePageObject(BasePageObject):
    """
    The class implements the new estimate page
    """
    _client_field = "//textarea[@name = 'customer']"
    _project_name_field = "//textarea[@aria-label='Название проекта']"
    _moderator_field = "//button['login-btn']"
    _crm_link_field = "//textarea[@name='linkToCRM']"
    _estimates_button_in_title = "//a[@ui-sref='index.estimates'][@ui-sref-opts]"
    _submit_button = "//button[@id='edit-about-button']"
    _dialog_close_element = "[ng-click='vm.closeModal()']"

    def get_url(self):
        self.wait_until_element_located((By.XPATH, self._client_field), "Страница создания оценки не открыта")
        return self._driver.current_url

    @allure.step("Заполнение полей новой оценки")
    def fill_fields(self, valid_data):
        client_field = self.find_element((By.XPATH, self._client_field))
        client_field.send_keys(valid_data)
        project_name_field = self.find_element((By.XPATH, self._project_name_field))
        project_name_field.send_keys(valid_data)
        srm_link_field = self.find_element((By.XPATH, self._crm_link_field))
        srm_link_field.send_keys(valid_data)

    @allure.step("Подтверждение создания новой оценки")
    def submit_form(self):
        save_and_add_phase_btn = self.find_element((By.XPATH, self._submit_button))
        save_and_add_phase_btn.click()

    @allure.step("Закрытие всплывающего окна добавления фазы")
    def interact_with_phase_window(self):
        dialog_close_element = self.find_clickable_element((By.CSS_SELECTOR, self._dialog_close_element))
        dialog_close_element.click()

    @allure.step("Редирект на страницу всех оценок")
    def return_to_estimates_page(self):
        self._driver.refresh()
        all_estimates_button = self.find_element((By.XPATH, self._estimates_button_in_title))
        all_estimates_button.click()
