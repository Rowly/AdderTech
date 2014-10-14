'''
Created on 19 Jun 2013

@author: Mark.Rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimPresetsConfigPageFunctionsTest(BaseAimRegressionTest):
    
    def test_can_change_preset_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        counter = 0
        presets = self._page.get_list_of_presets()
        for counter in range(counter, len(presets)):
            presets = self._page.get_list_of_presets()
            name = self._page.get_preset_name(presets[counter])
            self._page.click_preset_configure(presets[counter])
            self._page.set_preset_name_via_config_page(name + " edit")
            self._page.click_save()
            self._page.confirm_no_longer_on_preset_config_page()
            presets = self._page.get_list_of_presets()
            self._page.click_preset_configure(presets[counter])
            self.assertEqual(self._page.get_preset_name_from_config_page(), name + " edit")
            self._page.set_preset_name_via_config_page(name)
            self._page.click_save()
            self._page.confirm_no_longer_on_preset_config_page()
        self.reset_number_of_channels()
 
    def test_can_change_preset_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        counter = 0
        presets = self._page.get_list_of_presets()
        for counter in range(counter, len(presets)):
            presets = self._page.get_list_of_presets()
            desc = self._page.get_preset_description(presets[counter])
            self._page.click_preset_configure(presets[counter])
            self._page.set_preset_description_via_config_page(desc + " edit")
            self._page.click_save()
            self._page.confirm_no_longer_on_preset_config_page()
            presets = self._page.get_list_of_presets()
            self._page.click_preset_configure(presets[counter])
            self.assertEqual(self._page.get_preset_description_from_config_page(), desc + " edit")
            self._page.set_preset_description_via_config_page(desc)
            self._page.click_save()
            self._page.confirm_no_longer_on_preset_config_page()
        self.reset_number_of_channels()
  
    def test_can_change_number_of_pairs_in_preset(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        counter = 0
        presets = self._page.get_list_of_presets()
        for counter in range(counter, len(presets)):
            presets = self._page.get_list_of_presets()
            self._page.click_preset_configure(presets[counter])
            self._page.add_new_preset_pair()
            self._page.click_save()
            self._page.confirm_no_longer_on_preset_config_page()
            presets = self._page.get_list_of_presets()
            self._page.click_preset_configure(presets[counter])
            self.assertTrue(len(self._page.get_list_of_preset_pairs()) > 1)
            self._page.reset_preset_pairs()
            self._page.click_save()
            self._page.confirm_no_longer_on_preset_config_page()
        self.reset_number_of_channels()
  
    def test_can_change_number_pairs_to_all_unicast_available(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.add_all_available_pairs()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self.assertTrue(len(self._page.get_list_of_preset_pairs()) > 1)
        self._page.reset_preset_pairs()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        self.reset_number_of_channels()
  
    def test_can_change_number_pairs_to_include_multicast(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.add_multicast_pair()
        self._page.confirm_no_longer_on_preset_config_page()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self.assertTrue(len(self._page.get_list_of_preset_pairs()) > 1)
        self._page.reset_preset_pairs()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        self.reset_number_of_channels()
  
    def test_cannot_change_number_pairs_to_include_same_receiver(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.add_same_receiver_pair()
        self.assertEqual(self._page.check_for_receiver_single_connnection_error_message(), "A Receiver can only be used in one connection pair")
        self.reset_number_of_channels()
  
    def test_can_change_allowed_connections_to_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_view_only()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        presets = self._page.get_list_of_presets()
        self.assertTrue(self._page.get_preset_connection_view_only_button_visibility(presets[-1]))
        self.assertFalse(self._page.get_preset_connection_shared_button_visibility(presets[-1]))
        self.assertFalse(self._page.get_preset_connection_exclusive_button_visibility(presets[-1]))
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_global()
        self._page.click_save()
        self.reset_number_of_channels()
  
    def test_can_change_allowed_connections_to_shared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_shared()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        presets = self._page.get_list_of_presets()
        self.assertTrue(self._page.get_preset_connection_view_only_button_visibility(presets[-1]))
        self.assertTrue(self._page.get_preset_connection_shared_button_visibility(presets[-1]))
        self.assertFalse(self._page.get_preset_connection_exclusive_button_visibility(presets[-1]))
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_global()
        self._page.click_save()
        self.reset_number_of_channels()
          
    def test_can_change_allowed_connections_to_exclusive(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_exclusive()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        presets = self._page.get_list_of_presets()
        self.assertFalse(self._page.get_preset_connection_view_only_button_visibility(presets[-1]))
        self.assertFalse(self._page.get_preset_connection_shared_button_visibility(presets[-1]))
        self.assertTrue(self._page.get_preset_connection_exclusive_button_visibility(presets[-1]))
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_global()
        self._page.click_save()
        self.reset_number_of_channels()
  
    def test_can_change_allowed_connections_to_all(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.change_channels_to_working_set()
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_all()
        self._page.click_save()
        self._page.confirm_no_longer_on_preset_config_page()
        presets = self._page.get_list_of_presets()
        self.assertTrue(self._page.get_preset_connection_view_only_button_visibility(presets[-1]))
        self.assertTrue(self._page.get_preset_connection_shared_button_visibility(presets[-1]))
        self.assertTrue(self._page.get_preset_connection_exclusive_button_visibility(presets[-1]))
        self._page.click_preset_configure(presets[-1])
        self._page.select_preset_connection_global()
        self._page.click_save()
        self.reset_number_of_channels()
      
    def change_channels_to_working_set(self):
        self._page.open_channels_tab()
        channels = self._page.get_list_of_channels()
        if len(channels) > 6:
            self._page.click_batch_delete_mode()
            counter = 6
            for counter in range(counter, len(channels)):
                self._page.click_batch_delete_selector_for_channel_element(channels[counter])
            self._page.click_batch_delete_channels()
            self._page.click_lightbox_delete_button()
      
    def reset_number_of_channels(self):
        self._page.open_channels_tab()
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