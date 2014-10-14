'''
Created on 19 Dec 2013

@author: Mark
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from root.nested.pages.base_page import BasePage

class StatisticsPage(BasePage):
    
    def get_enable_statistics_state(self):
        return self.get_state_of_element_via_css_selector("#monitord_enable")
    
    def set_enable_statistics_state(self, state):
        self.set_state_of_element_via_css_selector("#monitord_enable", state)
    
    def click_submit(self):
        self.click_button_by_css_selector(".submit")
        self.driver.refresh()
    
    def get_appearance_of_graph(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#theChart"))).is_displayed()
    
    
