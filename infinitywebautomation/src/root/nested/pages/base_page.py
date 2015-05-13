'''
Created on 11 Dec 2013

@author: Mark
'''
import time

from selenium.common.exceptions import (UnexpectedAlertPresentException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def get_logo_text(self):
        return self.get_text_of_element_via_css(".logotext2")

    def get_main_header_text(self):
        return self.get_text_of_element_via_css("#right > h1")

    def click_menu_link(self, link_text):
        locator = By.LINK_TEXT, link_text
        self.wait.until(EC.presence_of_element_located(locator)).click()

    def get_text_of_element_via_css(self, selector):
        locator = By.CSS_SELECTOR, selector
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def get_attribute_of_element_via_css(self, selector, attribute):
        locator = By.CSS_SELECTOR, selector
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.get_attribute(attribute)

    def get_css_value_of_element_via_css(self, selector, css_value):
        locator = By.CSS_SELECTOR, selector
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.value_of_css_property(css_value)

    def set_text_of_element_via_css(self, selector, text):
        locator = By.CSS_SELECTOR, selector
        self.wait.until(EC.presence_of_element_located(locator)).clear()
        self.driver.find_element_by_css_selector(selector).send_keys(text)

    def get_state_of_element_via_css(self, selector):
        locator = By.CSS_SELECTOR, selector
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.is_selected()

    def set_state_of_element_via_css(self, selector, state):
        locator = By.CSS_SELECTOR, selector
        self.wait.until(EC.presence_of_element_located(locator))
        if self.get_state_of_element_via_css(selector) == state:
            pass
        else:
            self.driver.find_element_by_css_selector(selector).click()

    def click_button_by_css(self, selector):
        locator = By.CSS_SELECTOR, selector
        self.wait.until(EC.presence_of_element_located(locator)).click()

    def get_visibility_of_element_by_css(self, selector):
        locator = By.CSS_SELECTOR, selector
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.is_displayed()

    def get_selected_value_of_select_element_by_css(self, selector):
        locator = By.CSS_SELECTOR, selector
        self.wait.until(EC.presence_of_element_located(locator))
        select = Select(self.driver.find_element_by_css_selector(selector))
        return select.first_selected_option.text

    def select_text_of_select_element_by_css(self, selector, text):
        select = Select(self.driver.find_element_by_css_selector(selector))
        select.select_by_visible_text(text)

    def get_options_from_select_element_by_css(self, selector):
        items = Select(self.driver.find_element_by_css_selector(selector))
        options = [item.text
                   for item in items
                   if item.text != "None"]
        return options

    def get_enabled_state_of_element_via_css(self, selector):
        locator = By.CSS_SELECTOR, selector
        el = self.wait.until(EC.presence_of_element_located(locator))
        return el.is_enabled()

    def get_text_of_element_via_xpath(self, selector):
        locator = By.XPATH, selector
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def click_update_button(self, selector):
        if self.driver.name == "phantomjs":
            return self.click_update_button_with_phantomjs(selector)
        elif self.driver.name != "phantomjs":
            l_wait = WebDriverWait(self.driver, 60)
            time.sleep(1)
            try:
                self.driver.find_element_by_css_selector(selector).click()
                loc = By.CSS_SELECTOR, selector
                text = "Update Now"
                l_wait.until(EC.text_to_be_present_in_element_value(loc, text))
            except UnexpectedAlertPresentException:
                if self.driver.name == "firefox":
                    self.driver.find_element_by_css_selector(selector).click()
                alert = self.driver.switch_to_alert()
                return alert.text
            except TimeoutException:
                self.driver.refresh()

    def click_update_button_with_phantomjs(self, selector):
        js = """
        (function () {
        var lastAlert = undefined;
        window.alert = function (message) {
            lastAlert = message;
        };
        window.getLastAlert = function () {
        var result = lastAlert;
        lastAlert = undefined;
        return result;
        };
        }());
        """
        self.driver.execute_script(js)
        l_wait = WebDriverWait(self.driver, 60)
        self.driver.find_element_by_css_selector(selector).click()
        locator = By.CSS_SELECTOR, selector
        expect = "Update Now"
        l_wait.until(EC.text_to_be_present_in_element_value(locator, expect))
        time.sleep(1)
        script = "return window.getLastAlert && window.getLastAlert();"
        alert = self.driver.execute_script(script)
        self.driver.refresh()
        return alert
