'''
Created on 30 Apr 2013

@author: Mark.rowlands
'''
import unittest
from root.nested.services.parameters import parameter_singleton
#from ..services.selenium_start_service import SeleniumStartService
from root.nested.pages.base_page import BasePage
#from selenium.webdriver.support.wait import WebDriverWait


class BaseAimRegressionTest(unittest.TestCase):

    def setUp(self):
        parameter_singleton["version"] = "v4.0.32519"
        parameter_singleton["url"] = "http://10.10.10.10"
        parameter_singleton["local_only"] = True

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

        self._channel_names = ["Channel TX", "Channel TX2b", "Channel TX20"]
        self._tx_names = [name.replace("Channel ", "")
                          for name in self._channel_names]
#         self._rx_names = ["RX", "RX2", "RX20"]
        self._rx_names = ["RX2", "RX20"]

        self._silk_dir = self._baseurl + "/admin/images/silk_icons/"
        self._device_status_imgs = [self._silk_dir + "tick.png",
                                    self._silk_dir + "tick_cross.png",
                                    self._silk_dir + "cross_tick.png"]

    def tearDown(self):
        try:
            self._driver.quit()
        except Exception:
            pass

    def make_backup_url(self, url):
        backup = url.split(".")
        backup[3] = backup[3].replace("/", "")
        return ".".join((backup[0],
                         backup[1],
                         backup[2],
                         str(int(backup[3]) + 1) + "/"))

    def identify_skip_check(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if ((int(split_version[0]) > 3)
        or (int(split_version[0]) == 3 and (int(split_version[1]) >= 2))):
            raise unittest.SkipTest("Identify changed in v3.2")

    def colour_depth_skip_check(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if ((int(split_version[0]) > 3)
        or (int(split_version[0]) == 3 and (int(split_version[1]) >= 3))):
            raise unittest.SkipTest("Colour depth changed in v3.3")

    def gateway_skip_check(self):
        self.identify_skip_check()

    def old_ntp_skip_check(self):
        self.identify_skip_check()

    def new_ntp_skip_check(self):
        self.snmp_skip_check()

    def snmp_skip_check(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) <= 3 and int(split_version[1]) < 2:
            raise unittest.SkipTest("SNMP added in v3.2")
