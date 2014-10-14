'''
Created on 9 Jul 2014

@author: Mark
'''
from root.nested.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from root.nested.pages.settings_page import SettingsPage

class DashboardPage(BasePage):
    
    def click_settings_link(self):
        self.click_link((By.LINK_TEXT, "Settings"))
        return SettingsPage(self.driver, self.wait)

    def click_backups_link(self):
        self.click_link((By.LINK_TEXT, "Backups"))
        #return a backups page object

    def click_updates_link(self):
        self.click_link((By.LINK_TEXT, "Updates"))
        #return an updates page object

    def click_active_connections_link(self):
        self.click_link((By.LINK_TEXT, "Active Connections"))
        #return a connection log page object
    
    def click_connection_log_link(self):
        self.click_link((By.LINK_TEXT, "Connection Log"))
        #return a connection log page object
    
    def click_event_log_link(self):
        self.click_link((By.LINK_TEXT, "Event Log"))
        #return an event log page object
    
    def click_view_all_active_connections(self):
        self.click_link((By.LINK_TEXT, "View all Active Connections"))
        #return a connection log page object
    
    def click_view_all_events(self):
        self.click_link((By.LINK_TEXT, "View all Events"))
        #return an event log page object
    
    def click_view_all_channels(self):
        self.click_link((By.LINK_TEXT, "View all Channels"))
        #return a channels page object
    
    def click_view_all_channel_changes(self):
        self.click_link((By.LINK_TEXT, "View all Channel Changes"))
        #return a connection log page object
        
    def click_view_all_OSD_logins(self):
        self.click_link((By.LINK_TEXT, "View all OSD Logins"))
        #return an event log page object
    
    def click_view_all_users(self):
        self.click_link((By.LINK_TEXT, "View all Users"))
        #return a users page object
    
    def click_view_all_receivers(self):
        self.click_link((By.LINK_TEXT, "View all Receivers"))
        #return a devices page object
    
    def click_view_all_transmitters(self):
        self.click_link((By.LINK_TEXT, "View all Transmitters"))
        #return a devices page object
        
    def click_link(self, locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()