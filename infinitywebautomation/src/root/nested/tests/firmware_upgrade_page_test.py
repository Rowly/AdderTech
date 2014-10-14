'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.tests.base_infinity_regression_test import BaseInfinityRegressionTest
from root.nested.pages.home_page import HomePage

class FirmwareUpgradePageTest(BaseInfinityRegressionTest):
    
    def test_can_open_firmware_upgrade_page(self):
        home_page = HomePage(self._driver, self._wait)
        firmware_upgrade_page = home_page.open_firmware_upgrade_page()
        self.assertEqual("Firmware Upgrade", firmware_upgrade_page.get_logo_text())
        self.assertEqual("Firmware Upgrade", firmware_upgrade_page.get_main_header_text())