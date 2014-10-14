'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.tests.base_infinity_regression_test import BaseInfinityRegressionTest
from root.nested.pages.home_page import HomePage
from root.nested.services.parameters import parameter_singleton

class AboutPageTest(BaseInfinityRegressionTest):

    def test_can_open_about_page(self):
        home_page = HomePage(self._driver, self._wait)
        about_page = home_page.open_about_page()
        self.assertEqual("About", about_page.get_logo_text())
        self.assertEqual("About", about_page.get_main_header_text())
     
    def test_mac_addresses_are_hex_numbers(self):
        home_page = HomePage(self._driver, self._wait)
        about_page = home_page.open_about_page()
        for mac in about_page.get_macs():
            self.assertRegex(mac, "([0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2})")
         
    def test_version_numbers_are_correct_for_unit(self):
        home_page = HomePage(self._driver, self._wait)
        about_page = home_page.open_about_page()
        self.assertTrue(about_page.get_main_system_version_number() in self._version)
        self.assertTrue(about_page.get_backup_system_version_number() in self._version)
        self.assertTrue(about_page.get_boot_system_version_number() in self._version)
     
    def test_option_switches_are_correct_for_unit(self):
        home_page = HomePage(self._driver, self._wait)
        about_page = home_page.open_about_page()
        self.assertRegex(about_page.get_option_switch_1_text(), "(up)")
        self.assertRegex(about_page.get_option_switch_2_text(), "(up)")
 
    def test_board_revision_correct_for_unit(self):
        tx2 = ["0", "1"]
        tx2s = ["3"]
        tx2b = ["5", "6"]
        tx2v = ["5", "6"]
        rx2 = ["0", "1", "3"]
        rx2s = ["2"]
        home_page = HomePage(self._driver, self._wait)
        about_page = home_page.open_about_page()
        if parameter_singleton["device"] == "RX2s":
            self.assertTrue(any (device in about_page.get_board_revision() for device in rx2s))
        elif parameter_singleton["device"] == "TX2s":
            self.assertTrue(any (device in about_page.get_board_revision() for device in tx2s))
        elif parameter_singleton["device"] == "TX2b": 
            self.assertTrue(any (device in about_page.get_board_revision() for device in tx2b))
        elif parameter_singleton["device"] == "TX2v": 
            self.assertTrue(any (device in about_page.get_board_revision() for device in tx2v))
        elif parameter_singleton["device"] == "TX2":
            self.assertTrue(any (device in about_page.get_board_revision() for device in tx2))
        elif parameter_singleton["device"] == "RX2":
            self.assertTrue(any (device in about_page.get_board_revision() for device in rx2))
          
    def test_system_type_correct_for_unit(self):
        home_page = HomePage(self._driver, self._wait)
        about_page = home_page.open_about_page()
        self.assertEqual(about_page.get_system_type(), self._device)