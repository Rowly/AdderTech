'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.home_page import HomePage
from root.nested.tests.base_infinity_regression_test import \
    BaseInfinityRegressionTest


class SecurityPageTest(BaseInfinityRegressionTest):

    def test_can_open_security_page(self):
        home_page = HomePage(self._driver, self._wait)
        security_page = home_page.open_security_page()
        self.assertEqual("Security", security_page.get_logo_text())
        self.assertEqual("Security", security_page.get_main_header_text())

    def test_can_change_receiver_encryption(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        security_page = home_page.open_security_page()
        self.assertTrue(security_page.get_encryption_chosen_by_transmitter_unit_state())
        self.assertFalse(security_page.get_encryption_always_on_state())
        security_page.set_encryption_always_on_state(True)
        security_page.update_config_form()
        self.assertFalse(security_page.get_encryption_chosen_by_transmitter_unit_state())
        self.assertTrue(security_page.get_encryption_always_on_state())
        security_page.set_encryption_chosen_by_transmitter_unit_state(True)
        security_page.update_config_form()
        self.assertTrue(security_page.get_encryption_chosen_by_transmitter_unit_state())
        self.assertFalse(security_page.get_encryption_always_on_state())

    def test_can_change_transmitter_encryption(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        security_page = home_page.open_security_page()
        self.assertTrue(security_page.get_control_encryption_prefer_off_state())
        self.assertFalse(security_page.get_control_encryption_always_off_state())
        self.assertFalse(security_page.get_control_encryption_always_on_state())
        security_page.set_control_encryption_always_off_state(True)
        security_page.update_config_form()
        self.assertFalse(security_page.get_control_encryption_prefer_off_state())
        self.assertTrue(security_page.get_control_encryption_always_off_state())
        self.assertFalse(security_page.get_control_encryption_always_on_state())
        security_page.set_control_encryption_always_on_state(True)
        security_page.update_config_form()
        self.assertFalse(security_page.get_control_encryption_prefer_off_state())
        self.assertFalse(security_page.get_control_encryption_always_off_state())
        self.assertTrue(security_page.get_control_encryption_always_on_state())
        security_page.set_control_encryption_prefer_off_state(True)
        security_page.update_config_form()

    def test_change_password(self):
        home_page = HomePage(self._driver, self._wait)
        security_page = home_page.open_security_page()
        self.assertFalse(security_page.get_secure_web_pages_with_password_state())
        self.assertFalse(security_page.get_change_password_state())
        self.assertFalse(security_page.get_old_password_enabled_state())
        self.assertFalse(security_page.get_password_enabled_state())
        self.assertFalse(security_page.get_confirm_password_enabled_state())
        security_page.set_secure_web_pages_with_password_state(True)
        security_page.set_change_password_state(True)
        self.assertTrue(security_page.get_secure_web_pages_with_password_state())
        self.assertTrue(security_page.get_change_password_state())
        self.assertTrue(security_page.get_old_password_enabled_state())
        self.assertTrue(security_page.get_password_enabled_state())
        self.assertTrue(security_page.get_confirm_password_enabled_state())
