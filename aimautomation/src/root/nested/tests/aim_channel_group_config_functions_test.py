'''
Created on 5 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimChannelGroupConfigFunctionsTest(BaseAimRegressionTest):

    def test_change_channel_group_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        for counter in range(0, len(self._page.get_list_of_channel_groups())):
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Channel Group")
            name = self._page.get_channel_group_name_from_config_page()
            self._page.set_channel_group_name_via_config_page(name + " edit")
            self._page.click_save()
            groups = self._page.get_list_of_channel_groups()
            new_name = self._page.get_channel_group_name(groups[counter])
            self.assertEqual(new_name, name + " edit")
            self._page.click_configure_channel_group(groups[counter])
            self._page.set_channel_group_name_via_config_page(name)
            self._page.click_save()

    def test_can_change_channel_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        for counter in range(0, len(self._page.get_list_of_channels())):
            groups = self._page.get_list_of_channels()
            self._page.click_configure_channel_group(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Channel Group")
            desc = self._page.get_channel_group_description_from_config_page()
            self._page.set_channel_group_desc_via_config_page(desc + " edit")
            self._page.click_save()
            groups = self._page.get_list_of_channel_groups()
            new_desc = self._page.get_channel_group_desc(groups[counter])
            self.assertEqual(new_desc, desc + " edit")
            self._page.click_configure_channel_group(groups[counter])
            self._page.set_channel_group_desc_via_config_page(desc)
            self._page.click_save()

    def test_can_add_channel_to_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        for counter in range(0, len(self._page.get_list_of_channel_groups())):
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Channel Group")
            channels = self._page.get_all_channels_for_channel_group()
            self.assertTrue(len(channels) == 0)
            self._page.add_channel_to_channel_group(self._channel_names[0])
            self._page.click_save()
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            channels = self._page.get_all_channels_for_channel_group()
            self.assertTrue(self._channel_names[0] in channels)
            self._page.remove_all_channels_from_group()
            self._page.click_save()

    def test_can_change_user_permissions_of_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        for counter in range(0, len(self._page.get_list_of_channel_groups())):
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Channel Group")
            channels = self._page.get_all_users_for_channel_group()
            self.assertTrue(len(channels) == 0)
            self._page.add_user_to_channel_group_permission("anon")
            self._page.click_save()
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            channels = self._page.get_all_users_for_channel_group()
            self.assertTrue("anon" in channels)
            self._page.remove_user_from_channel_group_permission("anon")
            self._page.click_save()

    def test_can_change_user_group_of_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        for counter in range(0, len(self._page.get_list_of_channel_groups())):
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Channel Group")
            channels = self._page.get_all_user_groups_for_channel_group()
            self.assertTrue(len(channels) == 0)
            self._page.add_channel_group_to_user_group("group 0")
            self._page.click_save()
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            channels = self._page.get_all_user_groups_for_channel_group()
            self.assertTrue("group 0" in channels)
            self._page.remove_channel_group_from_user_group("group 0")
            self._page.click_save()
