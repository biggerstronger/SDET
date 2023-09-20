# -*- coding: utf-8 -*-

"""
Page Object for Estimates page
"""

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page_object import BasePageObject


class EstimatesPageObject(BasePageObject):
    """
    The class implements the estimates page
    """

    _plus_button = (By.XPATH, "//button[@id='open-menu-button']")
    _language_choice = (By.CSS_SELECTOR, ".md-whiteframe-6dp.adding-area-block.ng-scope > div")
    _button_login = (By.XPATH, "//button['login-btn']")
    _button_rating_in_title = (By.XPATH, "//button[@id='toggle-side-nav-button']")
    _new_estimate_entry = (By.XPATH, "//strong[@class='task-item-name ng-binding'][text()='{}']")
    _delete_estimate_button = (By.XPATH, "//button[@id='disable-deletion-button'][@tabindex='0']")
    _accept_deletion_button = (By.XPATH, "//button[@ng-click='dialog.hide()']")
    _add_phase_button = (By.XPATH, "//button[@id='add-phase-button']")
    _phase_checkbox = (By.XPATH, "//md-checkbox[@aria-label='{}']")
    _save_phase_button = (By.XPATH, "//button[@ng-click='vm.saveAddingPhases()']")
    _custom_phase_name_input = (By.XPATH, "//input[@id='save-adding-phases-button']")
    _all_phases = (By.XPATH, "//md-tab-item[@ng-click='$mdTabsCtrl.select(tab.getIndex())']")
    _input_feature = (By.XPATH, "//input[@type='search']")
    _feature_autocomplete = (By.XPATH, "//span[text()='{}']")
    _feature_table = (By.XPATH, "//div[@ng-repeat='(itemIndex, item) in vm.items track by item._id']")
    _feature_comment_button = (By.XPATH, "//md-icon[@ng-click='vm.toggleDescription()']")
    _feature_comment_field = (By.XPATH, "//textarea[@id='description-textarea']")
    _add_task_to_phase_button = (By.XPATH, "//button[@ng-click='vm.openFab($event)']")
    _add_new_task_button = (By.XPATH, "//div[@ng-click='vm.addNewTask($event)']")
    _task_checkbox = (By.XPATH, "//div[text()='{}']")
    _save_new_task_to_phase = (By.CSS_SELECTOR, "[ng-click='vm.saveAddingTasks()']")
    _new_task_to_phase_input = (By.XPATH, "//textarea[@id='task-name-textarea']")
    _min_hours = (By.XPATH, "//input[@id='min-hours-input']")
    _max_hours = (By.XPATH, "//input[@id='max-hours-input']")
    _phase_hours = (By.XPATH, "//div[@class='ng-binding flex-45']")
    _edit_phases_button = (By.XPATH, "//button[@ng-click='vm.openEditPhase()']")
    _delete_phase_button = (By.XPATH, "//button[@id='delete-phase-button']")
    _confirm_deletion_button = (By.XPATH, "//span[text()='ОК']")

    def _choose_russian_language(self) -> None:
        russian_language = self.find_element(self._language_choice)
        russian_language.click()

    @allure.step("Получение текущего адреса страницы")
    def get_url(self) -> str:
        self.wait_until_element_located(self._button_rating_in_title, "Вход на сайт не осуществлен")
        return self._driver.current_url

    @allure.step("Проверка создание новой оценки")
    def get_new_estimate_name(self, new_estimate_name) -> str:
        return self.find_element(
            (
                self._new_estimate_entry[0],
                self._new_estimate_entry[1].format(new_estimate_name),
            ),
        ).text

    @allure.step("Открытие страницы создания новой оценки")
    def open_new_estimate_page(self) -> None:
        plus_button = self.find_element(self._plus_button)
        plus_button.click()
        self._choose_russian_language()

    @allure.step("Удаление записи об оценке")
    def delete_estimate(self, estimate_name: str) -> bool:
        self.click_button(self._delete_estimate_button)
        self.click_button(self._accept_deletion_button)
        accept_deletion_window = self.find_element(self._accept_deletion_button)
        accept_deletion_window.send_keys(Keys.RETURN)
        self.wait_until_element_invisible(
            (
                self._new_estimate_entry[0],
                self._new_estimate_entry[1].format(estimate_name),
            ),
        )
        return estimate_name not in self._driver.page_source

    @allure.step("Добавление фазы к оценке")
    def add_phase(self, estimate_name: str, phase_name: str) -> None:
        self.click_button(
            (
                self._new_estimate_entry[0],
                self._new_estimate_entry[1].format(estimate_name),
            ),
        )
        self.click_button(self._add_phase_button)
        checkbox: WebElement = self.find_clickable_element(
            (
                self._phase_checkbox[0],
                self._phase_checkbox[1].format(phase_name),
            ),
        )
        if checkbox and phase_name == checkbox.text:
            checkbox.click()
        else:
            self.find_element(self._custom_phase_name_input).send_keys(estimate_name)
        self.click_button(self._save_phase_button)
        self.wait_until_element_invisible(self._save_phase_button)

    def get_added_phase_name(self) -> str:
        self._driver.refresh()
        return self.find_elements(self._all_phases)[-1].text

    @allure.step("Добавление фичи в оценку")
    def add_feature(self, feature_name: str) -> None:
        first_phase = self.find_elements(self._all_phases)[-1]
        first_phase.click()
        feature_input: WebElement = self.find_clickable_element(self._input_feature)
        feature_input.send_keys(feature_name)
        feature = self.find_clickable_element(
            (
                self._feature_autocomplete[0],
                self._feature_autocomplete[1].format(feature_name),
            ),
        )
        if feature and feature.text == feature_name:
            feature_input.send_keys(Keys.ARROW_DOWN)
        feature_input.send_keys(Keys.RETURN)

    @allure.step("Получение имени добавленной фичи")
    def get_added_feature_name(self) -> str:
        return self.find_elements(self._feature_table)[-1].text.split("\n")[0]

    @allure.step("Добавление комментария в фичу")
    def add_comment_to_feature(self, comment: str) -> None:
        self.click_button(self._feature_comment_button)
        comment_field = self.find_element(self._feature_comment_field)
        comment_field.send_keys(comment)
        self.click_button(self._feature_comment_button)
        self.click_button(self._feature_comment_button)

    @allure.step("Получение добавленного в фичу комментария")
    def get_feature_comment(self) -> str:
        comment_field = self.find_element(self._feature_comment_field)
        return comment_field.text

    @allure.step("Добавление задачи в фазу")
    def add_task_to_phase(self, task_name: str) -> None:
        self.find_elements(self._all_phases)[-1].click()
        self.find_clickable_element(self._add_task_to_phase_button).click()
        self.find_clickable_element(self._add_new_task_button).click()
        task_from_catalog = self.find_clickable_element(
            (
                self._task_checkbox[0],
                self._task_checkbox[1].format(task_name),
            ),
        )
        if task_from_catalog and task_from_catalog.text == task_name:
            task_from_catalog.click()
        else:
            self.find_element(self._new_task_to_phase_input).send_keys(task_name)
        self.click_button(self._save_new_task_to_phase)

    @allure.step("Получение имени задачи из фазы")
    def get_task_name_from_phase(self) -> str:
        return self.find_elements(self._feature_table)[-1].text.split("\n")[0]

    @allure.step("Добавления времени 'ОТ' в фичу")
    def add_min_hours(self, min_hours: float) -> None:
        self.find_element(self._min_hours).send_keys(Keys.BACKSPACE)
        self.find_element(self._min_hours).send_keys(Keys.BACKSPACE)
        self.find_element(self._min_hours).send_keys(Keys.BACKSPACE)
        self.find_element(self._min_hours).send_keys(min_hours)
        self.find_element(self._new_task_to_phase_input).click()

    @allure.step("Добавления времени 'ДО' в фичу")
    def add_max_hours(self, max_hours: float) -> None:
        self.find_element(self._max_hours).send_keys(Keys.BACKSPACE)
        self.find_element(self._max_hours).send_keys(Keys.BACKSPACE)
        self.find_element(self._max_hours).send_keys(Keys.BACKSPACE)
        self.find_element(self._max_hours).send_keys(max_hours)
        self.find_element(self._new_task_to_phase_input).click()

    @allure.step("Получение рассчитанного времени")
    def get_evaluated_hours(self) -> tuple[str, str]:
        hours_tuple = self.find_elements(self._phase_hours)
        return hours_tuple[0].text, hours_tuple[1].text

    @allure.step("Удаление фазы из оценки")
    def remove_phase_from_estimate(self) -> None:
        self.click_button(self._edit_phases_button)
        self.click_button(self._delete_phase_button)
        self.click_button(self._confirm_deletion_button)
        self._driver.refresh()

    @allure.step("Проверка появления кнопки добавления фазы")
    def check_buttons_on_estimate_page(self) -> bool:
        return self.find_element((By.XPATH, "//button[@id='add-phase-button']")).is_displayed()
