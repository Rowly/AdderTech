'''
Created on 19 Dec 2013

@author: Mark
'''
import time
from root.nested.pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SecurityPage(BasePage):

    def get_encryption_chosen_by_transmitter_unit_state(self):
        return self.get_state_of_element_via_css("#encryption_setbytx")

    def set_encryption_chosen_by_transmitter_unit_state(self, state):
        self.set_state_of_element_via_css("#encryption_setbytx", state)

    def get_encryption_always_on_state(self):
        return self.get_state_of_element_via_css("#encryption_on")

    def set_encryption_always_on_state(self, state):
        self.set_state_of_element_via_css("#encryption_on", state)

    def get_control_encryption_always_on_state(self):
        return self.get_state_of_element_via_css("#control_encryption_on")

    def set_control_encryption_always_on_state(self, state):
        self.set_state_of_element_via_css("#control_encryption_on", state)

    def get_control_encryption_always_off_state(self):
        return self.get_state_of_element_via_css("#control_encryption_off")

    def set_control_encryption_always_off_state(self, state):
        self.set_state_of_element_via_css("#control_encryption_off", state)

    def get_control_encryption_prefer_off_state(self):
        path = "#control_encryption_preferoff"
        return self.get_state_of_element_via_css(path)

    def set_control_encryption_prefer_off_state(self, state):
        path = "#control_encryption_preferoff"
        self.set_state_of_element_via_css(path, state)

    def get_secure_web_pages_with_password_state(self):
        return self.get_state_of_element_via_css("#https_enable")

    def set_secure_web_pages_with_password_state(self, state):
        self.set_state_of_element_via_css("#https_enable", state)

    def get_change_password_enabled_state(self):
        return self.get_state_of_element_via_css("#change_password_cb")

    def get_change_password_state(self):
        return self.get_state_of_element_via_css("#change_password_cb")

    def set_change_password_state(self, state):
        self.set_state_of_element_via_css("#change_password_cb", state)

    def get_old_password_enabled_state(self):
        time.sleep(0.2)
        return self.get_state_of_element_via_css("#old_password_txt")

    def get_password_enabled_state(self):
        time.sleep(0.2)
        return self.get_state_of_element_via_css("#password_txt")

    def get_confirm_password_enabled_state(self):
        time.sleep(0.2)
        return self.get_state_of_element_via_css("#confirm_password_txt")

    def update_config_form(self):
        try:
            path = "#configForm_submit"
            self.driver.find_element_by_css_selector(path).click()
            loc = By.CSS_SELECTOR, path
            exp = "Save"
            self.wait.until(EC.text_to_be_present_in_element_value(loc, exp))
        except UnexpectedAlertPresentException:
            if self.driver.name == "firefox":
                self.driver.find_element_by_css_selector(path).click()
            alert = self.driver.switch_to_alert()
            return alert.text
