'''
Created on 9 Jul 2014

@author: Mark
'''
from root.nested.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from root.nested.pages.mail_settings_page import MailSettingsPage

class SettingsPage(BasePage):
    
    def click_general_button(self):
        self.click_button("General")
        return self 
    
    def click_transmitters_button(self):
        self.click_button("Transmitters")
        #TODO: Create Transmitters Settings Page object
    
    def click_receivers_button(self):
        self.click_button("Receivers")
        #TODO:Create Receivers Settings Page object
    
    def click_servers_button(self):
        self.click_button("Servers")
        #TODO:Create Servers Settings Page object
    
    def click_network_button(self):
        self.click_button("Network")
        #TODO:Create Network Settings Page object
    
    def click_time_button(self):
        self.click_button("Time")
        #TODO:Create Time Settings Page object
        
    def click_mail_button(self):
        self.click_button("Mail")
        return MailSettingsPage(self.driver, self.wait)
    
    def click_active_directory_button(self):
        self.click_button("Active Directory")
        #TODO:Create Active Directory Settings Page object
        
    def click_button(self, link_text):
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text))).click()
        
        