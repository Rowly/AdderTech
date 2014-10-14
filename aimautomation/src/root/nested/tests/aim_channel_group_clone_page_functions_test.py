'''
Created on 6 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimChannelGroupClonePageFunctionsTest(BaseAimRegressionTest):

    def test_can_clone_existing_change_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        self._page.click_save()
        self._page.confirm_no_longer_on_clone_channel_group_page()
        channels = self._page.get_list_of_channels()
        self.assertEqual(self._page.get_channel_group_name(channels[-1])[-6:], "(Copy)")
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_channel_group_name(self):
        name = "New Name"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        self._page.set_channel_group_name_via_config_page(name)
        self._page.click_save()
        self._page.confirm_no_longer_on_clone_channel_group_page()
        channels = self._page.get_list_of_channels()
        self.assertEqual(self._page.get_channel_group_name(channels[-1]), name)
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_channel_group_desc(self):
        desc = "New Desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        self._page.set_channel_group_description_via_config_page(desc)
        self._page.click_save()
        self._page.confirm_no_longer_on_clone_channel_group_page()
        channels = self._page.get_list_of_channels()
        self.assertEqual(self._page.get_channel_group_description(channels[-1]), desc)
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()

    def test_can_add_one_member_to_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        channel_names = self._page.get_list_of_non_member_channels_for_group()
        before_added_channel_names = []
        for channel in channel_names:
            before_added_channel_names.append(channel.text)
        self._page.add_channel_to_channel_group(before_added_channel_names[0])
        self._page.click_save()
        self._page.confirm_no_longer_on_clone_channel_group_page()
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

    def test_can_add_all_members_to_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        before_added_channels = self._page.get_list_of_non_member_channels_for_group()
        before_added_channel_names = []
        for channel in before_added_channels:
            before_added_channel_names.append(channel.text)
        self._page.add_all_channels_to_channel_group()
        self._page.click_save()
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
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        self._page.add_user_to_channel_group_permission("anon")
        self._page.click_save()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        self.assertTrue(self._page.check_user_has_channel_group_permission("anon"))
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_clone_channel_group_with_user_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_clone(channels[-1])
        self._page.add_channel_group_to_user_group()
        self._page.click_save()
        self._page.confirm_no_longer_on_add_channel_page()
        channels = self._page.get_list_of_channels()
        self._page.click_configure_channel_group(channels[-1])
        self.assertTrue(self._page.check_channel_group_in_user_group())
#         self._page.click_cancel() #cancel button is missing from config group page!
        self._page.click_view_channel_groups_subtab_link()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_group_delete(channels[-1])
        self._page.click_lightbox_delete_button()