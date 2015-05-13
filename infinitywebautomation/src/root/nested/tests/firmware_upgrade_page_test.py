'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.home_page import HomePage
from root.nested.tests.base_infinity_regression_test import \
    BaseInfinityRegressionTest


class FirmwareUpgradePageTest(BaseInfinityRegressionTest):

    def test_can_open_firmware_upgrade_page(self):
        home_page = HomePage(self._driver, self._wait)
        firmware_upgrade_page = home_page.open_firmware_upgrade_page()
        logo = firmware_upgrade_page.get_logo_text()
        head = firmware_upgrade_page.get_main_header_text()
        self.assertEqual("Firmware Upgrade", logo)
        self.assertEqual("Firmware Upgrade", head)
