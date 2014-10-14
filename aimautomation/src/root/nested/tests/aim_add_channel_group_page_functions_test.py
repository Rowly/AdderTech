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
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups > Add Channel Group")
        self.assertFalse(self._page.is_ajax_error_message_displayed_for_channel_group())
        self._page.click_save()
        self.assertTrue(self._page.is_ajax_error_message_displayed_for_channel_group())
    
    def test_can_create_channel_group_with_one_channel(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_description_via_config_page(desc)
        before_added_channels = self._page.get_list_of_non_member_channels_for_group()
        before_added_channel_names = []
        for channel in before_added_channels:
            before_added_channel_names.append(channel.text)
        self._page.add_channel_to_channel_group(before_added_channel_names[0])
        self._page.click_save()
        self._page.check_for_error_message("configure_channel_group_ajax_message")
        self._page.confirm_no_longer_on_configure_channel_group_page()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        added_channels = self._page.get_list_of_member_channels_in_group()
        added_channel_names = []
        for added_channel in added_channels:
            added_channel_names.append(added_channel.text)
#         self._page.click_cancel() #cancel button is missing from config group page!
        for counter in range(0, len(added_channel_names)):
            self.assertTrue(added_channel_names[counter] in before_added_channel_names)
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
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_description_via_config_page(desc)
        before_added_channels = self._page.get_list_of_non_member_channels_for_group()
        before_added_channel_names = []
        for channel in before_added_channels:
            before_added_channel_names.append(channel.text)
        self._page.add_all_channels_to_channel_group()
        self._page.click_save()
        self._page.check_for_error_message("configure_channel_group_ajax_message")
        self._page.confirm_no_longer_on_configure_channel_group_page()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        added_channels = self._page.get_list_of_member_channels_in_group()
        added_channel_names = []
        for added_channel in added_channels:
            added_channel_names.append(added_channel.text)
#         self._page.click_cancel() #cancel button is missing from config group page!
        for counter in range(0, len(added_channel_names)):
            self.assertTrue(added_channel_names[counter] in before_added_channel_names)
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
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_description_via_config_page(desc)
        self._page.add_user_to_channel_group_permission("anon")
        self._page.click_save()
        self._page.check_for_error_message("configure_channel_group_ajax_message")
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        self.assertTrue(self._page.check_user_has_channel_group_permission("anon"))
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
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups > Add Channel Group")
        self._page.set_channel_group_name_via_config_page(name)
        self._page.set_channel_group_description_via_config_page(desc)
        self._page.add_channel_group_to_user_group()
        self._page.click_save()
        self._page.check_for_error_message("configure_channel_group_ajax_message")
        self._page.confirm_no_longer_on_add_channel_page()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        self.assertTrue(self._page.check_channel_group_in_user_group())
#         self._page.click_cancel() #cancel button is missing from config group page!
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()