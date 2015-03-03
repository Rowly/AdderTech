'''
Created on 23 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimDashboardSettingsActiveDirectoryPageFunctionsTest(BaseAimRegressionTest):

    def test_server_input_fields_become_active_if_enabled_set_to_yes(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_active_directory_settings_button()
        self._page.click_active_directory_enable_yes()
        self.assertTrue(self._page.is_active_directory_account_suffix_active())
        self.assertTrue(self._page.is_active_directory_base_dn_active())
        self.assertTrue(self._page.is_active_directory_domain_controller_active())
        self.assertTrue(self._page.is_active_directory_username_active())
        self.assertTrue(self._page.is_active_directory_password_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_never_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_hourly_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_daily_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_weekly_active())
        self._page.click_save()
        self.assertTrue(self._page.is_active_directory_account_suffix_active())
        self.assertTrue(self._page.is_active_directory_base_dn_active())
        self.assertTrue(self._page.is_active_directory_domain_controller_active())
        self.assertTrue(self._page.is_active_directory_username_active())
        self.assertTrue(self._page.is_active_directory_password_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_never_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_hourly_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_daily_active())
        self.assertTrue(self._page.is_active_directory_sync_schedule_weekly_active())
        self._page.click_active_directory_enable_no()
        self._page.click_save()

    def test_server_input_fields_become_inactive_if_enabled_set_to_no(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_active_directory_settings_button()
        self._page.click_active_directory_enable_yes()
        self._page.click_save()
        self._page.click_active_directory_enable_no()
        self.assertFalse(self._page.is_active_directory_account_suffix_active())
        self.assertFalse(self._page.is_active_directory_base_dn_active())
        self.assertFalse(self._page.is_active_directory_domain_controller_active())
        self.assertFalse(self._page.is_active_directory_username_active())
        self.assertFalse(self._page.is_active_directory_password_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_never_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_hourly_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_daily_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_weekly_active())
        self._page.click_save()
        self.assertFalse(self._page.is_active_directory_account_suffix_active())
        self.assertFalse(self._page.is_active_directory_base_dn_active())
        self.assertFalse(self._page.is_active_directory_domain_controller_active())
        self.assertFalse(self._page.is_active_directory_username_active())
        self.assertFalse(self._page.is_active_directory_password_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_never_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_hourly_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_daily_active())
        self.assertFalse(self._page.is_active_directory_sync_schedule_weekly_active())
