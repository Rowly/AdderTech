'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.tests.base_infinity_regression_test import unittest
from root.nested.tests.base_infinity_regression_test import BaseInfinityRegressionTest
from root.nested.pages.home_page import HomePage

class RebootPageTest(BaseInfinityRegressionTest):
 
    def test_can_open_reboot_page(self):
        home_page = HomePage(self._driver, self._wait)
        reboot_page = home_page.open_reboot_page()
        self.assertEqual("Reboot", reboot_page.get_logo_text())
        self.assertEqual("Reboot", reboot_page.get_main_header_text())
     
    def test_can_reboot_unit(self):
        home_page = HomePage(self._driver, self._wait)
        reboot_page = home_page.open_reboot_page()
        reboot_page.click_reboot()
        reboot_page.wait_for_reboot_to_complete()
        self.assertEqual("Reboot", reboot_page.get_logo_text())
        self.assertEqual("Reboot", reboot_page.get_main_header_text())
    
    def test_can_factory_reset_unit(self):
        if self._ip is not "169.254.1.32" or self.ip is not "169.254.1.33":
            raise unittest.SkipTest("When not using link-local skip.")
        home_page = HomePage(self._driver, self._wait)
        system_config_page = home_page.open_system_configuration_page()
        system_config_page.set_unit_name("TEST TEST")
        system_config_page.update_config_form()
        self.assertEqual(system_config_page.get_unit_name(), "TEST TEST")
        reboot_page = home_page.open_reboot_page()
        reboot_page.set_factory_reset_state(True)
        reboot_page.click_reboot()
        self.assertEqual(reboot_page.get_reboot_message(), "The unit has been reset to factory settings. IP Address has been reset to factory default. The new IP address will be in the 169.254.*.* range.")
        reboot_page.wait_for_factory_reset_to_complete()
        system_config_page = home_page.open_system_configuration_page()
        self.assertEqual(system_config_page.get_unit_name(), "Name")
        