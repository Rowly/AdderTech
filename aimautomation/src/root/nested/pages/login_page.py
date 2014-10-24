'''
Created on 9 Jul 2014

@author: Mark
'''
from root.nested.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from root.nested.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):
    
    def login(self):
        self.wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("password")
        self.driver.find_element_by_id("login").click()
        return DashboardPage(self.driver, self.wait)
    
    def login_as_user(self, user, password, remember):
        self.wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys(user)
        self.driver.find_element_by_id("password").send_keys(password)
        if remember:
            self.driver.find_element_by_id("remember_me").click()
        self.driver.find_element_by_id("login").click()
        return DashboardPage(self.driver, self.wait)
