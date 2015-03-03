'''
Created on 6 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimAddChannelGroupPageFunctionsTest(BaseAimRegressionTest):

    def test_cannot_create_channel_group_without_a_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")
        visible = self._page.is_error_message_displayed_for_channel_group()
        self.assertFalse(visible)
        self._page.click_save_ignore_warnings()
        visible = self._page.is_error_message_displayed_for_channel_group()
        self.assertTrue(visible)

    def test_can_create_channel_group_with_one_channel(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_desc_via_config_page(desc)
        before_channels = self._page.get_all_not_permitted_channels_for_group()
        self._page.add_channel_to_channel_group(before_channels[0])
        self._page.click_save()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        added_channels = self._page.get_all_permitted_channels_in_group()
        for counter in range(0, len(added_channels)):
            self.assertTrue(added_channels[counter] in before_channels)
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_group_with_all_channels(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_desc_via_config_page(desc)
        before_channels = self._page.get_all_not_permitted_channels_for_group()
        self._page.add_all_channels_to_channel_group()
        self._page.click_save()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        added_channels = self._page.get_all_permitted_channels_in_group()
        for counter in range(0, len(added_channels)):
            self.assertTrue(added_channels[counter] in before_channels)
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_user_permissions_of_channel_group(self):
        name = "New Name"
        desc = "New Desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_desc_via_config_page(desc)
        self._page.add_user_to_channel_group_permission("anon")
        self._page.click_save()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        self.assertTrue("anon" in self._page.get_all_users_for_channel())
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_group_with_user_group(self):
        name = "New Name"
        desc = "New Desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_desc_via_config_page(desc)
        self._page.add_channel_group_to_user_group("group 0")
        self._page.click_save()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        self.assertTrue("group 0"
                        in self._page.get_all_user_groups_for_channel_group())
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()
