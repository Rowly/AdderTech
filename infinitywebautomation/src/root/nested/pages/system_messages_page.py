'''
Created on 19 Dec 2013

@author: Mark
'''
import re
import time

from root.nested.pages.base_page import BasePage
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SystemMessagesPage(BasePage):

    def get_enable_system_messages_state(self):
        self.driver.refresh()
        time.sleep(1)
        return self.get_state_of_element_via_css("#enable")

    def set_enable_system_messages_state(self, state):
        self.set_state_of_element_via_css("#enable", state)

    def get_send_system_messages_to_remote_log_server_enabled_state(self):
        return self.get_enabled_state_of_element_via_css("#remote")

    def get_send_system_messages_to_remote_log_server_state(self):
        return self.get_state_of_element_via_css("#remote")

    def set_send_system_messages_to_remote_log_server_state(self, state):
        self.set_state_of_element_via_css("#remote", state)

    def set_store_system_mesages_in_unit(self, state):
        self.set_state_of_element_via_css("#local", state)

    def get_log_server_ip_address(self):
        return self.get_attribute_of_element_via_css("#server_ip", "value")

    def set_log_server_ip_address(self, ip):
        self.set_text_of_element_via_css("#server_ip", ip)

    def click_view_messages(self):
        self.click_button_by_css("#viewlogfile")

    def get_main_window_handle(self):
        return self.driver.current_window_handle

    def get_system_messages_from_new_window(self, main_window):
        handles = self.driver.window_handles
        for handle in handles:
            if handle != main_window:
                self.driver.switch_to_window(handle)
                break
        return self.get_text_of_element_via_css("textarea")

    def messages_start_header_is_correct(self, messages):
        match = re.search(r"[=== /var/log/messages]", messages)
        return match

    def update_config_form(self):
        l_wait = WebDriverWait(self.driver, 30)
        time.sleep(1)
        try:
            path = "#configForm_submit"
            self.driver.find_element_by_css_selector(path).click()
            loc = By.CSS_SELECTOR, path
            exp = "Update Now"
            l_wait.until(EC.text_to_be_present_in_element_value(loc, exp))
        except UnexpectedAlertPresentException:
            alert = self.driver.switch_to_alert()
            return alert.text
        return self.click_update_button("#configForm_submit")

    def dismiss_alert_if_present(self):
        try:
            self.driver.switch_to_default_content()
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception:
            pass
