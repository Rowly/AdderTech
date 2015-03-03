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
        self._page.click_save_settings_ignore_warnings()
        self.assertFalse(self._page.get_download_to_computer_current_setting())

    def test_enable_download_to_computer_option(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(True)
        self.assertTrue(self._page.get_download_to_computer_current_setting())
        self._page.click_save_settings_ignore_warnings()
        self.assertTrue(self._page.get_download_to_computer_current_setting())

    def test_settings_link_opens_mail_settings_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_mail_settings_link()
        text = self._page.get_text_of_mail_settings()
        self.assertEqual(text, "Mail Enabled?")

    def test_can_change_backup_schedule(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self.assertTrue(self._page.get_schedule_setting_state("daily"))
        self._page.select_backup_never()
        self._page.click_save_settings_ignore_warnings()
        self.assertTrue(self._page.get_schedule_setting_state("never"))
        self._page.select_backup_hourly()
        self._page.click_save_settings_ignore_warnings()
        self.assertTrue(self._page.get_schedule_setting_state("hourly"))
        self._page.select_backup_weekly()
        self._page.click_save_settings_ignore_warnings()
        self.assertTrue(self._page.get_schedule_setting_state("weekly"))
        self._page.select_backup_daily()
        self._page.click_save_settings_ignore_warnings()
        self.assertTrue(self._page.get_schedule_setting_state("daily"))

    def test_can_make_a_backup(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_download_to_computer(False)
        pre_backups = self._page.get_list_of_backups()
        self._page.click_backup_now_button()
        self._page.wait_for_backing_up_database_message_to_be_removed()
        text = self._page.get_information_to_user_text()
        self.assertEqual(text, "Backup completed successfully")
        post_backups = self._page.get_list_of_backups()
        backups = list(set(post_backups) - set(pre_backups))
        self.assertTrue(len(backups) == 1)
        self._page.select_backup_via_visible_text(backups[0])
        file_name = self._page.get_filename_from_element(backups[0])
        self._page.delete_backup(file_name)
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
        text = self._page.get_information_to_user_text()
        self.assertEqual(text, "Backup completed successfully")
        post_backups = self._page.get_list_of_backups()
        backups = list(set(post_backups) - set(pre_backups))
        self.assertTrue(len(backups) == 1)
        self._page.select_backup_via_visible_text(backups[0])
        self._page.click_restore_backup()
        self._page.wait_for_restoring_backup_message_to_be_removed()
        text = self._page.get_information_to_user_text()
        self.assertEqual(text, "Backup restored successfully")
        self._page.select_backup_via_visible_text(backups[0])
        file_name = self._page.get_filename_from_element(backups[0])
        self._page.delete_backup(file_name)
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
        file_name = self._page.get_filename_from_element(pre_backups[1])
        self._page.delete_backup(file_name)
        self._page.wait_for_backup_deleted_message_to_be_removed()
        post_backups = self._page.get_list_of_backups()
        backups = list(set(post_backups) - set(pre_backups))
        self.assertTrue(len(backups) == 0)
