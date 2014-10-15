'''
Created on 30 Apr 2013

@author: Mark.rowlands
'''
import unittest
from root.nested.services.parameters import parameter_singleton
from selenium.webdriver.support.wait import WebDriverWait  # @UnusedImport
from root.nested.services.selenium_start_service import SeleniumStartService  # @UnusedImport
from root.nested.pages.base_page import BasePage


class BaseAimRegressionTest(unittest.TestCase):

    def setUp(self):
        parameter_singleton["version"] = "v3.3.30400"
        parameter_singleton["suite"] = "short"
        parameter_singleton["url"] = "http://10.10.10.10"
        
        self._page = BasePage()
        self._driver = self._page.get_driver()
        self._wait = self._page.get_wait()
        
        self._baseurl = self._page.get_baseurl()
        self._backup_url = self.make_backup_url(self._baseurl)
        '''
        Here ready for change to Page Object Model
        Remember to delete the webdriver instantiation from BasePage()
        self._driver = SeleniumStartService().start_driver()
        self._wait = WebDriverWait(self._driver, 15)
        
        self._baseurl = parameter_singleton["url"]
        self._backup_url = self.make_backup_url(self._baseurl)
        self._driver.get(self._baseurl)
        '''
        #Global Test Variables
        self._version = parameter_singleton["version"]
        if parameter_singleton["suite"] == "long":
            self._test_all = True
        elif parameter_singleton["suite"] == "short":
            self._test_all = False
        
        self._channel_names = ["Channel TX2s", "Channel TX2b", "Channel TX2v"]

        self._invalid_device_ips = []

        self._device_status_imgs = [self._baseurl + "/admin/images/silk_icons/tick.png", 
                                    self._baseurl + "/admin/images/silk_icons/tick_cross.png",
                                    self._baseurl + "/admin/images/silk_icons/cross_tick.png"]

    def tearDown(self):
        try:
            self._driver.quit()
        except Exception:
            pass
    
    def make_backup_url(self, url):
        backup = url.split(".")
        backup[3] = backup[3].replace("/","")
        return ".".join((backup[0], backup[1], backup[2], str(int(backup[3])+1)+"/"))
