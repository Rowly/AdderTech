'''
Created on 11 Dec 2013

@author: Mark
'''
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException,\
    TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class BasePage(object):

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def get_logo_text(self):
        return self.get_text_of_element_via_css_selector(".logotext2")
    
    def get_main_header_text(self):
        return self.get_text_of_element_via_css_selector("#right>h1")
    
    def click_menu_link(self, link_text):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text))).click()
    
    def get_text_of_element_via_css_selector(self, selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).text
    
    def get_attribute_of_element_via_css_selector(self, selector, attribute):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).get_attribute(attribute)
    
    def get_css_value_of_element_via_css_selector(self, selector, css_value):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).value_of_css_property(css_value)
    
    def set_text_of_element_via_css_selector(self, selector, text):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).clear()
        self.driver.find_element_by_css_selector(selector).send_keys(text)
    
    def get_state_of_element_via_css_selector(self, selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).is_selected()

    def set_state_of_element_via_css_selector(self, selector, state):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        if self.get_state_of_element_via_css_selector(selector) == state:
            pass
        else: self.driver.find_element_by_css_selector(selector).click()
    
    def click_button_by_css_selector(self, selector):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).click()
    
    def get_visible_state_of_element_by_css_selector(self, selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).is_displayed()
    
    def get_selected_value_of_select_element_by_css_selector(self, selector):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        select = Select(self.driver.find_element_by_css_selector(selector))
        return select.first_selected_option.text
    
    def select_visible_text_value_of_select_element_by_css_selector(self, selector, text):
        select = Select(self.driver.find_element_by_css_selector(selector))
        select.select_by_visible_text(text)
    
    def get_all_option_text_values_from_select_element_by_css_selector(self, selector):
        options = []
        select = Select(self.driver.find_element_by_css_selector(selector))
        for item in select.options:
            if item.text != "None":
                options.append(item.text)
        return options
    
    def get_enabled_state_of_element_via_css_selector(self, selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector))).is_enabled()
    
    def get_text_of_element_via_xpath(self, selector):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, selector))).text
    
    def click_update_button(self, selector):
        if self.driver.name == "phantomjs":
            return self.click_update_button_with_phantomjs(selector)
        elif self.driver.name != "phantomjs":
            long_wait = WebDriverWait(self.driver, 60)
            time.sleep(1)
            try:
                self.driver.find_element_by_css_selector(selector).click()
                long_wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, selector), "Update Now"))
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
        long_wait = WebDriverWait(self.driver, 60)
        self.driver.find_element_by_css_selector(selector).click()
        long_wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, selector), "Update Now"))
        time.sleep(1)
        alert = self.driver.execute_script("return window.getLastAlert && window.getLastAlert();")
        self.driver.refresh()
        return alert
