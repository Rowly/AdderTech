'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from root.nested.services.parameters import parameter_singleton
import time

class SecurityPage(BasePage):
    
    def get_encryption_chosen_by_transmitter_unit_state(self):
        return self.get_state_of_element_via_css_selector("#encryption_setbytx")
    
    def set_encryption_chosen_by_transmitter_unit_state(self, state):
        self.set_state_of_element_via_css_selector("#encryption_setbytx", state)

    def get_encryption_always_on_state(self):
        return self.get_state_of_element_via_css_selector("#encryption_on")
    
    def set_encryption_always_on_state(self, state):
        self.set_state_of_element_via_css_selector("#encryption_on", state)

    def get_control_encryption_always_on_state(self):
        return self.get_state_of_element_via_css_selector("#control_encryption_on")
    
    def set_control_encryption_always_on_state(self, state):
        self.set_state_of_element_via_css_selector("#control_encryption_on", state)
    
    def get_control_encryption_always_off_state(self):
        return self.get_state_of_element_via_css_selector("#control_encryption_off")
    
    def set_control_encryption_always_off_state(self, state):
        self.set_state_of_element_via_css_selector("#control_encryption_off", state)
    
    def get_control_encryption_prefer_off_state(self):
        return self.get_state_of_element_via_css_selector("#control_encryption_preferoff")

    def set_control_encryption_prefer_off_state(self, state):
        self.set_state_of_element_via_css_selector("#control_encryption_preferoff", state)
    
    def get_secure_web_pages_with_password_state(self):
        return self.get_state_of_element_via_css_selector("#https_enable")

    def set_secure_web_pages_with_password_state(self, state):
        self.set_state_of_element_via_css_selector("#https_enable", state)
    
    def get_change_password_enabled_state(self):
        return self.get_enabled_state_of_element_via_css_selector("#change_password_cb")
    
    def get_change_password_state(self):
        return self.get_state_of_element_via_css_selector("#change_password_cb")
    
    def set_change_password_state(self, state):
        self.set_state_of_element_via_css_selector("#change_password_cb", state)
        
    def get_old_password_enabled_state(self):
        time.sleep(0.2)
        return self.get_enabled_state_of_element_via_css_selector("#old_password_txt")
    
    def get_password_enabled_state(self):
        time.sleep(0.2)
        return self.get_enabled_state_of_element_via_css_selector("#password_txt")
    
    def get_confirm_password_enabled_state(self):
        time.sleep(0.2)
        return self.get_enabled_state_of_element_via_css_selector("#confirm_password_txt")
        
    def update_config_form(self):
        try:
            self.driver.find_element_by_css_selector("#configForm_submit").click()
            self.wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "#configForm_submit"), "Save"))
        except UnexpectedAlertPresentException:
            if self.driver.name == "firefox":
                self.driver.find_element_by_css_selector("#configForm_submit").click()
            alert = self.driver.switch_to_alert()
            return alert.text

    
    
    

    
        
    
    
    
    
    
    
