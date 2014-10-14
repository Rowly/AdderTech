'''
Created on 3 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimChannelConfigPageFunctionsTest(BaseAimRegressionTest):
 
    def test_can_change_channel_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()     
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            name = self._page.get_channel_name_from_config_page()
            self._page.set_channel_name_via_config_page(name + " edit")
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            new_name = self._page.get_channel_name(channels[counter])
            self.assertEqual(new_name, name + " edit")
            self._page.click_configure_channel(channels[counter])
            self._page.set_channel_name_via_config_page(name)
            self._page.click_save()
 
    def test_can_change_channel_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            description = self._page.get_channel_description_from_config_page()
            self._page.set_channel_description_via_config_page(description + " edit")
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            new_description = self._page.get_channel_description(channels[counter])
            self.assertEqual(new_description, description + " edit")
            self._page.click_configure_channel(channels[counter])
            self._page.set_channel_description_via_config_page(description)
            self._page.click_save()
 
    def test_can_change_channel_location(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            location = self._page.get_channel_location_from_config_page()
            self._page.set_channel_location_via_config_page(location + " edit")
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            new_location = self._page.get_channel_location(channels[counter])
            self.assertEqual(new_location, location + " edit")
            self._page.click_configure_channel(channels[counter])
            self._page.set_channel_location_via_config_page(location)
            self._page.click_save()
       
    def test_can_change_channel_video_source(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            before = self._page.get_selected_video_source()
            self._page.set_channel_video_source(1)
            check = self._page.get_selected_video_source()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.is_channel_video_source(check))
            self._page.reset_channel_video_source(before)
            self._page.click_save()
   
    def test_can_change_channel_usb_source(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            before = self._page.get_selected_usb_source()
            self._page.set_channel_usb_source(1)
            check = self._page.get_selected_usb_source()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.is_channel_usb_source(check))
            self._page.reset_channel_usb_source(before)
            self._page.click_save()
   
    def test_can_change_channel_serial_source(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            before = self._page.get_selected_serial_source()
            self._page.set_channel_serial_source(1)
            check = self._page.get_selected_serial_source()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.is_channel_serial_source(check))
            self._page.reset_channel_serial_source(before)
            self._page.click_save()
               
    def test_can_change_allowed_connections_of_channel_to_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.set_channel_connections_to_view_only()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.get_channel_connections_to_view_only_selected())
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()
   
    def test_can_change_allowed_connections_of_channel_to_view_shared_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.set_channel_connections_to_view_shared_only()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.get_channel_connections_to_view_shared_only_selected())
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()
 
    def test_can_change_allowed_connections_of_channel_to_exclusive_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.set_channel_connections_to_exclusive_only()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.get_channel_connections_to_exclusive_only_selected())
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()
   
    def test_can_change_allowed_connections_of_channel_to_view_shared_and_exclusive_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.set_channel_connections_to_view_shared_and_exclusive()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.get_channel_connections_to_view_shared_and_exclusive_selected())
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()
               
    def test_can_change_user_permissions_of_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.add_user_to_channel_permission("user 0")
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.check_user_has_channel_permission("user 0"))
            self._page.remove_user_from_channel_permission("user 0")
            self._page.click_save()

    def test_can_change_channel_group_of_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.add_channel_to_group()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.check_channel_in_channel_group())
            self._page.remove_channel_from_group()
            self._page.click_save()
   
    def test_can_change_user_group_of_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._page.add_channel_to_user_group()
            self._page.click_save()
            self._page.confirm_no_longer_on_configure_channel_page()
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertTrue(self._page.check_channel_in_user_group())
            self._page.remove_channel_from_user_group()
            self._page.click_save()