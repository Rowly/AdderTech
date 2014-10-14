'''
Created on 9 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimDashboardSettingsGeneralPageFunctionsTest(BaseAimRegressionTest):
    
    def test_can_change_osd_timeout(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        labels = self._page.get_osd_timeout_options()
        for label in labels:
            self._page.select_osd_timeout_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_general_settings_button()
            self.assertEqual(self._page.get_current_osd_timeout_selection_text(), label)
        self._page.select_osd_timeout_by_label("15 minutes")
        self._page.click_save()

    def test_can_change_admin_timeout(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        labels = self._page.get_admin_timeout_options()
        for label in labels:
            self._page.select_admin_timeout_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_general_settings_button()
            self.assertEqual(self._page.get_current_admin_timeout_selection_text(), label)
        self._page.select_admin_timeout_by_label("15 minutes")
        self._page.click_save()

    def test_can_change_anonymous_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        labels = self._page.get_anonymous_user_options()
        for label in labels:
            self._page.select_anonymous_user_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_general_settings_button()
            self.assertEqual(self._page.get_current_anonymous_user_selection_text(), label)
        self._page.select_anonymous_user_by_label("anon")
        self._page.click_save()
    
    def test_can_toggle_hide_dormant_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        current_setting = self._page.get_hide_dormant_devices_setting()
        self._page.toggle_hide_dormant_devices()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        new_setting = self._page.get_hide_dormant_devices_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_hide_dormant_devices()
        self._page.click_save()

    def test_can_toggle_grant_all_users_exclusive_access(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        current_setting = self._page.get_grant_all_users_exclusive_access_setting()
        self._page.toggle_all_users_exclusive_access()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        new_setting = self._page.get_grant_all_users_exclusive_access_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_all_users_exclusive_access()
        self._page.click_save()

    def test_can_toggle_allowed_connections(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        options = self._page.get_allow_connection_mode_options()
        counter = 0
        for counter in range(counter, len(options)):
            options = self._page.get_allow_connection_mode_options()
            options[counter].click()
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_general_settings_button()
            self.assertTrue(self._page.get_selected_allow_connection_mode(counter))
        options = self._page.get_allow_connection_mode_options()
        options[-1].click()
        self._page.click_save()

#     def test_can_toggle_initial_streaming_mode(self):
#         self._page.open_AIM_homepage_on_base_url()
#         self._page.login_as("admin", "password", False)
#         self._page.click_dashboard_settings_link()
#         self._page.click_general_settings_button()
#         current_setting = self._page.get_initial_streaming_mode_setting()
#         self._page.toggle_initial_streaming_mode()
#         self._page.click_save()
#         self._page.open_dashboard_tab()
#         self._page.click_dashboard_settings_link()
#         self._page.click_general_settings_button()
#         new_setting = self._page.get_initial_streaming_mode_setting()
#         self.assertNotEqual(current_setting, new_setting)
#         self._page.toggle_initial_streaming_mode()
#         self._page.click_save()
    
    def test_can_change_rows_per_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        labels = self._page.get_rows_per_page_options()
        for label in labels:
            self._page.select_rows_per_page_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_general_settings_button()
            self.assertEqual(self._page.get_current_rows_per_page_selection_text(), label)
        self._page.select_rows_per_page_by_label("20")
        self._page.click_save()
    
    def test_can_toggle_api_login_required(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        current_setting = self._page.get_api_login_required_setting()
        self._page.toggle_api_login_required()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        new_setting = self._page.get_api_login_required_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_api_login_required()
        self._page.click_save()
    
    def test_can_change_api_anonymous_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_general_settings_button()
        labels = self._page.get_api_anonymous_user_options()
        for label in labels:
            self._page.select_api_anonymous_user_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_general_settings_button()
            self.assertEqual(self._page.get_current_api_anonymous_user_selection_text(), label)
        self._page.select_api_anonymous_user_by_label("api_anon")
        self._page.click_save()