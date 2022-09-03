from re import T
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)

from Locators import Locators
from TestData import TestData


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.delay = 10


    def click(self, by_locator):
        WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator)).click()


    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        assert web_element == element_text


    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator)).send_keys(text)


    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))


    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        return bool(element)


    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, self.delay).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class HomePage(BasePage):
    """Home Page Opencart"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def change_currency_to_euro(self):
        pass

    def change_currency_to_poundsterling(self):
        pass

    def change_currency_to_dollar(self):
        pass

    def contact(self):
        pass

    def go_to_register_page(self):
        self.click(Locators.MY_ACCOUNT_MENU_NAVBAR)
        self.click(Locators.REGISTER_SUBMENU_NAVBAR)

    def login(self):
        pass

    def wishlist(self):
        pass

    def shopping_cart(self):
        pass

    def checkout(self):
        pass

class RegisterPage(BasePage):
    """Register Page"""
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.REGISTER_URL)

    def fill_in_all_fields(self):
        self.enter_text(Locators.FIRST_NAME_TEXT_FIELD, TestData.FIRST_NAME)
        self.enter_text(Locators.LAST_NAME_TEXT_FIELD, TestData.LAST_NAME)
        self.enter_text(Locators.EMAIL_TEXT_FIELD, TestData.EMAIL)
        self.enter_text(Locators.PASSWORD_TEXT_FIELD, TestData.PASSWORD)

    def read_and_agree(self):
        self.click(Locators.AGREEMENT_CHECK_BOX)
    
    def continue_to_register(self):
        self.click(Locators.CONTINUE_BUTTON)

    def display_warning_message(self):
        pass

class SuccessPage(BasePage):
    """Success Page"""
    def __init__(self, driver):
        super().__init__(driver)

    def continue_to_my_account_page(self):
        self.is_visible(Locators.PAGE_TITLE_TEXT)
        self.click(Locators.CONTINUE_BUTTON_AFTER_SUCCESS)