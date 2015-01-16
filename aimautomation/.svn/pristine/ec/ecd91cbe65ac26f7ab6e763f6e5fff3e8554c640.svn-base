'''
Created on 23 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimDashboardBackupsPageFunctionsTest(BaseAimRegressionTest):
    
    def test_disable_download_to_computer_option(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(False)
        self.assertFalse(self._page.get_download_to_computer_current_setting())
        self._page.click_save_settings()
        self.assertFalse(self._page.get_download_to_computer_current_setting())

    def test_enable_download_to_computer_option(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(True)
        self.assertTrue(self._page.get_download_to_computer_current_setting())
        self._page.click_save_settings()
        self.assertTrue(self._page.get_download_to_computer_current_setting())
    
    def test_settings_link_located_under_backup_header_opens_mail_settings_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_settings_link()
        self.assertEqual(self._page.get_text_of_mail_settings(), "Mail Enabled?")
    
    def test_can_change_backup_schedule_to_never(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.select_backup_never()
        self._page.click_save_settings()
        self.assertTrue(self._page.is_schedule_never_selected())

    def test_can_change_backup_schedule_to_hourly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.select_backup_hourly()
        self._page.click_save_settings()
        self.assertTrue(self._page.is_schedule_hourly_selected())

    def test_can_change_backup_schedule_to_daily(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.select_backup_daily()
        self._page.click_save_settings()
        self.assertTrue(self._page.is_schedule_daily_selected())

    def test_can_change_backup_schedule_to_weekly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.select_backup_weekly()
        self._page.click_save_settings()
        self.assertTrue(self._page.is_schedule_weekly_selected())
    
    def test_can_make_a_backup(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(False)
        pre_backups = self._page.get_list_of_backups()
        self._page.click_backup_now_button()
        self._page.wait_for_backing_up_database_message_to_be_removed()
        self.assertEqual(self._page.get_information_to_user_text(), "Backup completed successfully")
        post_backups = self._page.get_list_of_backups()
        backups = list(set(post_backups) - set(pre_backups))
        self.assertTrue(len(backups) == 1)
        self._page.select_backup_via_visible_text(backups[0])
        self._page.delete_backup(self._page.get_filename_from_element(backups[0]))
        self._page.wait_for_backup_deleted_message_to_be_removed()

    def test_can_restore_from_a_backup(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(False)
        pre_backups = self._page.get_list_of_backups()
        self._page.click_backup_now_button()
        self._page.wait_for_backing_up_database_message_to_be_removed()
        self.assertEqual(self._page.get_information_to_user_text(), "Backup completed successfully")
        post_backups = self._page.get_list_of_backups()
        backups = list(set(post_backups) - set(pre_backups))
        self.assertTrue(len(backups) == 1)
        self._page.select_backup_via_visible_text(backups[0])
        self._page.click_restore_backup()
        self._page.wait_for_restoring_backup_message_to_be_removed()
        self.assertEqual(self._page.get_information_to_user_text(), "Backup restored successfully")
        self._page.select_backup_via_visible_text(backups[0])
        self._page.delete_backup(self._page.get_filename_from_element(backups[0]))
        self._page.wait_for_backup_deleted_message_to_be_removed()
    
    def test_can_delete_a_backup(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(False)
        self._page.click_backup_now_button()
        self._page.wait_for_backing_up_database_message_to_be_removed()
        pre_backups = self._page.get_list_of_backups()
        self._page.select_backup_via_visible_text(pre_backups[1])
        self._page.delete_backup(self._page.get_filename_from_element(pre_backups[1]))
        self._page.wait_for_backup_deleted_message_to_be_removed()
        post_backups = self._page.get_list_of_backups()
        backups = list(set(post_backups) - set(pre_backups))
        self.assertTrue(len(backups) == 0)
        