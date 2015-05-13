'''
Created on 19 Dec 2013

@author: Mark
'''
import time

from root.nested.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class RebootPage(BasePage):

    def click_reboot(self):
        self.click_button_by_css("#rebootbutton")

    def set_factory_reset_state(self, state):
        error = True
        while(error):
            try:
                self.set_state_of_element_via_css("#factory_reset", state)
                error = False
            except TimeoutException:
                self.driver.refresh()

    def get_reboot_message(self):
        locator = By.CSS_SELECTOR, "#rebootdiv_outer > b"
        expected = ("The unit has been reset to factory settings. " +
                    "IP Address has been reset to factory default. " +
                    "The new IP address will be in the 169.254.*.* range.")
        self.wait.until(EC.text_to_be_present_in_element(locator, expected))
        el = self.driver.find_element_by_css_selector("#rebootdiv_outer > b")
        return el.text

    def wait_for_reboot_to_complete(self):
        l_wait = WebDriverWait(self.driver, 60)
        if self.driver.name == "chrome":
            try:
                locator = By.CSS_SELECTOR, "#reload-button"
                l_wait.until(EC.presence_of_element_located(locator)).click()
            except:
                NoSuchElementException
        else:
            time.sleep(30)
        locator = By.LINK_TEXT, "Reboot"
        l_wait.until(EC.presence_of_element_located(locator)).click()

    def wait_for_factory_reset_to_complete(self):
        time.sleep(60)
        self.driver.refresh()
