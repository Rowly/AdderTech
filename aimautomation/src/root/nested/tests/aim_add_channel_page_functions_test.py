'''
Created on 4 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimAddChannelPageFunctionsTest(BaseAimRegressionTest):

    name = "New Name"
    desc = "New Desc"
    loc = "New Loc"

    def test_cannot_create_channel_without_a_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels > Add Channel")
        msg = self._page.is_ajax_error_message_displayed_for_channel()
        self.assertFalse(msg)
        self._page.click_save_ignore_warnings()
        msg = self._page.is_ajax_error_message_displayed_for_channel()
        self.assertTrue(msg)

    def test_can_create_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        img_srcs = img_srcs
        self.assertEqual(img_srcs[0], self._silk_dir + "inherit.png")
        self._page.click_channel_delete(chnl)
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_view_only_connection(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.set_channel_connections_to_view_only()
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "eye.png")
        self._page.click_channel_delete(chnl)
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_view_shared_only_connection(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.set_channel_connections_to_view_shared_only()
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "eye.png")
        self.assertEqual(img_srcs[1], self._silk_dir + "multicast.png")
        self._page.click_channel_delete(chnl)
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_shared_only_connection(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.set_channel_connections_to_shared_only()
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "multicast.png")
        self._page.click_channel_delete(chnl)
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_exclusive_only_connection(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.set_channel_connections_to_exclusive_only()
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "lock.png")
        self._page.click_channel_delete(chnl)
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_view_shared_and_exclusive_conx(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.set_channel_connections_to_view_shared_and_exclusive()
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "eye.png")
        self.assertEqual(img_srcs[1], self._silk_dir + "multicast.png")
        self.assertEqual(img_srcs[2], self._silk_dir + "lock.png")
        self._page.click_channel_delete(chnl)
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.add_channel_to_group("group 0")
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "inherit.png")
        link_text = self._page.get_channel_config_linktext(chnl)
        self._page.driver.get(link_text)
        self.assertTrue("group 0"
                        in self._page.get_selected_c_groups_for_user())
        self._page.open_channels_tab()
        final_channels = self._page.get_list_of_channels()
        self._page.click_channel_delete(final_channels[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_channel_with_user_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_add_channel_button()
        self.complete_details()
        self._page.add_channel_to_user_group("group 0")
        self._page.click_save()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(new_channels) > len(channels))
        chnl = new_channels[-1]
        self.assertEqual(self._page.get_channel_name(chnl), self.name)
        self.assertEqual(self._page.get_channel_desc(chnl), self.desc)
        self.assertEqual(self._page.get_channel_loc(chnl), self.loc)
        img_srcs = self._page.get_channel_connection_img_src(chnl)
        self.assertEqual(img_srcs[0], self._silk_dir + "inherit.png")
        link_text = self._page.get_channel_config_linktext(chnl)
        self._page.driver.get(link_text)
        self.assertTrue("group 0"
                        in self._page.get_all_user_groups_for_channel())
        self._page.open_channels_tab()
        final_channels = self._page.get_list_of_channels()
        self._page.click_channel_delete(final_channels[-1])
        self._page.click_lightbox_delete_button()

    def complete_details(self):
        prefix = self._channel_names[0].replace("Channel ", "")
        self._page.set_channel_name_via_config_page(self.name)
        self._page.set_channel_description_via_config_page(self.desc)
        self._page.set_channel_location_via_config_page(self.loc)
        self._page.set_channel_video_source(prefix + " [1]")
        self._page.set_channel_audio_source(prefix)
        self._page.set_channel_usb_source(prefix)
        self._page.set_channel_serial_source("- OFF -")
        self._page.add_user_to_channel_permission("admin")
