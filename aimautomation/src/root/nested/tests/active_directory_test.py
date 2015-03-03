'''
Created on 27 Feb 2015

@author: Mark
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class ActiveDirectoryTest(BaseAimRegressionTest):

    def test_can_import_users(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.check_active_directory_enabled()
        self._page.open_users_tab()
        # testing adding users
        pre_users = self._page.get_list_of_users()
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "user_test" in name:
                self._page.select_ad_import(cells[4])
                break
        self._page.click_save_and_sync()
        self._page.open_users_tab()
        post_users = self._page.get_list_of_users()
        self.assertNotEqual(len(pre_users), len(post_users))
        # testing deleting users
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "user_test" in name:
                self._page.select_ad_import(cells[4])
                break
        self._page.click_save_and_sync()
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self.assertEqual(len(pre_users), len(users))

    def test_can_import_groups(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.check_active_directory_enabled()
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        # testing adding user groups
        pre_groups = self._page.get_list_of_user_groups()
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "group_test" in name:
                self._page.select_ad_import(cells[5])
                break
        self._page.click_save_and_sync()
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        post_groups = self._page.get_list_of_user_groups()
        self.assertNotEqual(len(pre_groups), len(post_groups))
        # testing deleting user groups
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "group_test" in name:
                self._page.select_ad_import(cells[5])
                break
        self._page.click_save_and_sync()
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        groups = self._page.get_list_of_user_groups()
        self.assertEqual(len(pre_groups), len(groups))

    def test_assign_channel_permission_to_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.check_active_directory_enabled()
        self._page.open_users_tab()
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "user_test" in name:
                self._page.select_ad_import(cells[4])
                break
        self._page.click_save_and_sync()
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        for user in users:
            if self._page.get_user_username(user) == "testuser1_1":
                self._page.click_user_config(user)
                break
        channels = self._page.get_all_channel_permissions_for_user()
        self.assertTrue(len(channels) == 0)
        self._page.add_channel_permission_to_user(self._channel_names[0])
        self._page.click_save()
        users = self._page.get_list_of_users()
        users = self._page.get_list_of_users()
        for user in users:
            if self._page.get_user_username(user) == "testuser1_1":
                self._page.click_user_config(user)
                break
        self.assertTrue(self._channel_names[0]
                        in self._page.get_all_channel_permissions_for_user())
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "user_test" in name:
                self._page.select_ad_import(cells[4])
                break
        self._page.click_save_and_sync()

    def test_assign_channel_permission_to_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.check_active_directory_enabled()
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        # testing adding group groups
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "group_test" in name:
                self._page.select_ad_import(cells[5])
                break
        self._page.click_save_and_sync()
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        groups = self._page.get_list_of_user_groups()
        for group in groups:
            if self._page.get_user_group_name(group) == "Test1 Group1":
                self._page.click_user_group_config(group)
                break
        channels = self._page.get_all_channel_permissions_for_user_group()
        self.assertTrue(len(channels) == 0)
        self._page.add_channel_permission_to_user_group(self._channel_names[0])
        self._page.click_save()
        groups = self._page.get_list_of_user_groups()
        for group in groups:
            if self._page.get_user_group_name(group) == "Test1 Group1":
                self._page.click_user_group_config(group)
                break
        permissions = self._page.get_all_channel_permissions_for_user_group()
        self.assertTrue(self._channel_names[0] in permissions)
        self._page.open_active_directory_page()
        self._page.click_rescan_active_directory()
        rows = self._page.get_active_directory_content()
        for row in rows[1:-1]:
            cells = self._page.get_active_directory_table_cells(row)
            name = cells[0].text
            if "group_test" in name:
                self._page.select_ad_import(cells[5])
                break
        self._page.click_save_and_sync()

    """
    Utils
    """
    def check_active_directory_enabled(self):
        self._page.click_dashboard_settings_link()
        self._page.click_active_directory_settings_button()
        if self._page.get_active_directory_enable_state():
            pass
        else:
            self._page.click_active_directory_enable_yes()
            self._page.enter_active_directory_suffix()
            self._page.enter_active_directory_base_dn()
            self._page.enter_active_directory_domain()
            self._page.enter_active_directory_username()
            self._page.enter_active_directory_password()
            self._page.click_save()
