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
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            name = self._page.get_channel_name_from_config_page()
            self._page.set_channel_name_via_config_page(name + " edit")
            self._page.click_save()
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
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            desc = self._page.get_channel_description_from_config_page()
            self._page.set_channel_description_via_config_page(desc + " edit")
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            new_description = self._page.get_channel_desc(chnl)
            self.assertEqual(new_description, desc + " edit")
            self._page.click_configure_channel(chnl)
            self._page.set_channel_description_via_config_page(desc)
            self._page.click_save()

    def test_can_change_channel_location(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            location = self._page.get_channel_location_from_config_page()
            self._page.set_channel_location_via_config_page(location + " edit")
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            new_location = self._page.get_channel_loc(chnl)
            self.assertEqual(new_location, location + " edit")
            self._page.click_configure_channel(chnl)
            self._page.set_channel_location_via_config_page(location)
            self._page.click_save()

    def test_can_change_channel_video_source(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            name = self._page.get_channel_name(chnl).replace("Channel ", "")
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            self.assertTrue(name in self._page.get_selected_video_source())
            before = self._page.get_selected_video_source()
            new = self._page.get_different_video_source(before)
            self._page.set_channel_video_source(new)
            check = self._page.get_selected_video_source()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertTrue(self._page.get_selected_video_source() == check)
            self._page.reset_channel_video_source(before)
            self._page.click_save()

    def test_can_change_channel_usb_source(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            name = self._page.get_channel_name(chnl).replace("Channel ", "")
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            self.assertTrue(name in self._page.get_selected_usb_source())
            before = self._page.get_selected_usb_source()
            new = self._page.get_different_usb_source(before)
            self._page.set_channel_usb_source(new)
            check = self._page.get_selected_usb_source()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertTrue(self._page.get_selected_usb_source() == check)
            self._page.reset_channel_usb_source(before)
            self._page.click_save()

    def test_can_change_channel_serial_source(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            before = self._page.get_selected_serial_source()
            self.assertTrue(before == "- OFF -")
            new = self._page.get_different_serial_source(before)
            self._page.set_channel_serial_source(new)
            check = self._page.get_selected_serial_source()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertTrue(self._page.get_selected_serial_source() == check)
            self._page.reset_channel_serial_source(before)
            self._page.click_save()

    def test_can_change_allowed_connections_of_channel_to_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            state = self._page.get_channel_connection_state("inherit")
            self.assertTrue(state)
            self._page.set_channel_connections_to_view_only()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            state = self._page.get_channel_connection_state("view_only")
            self.assertTrue(state)
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()

    def test_can_change_allowed_connections_of_channel_to_shared_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            state = self._page.get_channel_connection_state("inherit")
            self.assertTrue(state)
            self._page.set_channel_connections_to_shared_only()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            state = self._page.get_channel_connection_state("shared")
            self.assertTrue(state)
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()

    def test_can_change_connections_of_channel_to_view_shared_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            state = self._page.get_channel_connection_state("inherit")
            self.assertTrue(state)
            self._page.set_channel_connections_to_view_shared_only()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            state = self._page.get_channel_connection_state("view_shared")
            self.assertTrue(state)
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()

    def test_can_change_allowed_connections_of_channel_to_exclusive_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            state = self._page.get_channel_connection_state("inherit")
            self.assertTrue(state)
            self._page.set_channel_connections_to_exclusive_only()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            state = self._page.get_channel_connection_state("exclusive")
            self.assertTrue(state)
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()

    def test_can_change_connections_of_channel_to_all(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            self.assertTrue(self._page.get_channel_connection_state("inherit"))
            self._page.set_channel_connections_to_view_shared_and_exclusive()
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertTrue(self._page.get_channel_connection_state("all"))
            self._page.set_channel_connections_to_global_settings()
            self._page.click_save()

    def test_can_change_user_permissions_of_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            self.assertTrue("admin" in self._page.get_all_users_for_channel())
            self._page.add_user_to_channel_permission("user 0")
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertTrue("user 0" in self._page.get_all_users_for_channel())
            self._page.remove_user_from_channel_permission("user 0")
            self._page.click_save()

    def test_can_change_channel_group_of_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            total_groups = self._page.get_selected_c_groups_for_user()
            self.assertTrue(len(total_groups) == 0)
            self._page.add_channel_to_group("group 0")
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            total_groups = self._page.get_selected_c_groups_for_user()
            self.assertTrue("group 0" in total_groups)
            self._page.remove_channel_from_group("group 0")
            self._page.click_save()

    def test_can_change_user_group_of_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        for counter in range(0, len(self._page.get_list_of_channels())):
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            total_groups = self._page.get_all_user_groups_for_channel()
            self.assertTrue(len(total_groups) == 0)
            self._page.add_channel_to_user_group("group 0")
            self._page.click_save()
            channels = self._page.get_list_of_channels()
            chnl = channels[counter]
            self._page.click_configure_channel(chnl)
            total_groups = self._page.get_all_user_groups_for_channel()
            self.assertTrue("group 0" in total_groups)
            self._page.remove_channel_from_user_group("group 0")
            self._page.click_save()
