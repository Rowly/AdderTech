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
        self.assertEqual(self._page.get_text_of_page_header(), "Channels > Add Channel")
        self._page.click_view_channel_groups_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")
        self._page.click_add_channel_group_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups > Add Channel Group")
        self._page.click_view_channels_subtab_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
    
    def test_add_channel_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_add_channel_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels > Add Channel")

    def test_view_channel_groups_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "Channel Groups")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_name(channels[0])
        self._page.send_search_term_to_channel_name_field(search_term)
        self._page.click_on_filter_channels_by_name()
        channels = self._page.get_list_of_channels()
        for channel in channels:
            self.assertTrue(search_term in self._page.get_channel_name(channel))

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_name(channels[0])
        self._page.send_search_term_to_channel_name_field(search_term)
        self._page.click_on_filter_channels_by_name()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_name(channel))
        self._page.click_on_remove_channels_name_filter()
        non_filtered_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_channels) <= len(non_filtered_channels))
    
    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_name(channels[0])
        self._page.send_search_term_to_channel_name_field(search_term)
        self._page.click_on_filter_channels_by_name()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_name(channel))
        self._page.clear_channel_names_filter()
        self._page.click_on_filter_channels_by_name()
        non_filtered_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_channels) <= len(non_filtered_channels))
        
    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_description(channels[0])
        self._page.send_search_term_to_channel_description_field(search_term)
        self._page.click_on_filter_channels_by_description()
        channels = self._page.get_list_of_channels()
        for channel in channels:
            self.assertTrue(search_term in self._page.get_channel_description(channel))
            
    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_description(channels[0])
        self._page.send_search_term_to_channel_description_field(search_term)
        self._page.click_on_filter_channels_by_description()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_description(channel))
        self._page.click_on_remove_channels_description_filter()
        non_filtered_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_channels) <= len(non_filtered_channels))
    
    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_description(channels[0])
        self._page.send_search_term_to_channel_description_field(search_term)
        self._page.click_on_filter_channels_by_description()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_description(channel))
        self._page.clear_channel_descriptions_filter()
        self._page.click_on_filter_channels_by_description()
        non_filtered_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_channels) <= len(non_filtered_channels))
        
    def test_location_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_location(channels[0])
        self._page.send_search_term_to_channel_location_field(search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_location(channel))
            
    def test_location_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_location(channels[0])
        self._page.send_search_term_to_channel_location_field(search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_location(channel))
        self._page.click_on_remove_channels_location_filter()
        non_filtered_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_channels) <= len(non_filtered_channels))
    
    def test_location_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        search_term = self._page.get_channel_location(channels[0])
        self._page.send_search_term_to_channel_location_field(search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_channels = self._page.get_list_of_channels()
        for channel in filtered_channels:
            self.assertTrue(search_term in self._page.get_channel_location(channel))
        self._page.clear_channel_locations_filter()
        self._page.click_on_filter_channels_by_location()
        non_filtered_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_channels) <= len(non_filtered_channels))
    
    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        name_search_term = self._page.get_channel_name(channels[0])
        desc_search_term = self._page.get_channel_description(channels[0])
        loc_search_term = self._page.get_channel_location(channels[0])
        self._page.send_search_term_to_channel_name_field(name_search_term)
        self._page.click_on_filter_channels_by_name()
        filtered_by_name_channels = self._page.get_list_of_channels()
        self._page.click_on_remove_filters()
        remove_filter_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_by_name_channels) <= len(remove_filter_channels))
        self._page.send_search_term_to_channel_description_field(desc_search_term)
        self._page.click_on_filter_channels_by_description()
        filtered_by_description_channels = self._page.get_list_of_channels()
        self._page.click_on_remove_filters()
        remove_filter_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_by_description_channels) <= len(remove_filter_channels))
        self._page.send_search_term_to_channel_location_field(loc_search_term)
        self._page.click_on_filter_channels_by_location()
        filtered_by_location_channels = self._page.get_list_of_channels()
        self._page.click_on_remove_filters()
        remove_filter_channels = self._page.get_list_of_channels()
        self.assertTrue(len(filtered_by_location_channels) <= len(remove_filter_channels))
        
    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_ascend_channel_names()
        sorted_channels = self._page.get_list_of_channels()
        channel_names = []
        if len(sorted_channels) > 1:
            for channel in sorted_channels:
                channel_names.append(self._page.get_channel_name(channel))
            counter = 0
            for counter in range((len(channel_names) - 1)):
                self.assertTrue(channel_names[counter].lower() <= channel_names[counter + 1].lower())
                
    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_decend_channel_names()
        sorted_channels = self._page.get_list_of_channels()
        channel_names = []
        if len(sorted_channels) > 1:
            for channel in sorted_channels:
                channel_names.append(self._page.get_channel_name(channel))
            counter = 0
            for counter in range((len(channel_names) - 1)):
                self.assertTrue(channel_names[counter].lower() >= channel_names[counter + 1].lower())
                
    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_ascend_channel_descriptions()
        sorted_channels = self._page.get_list_of_channels()
        channel_descriptions = []
        if len(sorted_channels) > 1:
            for channel in sorted_channels:
                channel_descriptions.append(self._page.get_channel_description(channel))
            counter = 0
            for counter in range((len(channel_descriptions) - 1)):
                self.assertTrue(channel_descriptions[counter].lower() <= channel_descriptions[counter + 1].lower())        
    
    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_decend_channel_descriptions()
        sorted_channels = self._page.get_list_of_channels()
        channel_descriptions = []
        if len(sorted_channels) > 1:
            for channel in sorted_channels:
                channel_descriptions.append(self._page.get_channel_description(channel))
            counter = 0
            for counter in range((len(channel_descriptions) - 1)):
                self.assertTrue(channel_descriptions[counter].lower() >= channel_descriptions[counter + 1].lower())        

    def test_can_sort_locations_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_ascend_channel_locations()
        sorted_channels = self._page.get_list_of_channels()
        channel_locations = []
        if len(sorted_channels) > 1:
            for channel in sorted_channels:
                channel_locations.append(self._page.get_channel_location(channel))
            counter = 0
            for counter in range((len(channel_locations) - 1)):
                self.assertTrue(channel_locations[counter].lower() <= channel_locations[counter + 1].lower())        

    def test_can_sort_locations_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self._page.click_on_decend_channel_locations()
        sorted_channels = self._page.get_list_of_channels()
        channel_locations = []
        if len(sorted_channels) > 1:
            for channel in sorted_channels:
                channel_locations.append(self._page.get_channel_location(channel))
            counter = 0
            for counter in range((len(channel_locations) - 1)):
                self.assertTrue(channel_locations[counter].lower() >= channel_locations[counter + 1].lower())
    
    def test_can_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_configure_channel(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
            self._driver.back()
    
    def test_can_open_clone_channel_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        counter = 0
        channels = self._page.get_list_of_channels()
        for counter in range(counter, len(channels)):
            channels = self._page.get_list_of_channels()
            self._page.click_channel_clone(channels[counter])
            self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Cloned Channel")
            self._driver.back()
    
    def test_can_open_and_cancel_delete_channel_dialogue(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        for channel in channels:
            self._page.click_channel_delete(channel)
            self.assertTrue("Delete channel" in self._page.get_delete_channel_text_from_lightbox())
            self._page.click_lightbox_cancel_button()
            self.assertFalse(self._page.check_lightbox_visibility())
    
    def test_can_delete_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.reset_number_of_channels()
        channels = self._page.get_list_of_channels()
        self._page.click_channel_delete(channels[-1])
        self.assertTrue("Delete channel" in self._page.get_delete_channel_text_from_lightbox())
        self._page.click_lightbox_delete_button()
        self.assertFalse(self._page.check_lightbox_visibility())
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) > len(new_channels))
        self.reset_number_of_channels()

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertFalse(self._page.check_for_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.check_for_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.check_for_batch_delete_checkbox())
    
    def test_can_cancel_batch_delete(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        self._page.click_batch_delete_mode()
        for channel in channels:
            self.assertTrue(self._page.check_for_batch_delete_checkbox_for_channel_element(channel))
        self._page.click_batch_delete_mode()
        for channels in channels:
            self.assertFalse(self._page.check_for_batch_delete_checkbox_for_channel_element(channel))
        channels = self._page.get_list_of_channels()
        self._page.click_batch_delete_mode()
        self._page.click_batch_delete_selector_for_channel_element(channels[-1])
        self._page.click_batch_delete_selector_for_channel_element(channels[-2])
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
        self._page.click_batch_delete_selector_for_channel_element(channels[-1])
        self._page.click_batch_delete_selector_for_channel_element(channels[-2])
        self._page.click_batch_delete_channels()
        self._page.click_lightbox_delete_button()
        new_channels = self._page.get_list_of_channels()
        self.assertTrue(len(channels) >= len(new_channels))
        self.reset_number_of_channels()
        
    def reset_number_of_channels(self):
        current_names = []
        for channel in self._page.get_list_of_channels():
            current_names.append(self._page.get_channel_name(channel))
        missing_names = list(set(self._channel_names) - set(current_names))
        if missing_names:
            for name in missing_names:
                self._page.click_add_channel_button()
                self._page.set_channel_name_via_config_page(name)
                split = name.split()
                end = split[-1]
                self._page.set_channel_description_via_config_page("desc " + end)
                self._page.set_channel_location_via_config_page("loc " + end)
                self._page.set_channel_video_source_by_visible_text(end + " [1]")
                try:
                    self._page.set_channel_video2_source_by_visible_text(end + " [2]")
                except Exception:
                    pass
                self._page.set_channel_audio_source_by_visible_text(end)
                self._page.set_channel_usb_source_by_visible_text(end)
                self._page.add_user_to_channel_permission("admin")
                self._page.click_save()
                self._page.check_for_error_message("configure_channel_ajax_message")
        self._driver.refresh()