'''
Created on 5 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimAddUserGroupPageFunctionsTest(BaseAimRegressionTest):

    name = "users new"

    def test_cannot_create_user_group_without_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "User Groups > Add User Group")
        self._page.click_save_ignore_warnings()
        msg = self._page.is_ajax_error_message_displayed_for_user_group()
        self.assertTrue(msg)

    def test_create_user_group_with_name_but_no_members_or_permissions(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        self.assertEqual(self._page.get_user_group_name(users[-1]), self.name)
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_allow_exclusive_no(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.select_user_group_exclusive_no()
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        src = self._page.get_user_group_connection_image_src(users[-1])
        self.assertEqual(src, self._silk_dir + "cross.png")
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_allow_exclusive_global(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.select_user_group_exclusive_global()
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        src = self._page.get_user_group_connection_image_src(users[-1])
        self.assertEqual(src, self._silk_dir + "inherit.png")
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_allow_exclusive_yes(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.select_user_group_exclusive_yes()
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        src = self._page.get_user_group_connection_image_src(users[-1])
        self.assertEqual(src, self._silk_dir + "tick.png")
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.add_member_to_user_group("user 0")
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_config(users[-1])
        self.assertTrue("user 0" in self._page.get_all_members_of_user_group())
        self._page.driver.back()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_channel_permission(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.add_channel_permission_to_user_group(self._channel_names[0])
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_config(users[-1])
        channels = self._page.get_all_channel_permissions_for_user_group()
        self.assertTrue(self._channel_names[0] in channels)
        self._page.driver.back()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_channel_group_permission(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.add_channel_group_permission_to_user_group("group 0")
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_config(users[-1])
        groups = self._page.get_all_channel_groups_for_user_group()
        self.assertTrue("group 0" in groups)
        self._page.driver.back()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_receiver_permission(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.show_receiver_permissions()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.remove_all_receivers_from_user_group()
        self._page.add_receiver_permission_to_user_group("RX2")
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_config(users[-1])
        self._page.show_receiver_permissions()
        self.assertTrue("RX2" in self._page.get_all_rxs_for_user_group())
        self._page.driver.back()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_user_group_with_receiver_group_permission(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_add_user_group_page()
        self._page.show_receiver_permissions()
        self._page.set_user_group_name_via_config_page(self.name)
        self._page.remove_all_receivers_from_user_group()
        self._page.add_receiver_group_permission_to_user_group("group 0")
        self._page.click_save()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_config(users[-1])
        self._page.show_receiver_permissions()
        groups = self._page.get_all_rx_groups_for_user_group()
        self.assertTrue("group 0" in groups)
        self._page.driver.back()
        users = self._page.get_list_of_user_groups()
        self._page.click_user_group_delete(users[-1])
        self._page.click_lightbox_delete_button()
