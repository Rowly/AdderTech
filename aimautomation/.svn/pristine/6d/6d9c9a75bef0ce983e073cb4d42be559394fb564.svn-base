'''
Created on 5 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage

class AimChannelGroupConfigFunctionsTest(BaseAimRegressionTest):

    def test_change_channel_group_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for channel in channels:
                index = channels.index(channel)
                link_text = self._page.get_channel_group_linktext(channel)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Channel Groups > Configure Channel Group")
                name = page.get_channel_group_name_from_config_page()
                page.set_channel_group_name_via_config_page(name + " edit")
                page.click_save()
                new_channel = page.get_list_of_channels()[index]
                new_name = page.get_channel_group_name(new_channel)
                self.assertEqual(new_name, name + " edit")
                page.driver.get(link_text)
                page.set_channel_group_name_via_config_page(name)
                page.click_save()
        finally:
            page.driver.quit()
            
    def test_can_change_channel_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for channel in channels:
                index = channels.index(channel)
                link_text = self._page.get_channel_group_linktext(channel)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Channel Groups > Configure Channel Group")
                description = page.get_channel_group_description_from_config_page()
                page.set_channel_group_description_via_config_page(description + " edit")
                page.click_save()
                new_channel = page.get_list_of_channels()[index]
                new_description = page.get_channel_group_description(new_channel)
                self.assertEqual(new_description, description + " edit")
                page.driver.get(link_text)
                page.set_channel_group_description_via_config_page(description)
                page.click_save()
        finally:
            page.driver.quit()
    
    def test_can_add_channel_to_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for channel in channels:
                link_text = self._page.get_channel_group_linktext(channel)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Channel Groups > Configure Channel Group")
                channel_name = page.get_first_channel_name_from_add_select()
                page.add_channel_to_channel_group(channel_name)
                page.click_save()
                page.driver.get(link_text)
                self.assertTrue(page.channel_name_is_member_of_channel_group(channel_name))
                page.remove_all_channels_from_group()
                page.click_save()
        finally:
            page.driver.quit()
    
    def test_can_change_user_permissions_of_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for channel in channels:
                link_text = self._page.get_channel_group_linktext(channel)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Channel Groups > Configure Channel Group")
                page.add_user_to_channel_group_permission("anon")
                page.click_save()
                page.driver.get(link_text)
                self.assertTrue(page.check_user_has_channel_group_permission("anon"))
                page.remove_user_from_channel_group_permission("anon")
                page.click_save()
        finally:
            page.driver.quit()
            
    def test_can_change_user_group_of_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        channels = self._page.get_list_of_channels()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for channel in channels:
                link_text = self._page.get_channel_group_linktext(channel)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Channel Groups > Configure Channel Group")
                page.add_channel_group_to_user_group()
                page.click_save()
                page.driver.get(link_text)
                self.assertTrue(page.check_channel_group_in_user_group())
                page.remove_channel_group_from_user_group()
                page.click_save()
        finally:
            page.driver.quit()
