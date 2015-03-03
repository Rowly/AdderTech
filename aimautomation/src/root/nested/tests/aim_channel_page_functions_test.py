'''
Created on 28 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimChannelPageFunctionsTest(BaseAimRegressionTest):

    def test_subtab_links_open_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels > Add Channel")
        self._page.click_view_channel_groups_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")
        self._page.click_view_channels_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")

    def test_add_channel_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels > Add Channel")

    def test_view_channel_groups_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_name(channels[0])
        self._page.send_search_term_to_channel_name(search_term)
        self._page.click_on_filter_channels_by_name()
        for chnl in self._page.get_list_of_channels():
            self.assertTrue(search_term in self._page.get_channel_name(chnl))

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_name(channels[0])
        self._page.send_search_term_to_channel_name(search_term)
        self._page.click_on_filter_channels_by_name()
        filtered_chnls = self._page.get_list_of_channels()
        for chnl in filtered_chnls:
            self.assertTrue(search_term in self._page.get_channel_name(chnl))
        self._page.click_on_remove_channels_name_filter()
        non_filtered_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_chnls) <= len(non_filtered_chnls))

    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_name(channels[0])
        self._page.send_search_term_to_channel_name(search_term)
        self._page.click_on_filter_channels_by_name()
        filtered_chnls = self._page.get_list_of_channels()
        for chnl in filtered_chnls:
            self.assertTrue(search_term in self._page.get_channel_name(chnl))
        self._page.clear_channel_names_filter()
        self._page.click_on_filter_channels_by_name()
        non_filtered_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_chnls) <= len(non_filtered_chnls))

    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_desc(channels[0])
        self._page.send_search_term_to_channel_desc(search_term)
        self._page.click_on_filter_channels_by_description()
        for chnl in self._page.get_list_of_channels():
            desc = self._page.get_channel_desc(chnl)
            self.assertTrue(search_term in desc)

    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_desc(channels[0])
        self._page.send_search_term_to_channel_desc(search_term)
        self._page.click_on_filter_channels_by_description()
        filtered_chnls = self._page.get_list_of_channels()
        for chnl in filtered_chnls:
            desc = self._page.get_channel_desc(chnl)
            self.assertTrue(search_term in desc)
        self._page.click_on_remove_channels_description_filter()
        non_filtered_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_chnls) <= len(non_filtered_chnls))

    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_desc(channels[0])
        self._page.send_search_term_to_channel_desc(search_term)
        self._page.click_on_filter_channels_by_description()
        filtered_chnls = self._page.get_list_of_channels()
        for chnl in filtered_chnls:
            desc = self._page.get_channel_desc(chnl)
            self.assertTrue(search_term in desc)
        self._page.clear_channel_descriptions_filter()
        self._page.click_on_filter_channels_by_description()
        non_filtered_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_chnls) <= len(non_filtered_chnls))

    def test_location_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_loc(channels[0])
        self._page.send_search_term_to_channel_loc(search_term)
        self._page.click_on_filter_channels_by_location()
        for chnl in self._page.get_list_of_channels():
            loc = self._page.get_channel_loc(chnl)
            self.assertTrue(search_term in loc)

    def test_location_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_loc(channels[0])
        self._page.send_search_term_to_channel_loc(search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_chnls = self._page.get_list_of_channels()
        for chnl in filtered_chnls:
            loc = self._page.get_channel_loc(chnl)
            self.assertTrue(search_term in loc)
        self._page.click_on_remove_channels_location_filter()
        non_filtered_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_chnls) <= len(non_filtered_chnls))

    def test_location_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_loc(channels[0])
        self._page.send_search_term_to_channel_loc(search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_chnls = self._page.get_list_of_channels()
        for chnl in filtered_chnls:
            loc = self._page.get_channel_loc(chnl)
            self.assertTrue(search_term in loc)
        self._page.clear_channel_locations_filter()
        self._page.click_on_filter_channels_by_location()
        non_filtered_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_chnls) <= len(non_filtered_chnls))

    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        name_search_term = self._page.get_channel_name(channels[0])
        desc_search_term = self._page.get_channel_desc(channels[0])
        loc_search_term = self._page.get_channel_loc(channels[0])

        self._page.send_search_term_to_channel_name(name_search_term)
        self._page.click_on_filter_channels_by_name()
        filtered_name_chnls = self._page.get_list_of_channels()
        self._page.click_on_remove_filters()
        remove_filter_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_name_chnls) <= len(remove_filter_chnls))

        self._page.send_search_term_to_channel_desc(desc_search_term)
        self._page.click_on_filter_channels_by_description()
        filtered_desc_chnls = self._page.get_list_of_channels()
        self._page.click_on_remove_filters()
        remove_filter_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_desc_chnls) <= len(remove_filter_chnls))

        self._page.send_search_term_to_channel_loc(loc_search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_loc_chnls = self._page.get_list_of_channels()
        self._page.click_on_remove_filters()
        remove_filter_chnls = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_loc_chnls) <= len(remove_filter_chnls))

    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_ascend_channel_names()
        sorted_channels = self._page.get_list_of_channels()
        if len(sorted_channels) > 1:
            chnl_names = [self._page.get_channel_name(chnl)
                             for chnl in sorted_channels]
            for counter in range(0, (len(chnl_names) - 1)):
                prior = chnl_names[counter].lower()
                latter = chnl_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_decend_channel_names()
        sorted_channels = self._page.get_list_of_channels()
        if len(sorted_channels) > 1:
            chnl_names = [self._page.get_channel_name(channel)
                             for channel in sorted_channels]
            for counter in range(0, (len(chnl_names) - 1)):
                prior = chnl_names[counter].lower()
                latter = chnl_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_ascend_channel_descriptions()
        sorted_channels = self._page.get_list_of_channels()
        if len(sorted_channels) > 1:
            chnl_descs = [self._page.get_channel_desc(chnl)
                          for chnl in sorted_channels]
            for counter in range(0, (len(chnl_descs) - 1)):
                prior = chnl_descs[counter].lower()
                latter = chnl_descs[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_decend_channel_descriptions()
        sorted_channels = self._page.get_list_of_channels()
        if len(sorted_channels) > 1:
            chnl_descs = [self._page.get_channel_desc(chnl)
                          for chnl in sorted_channels]
            for counter in range(0, (len(chnl_descs) - 1)):
                prior = chnl_descs[counter].lower()
                latter = chnl_descs[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_locations_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_ascend_channel_locations()
        sorted_channels = self._page.get_list_of_channels()
        if len(sorted_channels) > 1:
            chnl_locs = [self._page.get_channel_loc(chnl)
                         for chnl in sorted_channels]
            for counter in range(0, (len(chnl_locs) - 1)):
                prior = chnl_locs[counter].lower()
                latter = chnl_locs[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_locations_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_decend_channel_locations()
        sorted_channels = self._page.get_list_of_channels()
        if len(sorted_channels) > 1:
            chnl_locs = [self._page.get_channel_loc(chnl)
                         for chnl in sorted_channels]
            for counter in range(0, (len(chnl_locs) - 1)):
                prior = chnl_locs[counter].lower()
                latter = chnl_locs[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        for counter in range(0, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Channel")
            self._driver.back()

    def test_can_open_clone_channel_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        for counter in range(0, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_channel_clone(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channels > Configure Cloned Channel")
            self._driver.back()

    def test_can_open_and_cancel_delete_channel_dialogue(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        for channel in channels:
            self._page.click_channel_delete(channel)
            self.assertTrue("Delete channel"
                            in self._page.get_delete_chnl_txt_from_lightbox())
            self._page.click_lightbox_cancel_button()
            self.assertFalse(self._page.check_lightbox_visibility())

    def test_can_delete_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.reset_number_of_channels()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_delete(channels[-1])
        self.assertTrue("Delete channel"
                        in self._page.get_delete_chnl_txt_from_lightbox())
        self._page.click_lightbox_delete_button()
        self.assertFalse(self._page.check_lightbox_visibility())
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) > len(new_channels))
        self.reset_number_of_channels()

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertFalse(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.verify_batch_delete_checkbox())

    def test_can_cancel_batch_delete(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_batch_delete_mode()
        for chnl in channels:
            self.assertTrue(self._page.verify_batch_delete_channel(chnl))
        self._page.click_batch_delete_mode()
        for channels in channels:
            self.assertFalse(self._page.verify_batch_delete_channel(chnl))
        channels = self._page.get_list_of_channels()
        self._page.click_batch_delete_mode()
        self._page.click_batch_delete_channel(channels[-1])
        self._page.click_batch_delete_channel(channels[-2])
        self._page.click_batch_delete_channels()
        self._page.click_lightbox_cancel_button()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) == len(new_channels))

    def test_can_batch_delete_channels(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.reset_number_of_channels()
        self._page.click_batch_delete_mode()
        channels = self._page.get_list_of_channels()
        self._page.click_batch_delete_channel(channels[-1])
        self._page.click_batch_delete_channel(channels[-2])
        self._page.click_batch_delete_channels()
        self._page.click_lightbox_delete_button()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) >= len(new_channels))
        self.reset_number_of_channels()

    """
    Default appearances
    """
    def test_channel_page_opened_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self.assertEqual(self._page.get_text_of_view_channel_link(),
                         "View Channels")
        self.assertEqual(self._page.get_text_of_add_channel_link_link(),
                         "Add Channel")
        self.assertEqual(self._page.get_text_of_view_channel_group_link(),
                         "View Channel Groups")
        self.assertEqual(self._page.get_text_of_add_channel_group_link(),
                         "Add Channel Group")

    def test_channels_are_shown_in_paginated_table(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) >= 1)
        total_channels = self._page.get_pagination_total()
        if int(total_channels) <= 20:
            self.assertTrue(len(channels) <= int(total_channels))
        elif int(total_channels) > 20:
            pass

    def test_each_channel_row_comprises_correct_elements(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) >= 1)
        for channel in channels:
            cells = self._page.get_cell_elements(channel)
            self.assertEqual(len(cells), 8)
            name_class = self._page.get_attribute_of_element(cells[0], "class")
            self.assertEqual(name_class, "left channel_name_id")
            self.assertNotEqual(self._page.get_text_of_element(cells[0]), "")
            img_src = self._page.get_channel_conx_default_img_src(cells[1])
            self.assertTrue(img_src, self._silk_dir + "inherit.png")
            self.assertTrue(self._page.get_class_attribute_of_link(cells[2]),
                            "tooltip")
            self.assertTrue(self._page.get_class_attribute_of_link(cells[3]),
                            "tooltip")
            self.assertTrue(self._page.get_class_attribute_of_link(cells[4]),
                            "tooltip")
            self.assertNotEqual(self._page.get_text_of_element(cells[5]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[6]), "")
            img_src = self._page.get_configure_channel_img_src(cells[7])
            self.assertEqual(img_src, self._silk_dir + "pencil.png")
            img_src = self._page.get_clone_channel_img_src(cells[7])
            self.assertEqual(img_src, self._silk_dir + "page_copy_green.png")
            img_src = self._page.get_delete_channel_img_src(cells[7])
            self.assertEqual(img_src, self._silk_dir + "delete.png")

    def test_search_fields_are_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertTrue(self._page.get_located_search_by_channel_name())
        self.assertTrue(self._page.get_located_search_by_channel_description())
        self.assertTrue(self._page.get_located_search_by_channel_location())

    """
    Utilities
    """
    def reset_number_of_channels(self):
        current_names = [self._page.get_channel_name(channel)
                         for channel in self._page.get_list_of_channels()]
        missing_names = list(set(self._channel_names) - set(current_names))
        if missing_names:
            for name in missing_names:
                self._page.click_add_channel_button()
                self._page.set_channel_name_via_config_page(name)
                split = name.split()
                end = split[-1]
                desc = "desc " + end
                self._page.set_channel_description_via_config_page(desc)
                loc = "loc " + end
                self._page.set_channel_location_via_config_page(loc)
                self._page.set_channel_video_source(end + " [1]")
                if (end + " [2]") in self._page.get_video2_source_options():
                    self._page.set_channel_video2_source(end + " [2]")
                self._page.set_channel_audio_source(end)
                self._page.set_channel_usb_source(end)
                self._page.add_user_to_channel_permission("admin")
                self._page.click_save()
