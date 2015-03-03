'''
Created on 23 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
#from root.nested.pages.login_page import LoginPage


class AimDashboardSettingsMailPageFunctionsTest(BaseAimRegressionTest):

    def test_server_input_fields_become_active_if_enabled_set_to_yes(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_mail_settings_button()
        self._page.click_mail_enable_yes()
        self.assertTrue(self._page.is_mail_smpt_domain_name_ip_active())
        self.assertTrue(self._page.is_mail_smpt_port_active())
        self.assertTrue(self._page.is_mail_username_active())
        self.assertTrue(self._page.is_mail_password_active())
        self.assertTrue(self._page.is_mail_alert_email_address_active())
        self._page.click_save()
        self.assertTrue(self._page.is_mail_smpt_domain_name_ip_active())
        self.assertTrue(self._page.is_mail_smpt_port_active())
        self.assertTrue(self._page.is_mail_username_active())
        self.assertTrue(self._page.is_mail_password_active())
        self.assertTrue(self._page.is_mail_alert_email_address_active())
        self._page.click_mail_enable_no()
        self._page.click_save()

    def test_server_input_fields_become_inactive_if_enable_set_to_no(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_mail_settings_button()
        self._page.click_mail_enable_yes()
        self._page.click_save()
        self._page.click_mail_enable_no()
        self.assertFalse(self._page.is_mail_smpt_domain_name_ip_active())
        self.assertFalse(self._page.is_mail_smpt_port_active())
        self.assertFalse(self._page.is_mail_username_active())
        self.assertFalse(self._page.is_mail_password_active())
        self.assertFalse(self._page.is_mail_alert_email_address_active())
        self._page.click_save()
        self.assertFalse(self._page.is_mail_smpt_domain_name_ip_active())
        self.assertFalse(self._page.is_mail_smpt_port_active())
        self.assertFalse(self._page.is_mail_username_active())
        self.assertFalse(self._page.is_mail_password_active())
        self.assertFalse(self._page.is_mail_alert_email_address_active())

#     def test_server_input_fields_become_active_if_enabled_set_to_yes_PO(self):
#         mail_page = self.get_page_under_test()
#         mail_page.click_mail_enable_yes()
#         self.assertTrue(mail_page.is_mail_smpt_domain_name_ip_active())
#         self.assertTrue(mail_page.is_mail_smpt_port_active())
#         self.assertTrue(mail_page.is_mail_username_active())
#         self.assertTrue(mail_page.is_mail_password_active())
#         self.assertTrue(mail_page.is_mail_alert_email_address_active())
#         mail_page.click_save_mail_settings()
#         self.assertTrue(mail_page.is_mail_smpt_domain_name_ip_active())
#         self.assertTrue(mail_page.is_mail_smpt_port_active())
#         self.assertTrue(mail_page.is_mail_username_active())
#         self.assertTrue(mail_page.is_mail_password_active())
#         self.assertTrue(mail_page.is_mail_alert_email_address_active())
#         mail_page.click_mail_enable_no()
#         mail_page.click_save_mail_settings()

#     def test_server_input_fields_become_inactive_if_enable_set_to_no_PO(self):
#         mail_page = self.get_page_under_test()
#         mail_page.click_mail_enable_yes()
#         mail_page.click_save_mail_settings()
#         mail_page.click_mail_enable_no()
#         self.assertFalse(mail_page.is_mail_smpt_domain_name_ip_active())
#         self.assertFrtFalse(mail_page.is_mail_password_active())
#         self.assertFalse(mail_page.is_mail_alert_email_address_active())
#         mail_page.click_save_mail_settings()
#         self.assertFalse(mail_page.is_mail_smpt_domain_name_ip_active())
#         self.assertFalse(mail_page.is_mail_smpt_port_active())
#         self.assertFalse(mail_page.is_mail_username_active())
#         self.assertFalse(mail_page.is_mail_password_active())
#         self.assertFalse(mail_page.is_mail_alert_email_address_active())

#     def get_page_under_test(self):
#         login_page = LoginPage(self._driver, self._wait)
#         dashboard_page = login_page.login()
#         settings_page = dashboard_page.click_settings_link()
#         return settings_page.click_mail_button()
