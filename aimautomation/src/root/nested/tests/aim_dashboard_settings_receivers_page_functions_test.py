'''
Created on 11 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage

class AimDashboardSettingsReceiversPageFunctionsTest(BaseAimRegressionTest):
   
    def test_can_toggle_login_required(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        current_setting = self._page.get_login_required_setting()
        self._page.toggle_login_required()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        new_setting = self._page.get_login_required_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_login_required()
        self._page.click_save()
     
    def test_can_toggle_enable_required_osd_alerts(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        current_setting = self._page.get_login_required_setting()
        self._page.toggle_login_required()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        new_setting = self._page.get_login_required_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_login_required()
        self._page.click_save()
     
         
    def test_can_toggle_audio_input_type(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        options = self._page.get_audio_input_type_mode_options()
        counter = 0
        for counter in range(counter, len(options)):
            options = self._page.get_audio_input_type_mode_options()
            options[counter].click()
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_receivers_settings_button()
            self.assertTrue(self._page.get_selected_audio_input_type(counter))
         
    def test_can_change_video_compatibility_check(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        labels = self._page.get_video_compatibility_check_options()
        for label in labels:
            self._page.select_video_compatibility_check_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_receivers_settings_button()
            self.assertEqual(self._page.get_current_video_compatibility_check_selection_text(), label)
        self._page.select_video_compatibility_check_by_label("Off")
        self._page.click_save()
     
    def test_can_change_receiver_keyboard_country_code(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        labels = self._page.get_receiver_keyboard_country_code_options()
        for label in labels:
            self._page.select_receiver_keyboard_country_code_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_receivers_settings_button()
            self.assertEqual(self._page.get_current_receiver_keyboard_country_code_selection_text(), label)
        self._page.select_receiver_keyboard_country_code_by_label("gb - UK")
        self._page.click_save()
         
    def test_error_given_if_same_key_used_for_osd_hotkeys(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_osd_hotkey()
        second_key = self._page.get_selected_second_osd_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_osd_hotkey_validation_icon_appearance())
        self._page.select_second_osd_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_osd_hotkey_validation_icon_appearance())
     
    def test_error_given_if_same_key_used_for_shortcut_hotkeys(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_shortcut_hotkey()
        second_key = self._page.get_selected_second_shortcut_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_shortcut_hotkey_validation_icon_appearance())
        self._page.select_second_shortcut_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_shortcut_hotkey_validation_icon_appearance())
     
    def test_error_given_if_same_key_used_for_last_channel_hotkey(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_last_channel_hotkey()
        second_key = self._page.get_selected_second_last_channel_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_last_channel_hotkey_validation_icon_appearance())
        self._page.select_second_last_channel_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_last_channel_hotkey_validation_icon_appearance())
     
    def test_error_given_if_same_key_used_for_view_only_mode_hotkeys(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_view_only_mode_hotkey()
        second_key = self._page.get_selected_second_view_only_mode_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_view_only_mode_hotkey_validation_icon_appearance())
        self._page.select_second_view_only_mode_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_view_only_mode_hotkey_validation_icon_appearance())
     
    def test_error_given_if_same_key_used_for_shared_mode_hotkeys(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_shared_mode_hotkey()
        second_key = self._page.get_selected_second_shared_mode_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_shared_mode_hotkey_validation_icon_appearance())
        self._page.select_second_shared_mode_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_shared_mode_hotkey_validation_icon_appearance())
     
    def test_error_given_if_same_key_used_for_exclusive_mode_hotkeys(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_exclusive_mode_hotkey()
        second_key = self._page.get_selected_second_exclusive_mode_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_exclusive_mode_hotkey_validation_icon_appearance())
        self._page.select_second_exclusive_mode_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_exclusive_mode_hotkey_validation_icon_appearance())
     
    def test_error_given_if_same_key_used_for_disconnect_hotkeys(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        first_key = self._page.get_selected_first_disconnect_hotkey()
        second_key = self._page.get_selected_second_disconnect_hotkey()
        self.assertNotEqual(first_key, second_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_disconnect_hotkey_validation_icon_appearance())
        self._page.select_second_disconnect_hotkey(first_key)
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_disconnect_hotkey_validation_icon_appearance())
        
    """
    USB Settings Tests
    """
    def test_can_toggle_hid_only(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        current_setting = self._page.get_hid_only_setting()
        self._page.toggle_hid_only()
        self._page.click_save_usb_settings()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        new_setting = self._page.get_hid_only_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_hid_only()
        self._page.click_save_usb_settings()
    
    def test_can_toggle_disable_isochronous_endpoint_osd_alerts(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        current_setting = self._page.get_disable_isochronous_endpoint_osd_alerts_setting()
        self._page.toggle_disable_isochronous_endpoint_osd_alerts()
        self._page.click_save_usb_settings()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        new_setting = self._page.get_disable_isochronous_endpoint_osd_alerts_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_disable_isochronous_endpoint_osd_alerts()
        self._page.click_save_usb_settings()
        
    def test_can_toggle_enable_isochronous_endpoint_attach(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        current_setting = self._page.get_enable_isochronous_endpoint_attach_setting()
        self._page.toggle_enable_isochronous_endpoint_attach()
        self._page.click_save_usb_settings()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        new_setting = self._page.get_enable_isochronous_endpoint_attach_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_enable_isochronous_endpoint_attach()
        self._page.click_save_usb_settings()
        
    def test_can_change_port_reservation_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        current_setting = self._page.get_reserved_usb_port_setting()
        labels = self._page.get_reserved_usb_port_options()
        labels.remove("None")
        for label in labels:
            self._page.select_reserved_usb_port_by_label(label)
            self._page.click_save()
            self.assertEqual(self._page.get_current_reserved_usb_port_selection_text(), label)
            try:
                converted_label = str(int(label)+3)
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                page.click_dashboard_settings_link()
                page.click_receivers_settings_button()
                page.open_receiver_usb_settings()
                menus = page.get_list_of_port_reservation_dropdowns()
                for menu in menus:
                    page.select_port_reservation_label_by_element(menu, converted_label)
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                menus = page.get_list_of_port_reservation_dropdowns()
                for menu in menus:
                    self.assertEqual(page.get_current_global_receiver_reserved_usb_port_selection_text(menu), converted_label)
                    page.select_port_reservation_label_by_element(menu, "None")
                page.click_save_usb_settings()
            finally:
                page.driver.quit()
        self._page.select_reserved_usb_port_by_label(current_setting)
        self._page.click_save()
       
    def test_can_change_port_reservation_device(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        labels = self._page.get_list_of_reserved_devices(menus[0])
        labels.remove("Not Set")
        for label in labels:
            for counter in range(0, len(menus)):
                menus = self._page.get_list_of_port_reservation_device_dropdowns()
                self._page.select_port_reservation_device_label_by_element(menus[counter], label)
                self._page.click_save_usb_settings()
                self._page.open_receiver_usb_settings()
                menus = self._page.get_list_of_port_reservation_device_dropdowns()
                self.assertEqual(self._page.get_current_global_receiver_reserved_usb_port_device_selection_text(menus[0]), label)
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        for menu in menus:
            self._page.select_port_reservation_device_label_by_element(menu, "Not Set")
        self._page.click_save_usb_settings()
        
    def test_can_change_displayed_port_reservation_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        for counter in range(0, len(devices)):
            devices = self._page.get_list_usb_devices()
            devices.pop()
            menus = self._page.get_list_of_port_reservation_device_dropdowns()
            original_labels = self._page.get_list_of_reserved_devices(menus[0])
            self._page.toggle_hide_usb_device(devices[counter])
            self._page.click_save_features()
            self._page.open_receiver_usb_settings()
            self._page.show_advanced_usb_features()
            menus = self._page.get_list_of_port_reservation_device_dropdowns()
            new_labels = self._page.get_list_of_reserved_devices(menus[0])
            self.assertNotEqual(original_labels, new_labels)
            self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        for device in devices:
            self._page.toggle_hide_usb_device(device)
        self._page.click_save_features()
        
    def test_can_change_displayed_port_reservation_devices_via_global_toggle(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        original_labels = self._page.get_list_of_reserved_devices(menus[0])
        self._page.set_status_hide_usb_device_global(False)
        self._page.set_status_hide_usb_device_global(False)#twice as needed to deselect all
        for device in devices:
            self.assertFalse(self._page.check_show_status_of_usb_device(device))
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertNotEqual(original_labels, new_labels)
        self._page.show_advanced_usb_features()
        self._page.set_status_hide_usb_device_global(True)
        self._page.click_save_features()
           
    def test_can_change_displayed_port_reservation_devices_by_adding_test_device(self):
        test_name = "XX TEST name"
        test_desc = "XX TEST desc"
        test_kernel = "1234"
        test_user = "1234"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        original_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertFalse(test_name in original_labels)
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device(test_name, test_desc, test_kernel, test_user)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertNotEqual(original_labels, new_labels)
        self.assertTrue(test_name in new_labels)
        self._page.show_advanced_usb_features()
        self._page.delete_test_usb_device()
        self._page.click_save_features()
    
    def test_cannot_change_displayed_port_reservation_devices_with_incomplete_form(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device("", "", "", "")
        self._page.click_save_features()
        self.assertEqual("No changes made", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("", "XX TEST", "", "")
        self._page.click_save_features()
        self.assertEqual("No changes made", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("", "", "XX TEST", "")
        self._page.click_save_features()
        self.assertEqual("No changes made", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("", "", "", "XX TEST")
        self._page.click_save_features()
        self.assertEqual("No changes made", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "", "", "")
        self._page.click_save_features()
        self.assertEqual("Please ensure the form is completed correctly", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "", "")
        self._page.click_save_features()
        self.assertEqual("Please ensure the form is completed correctly", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "XX TEST", "")
        self._page.click_save_features()
        self.assertEqual("Please ensure the form is completed correctly", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "", "XX TEST")
        self._page.click_save_features()
        self.assertEqual("Please ensure the form is completed correctly", self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "XX TEST", "XX TEST")
        self._page.click_save_features()
        self.assertEqual("Please ensure the form is completed correctly", self._page.get_quirk_ajax_message_text())
  
    def test_can_change_displayed_port_reservation_devices_by_deleting_test_device(self):
        test_name = "XX TEST name"
        test_desc = "XX TEST desc"
        test_kernel = "1234"
        test_user = "1234"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device(test_name, test_desc, test_kernel, test_user)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertTrue(test_name in labels)
        self._page.show_advanced_usb_features()
        self._page.delete_test_usb_device()
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertFalse(test_name in new_labels)
        
    def test_can_change_port_reservation_merge(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        port_mergers = self._page.get_list_of_port_reservation_merge_checkboxes()
        for merger in port_mergers:
            state = self._page.get_port_merge_selector_state(merger)
            self._page.toggle_port_merge_state(merger)
            new_state = self._page.get_port_merge_selector_state(merger)
            self.assertNotEqual(state, new_state)
            self._page.toggle_port_merge_state(merger)
     
    def test_ensure_usb_devices_that_reject_merging_force_merge_to_disabled(self):
        disabled_device_names = ["Eizo CG276 screen", 
                                 "Eizo CX240 screen + Colormunki", 
                                 "Wacom Intuos4 tablet"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_receivers_settings_button()
        self._page.open_receiver_usb_settings()
        for device in disabled_device_names:
            merger = self._page.get_list_of_port_reservation_merge_checkboxes()[0]
            menu = self._page.get_list_of_port_reservation_device_dropdowns()[0]
            self._page.select_port_reservation_device_label_by_element(menu, "Not Set")
            state = self._page.get_port_merge_selector_state(merger)
            if not state:
                self._page.toggle_port_merge_state(merger)
                state = self._page.get_port_merge_selector_state(merger)
            self._page.select_port_reservation_device_label_by_element(menu, device)
            new_state = self._page.get_port_merge_selector_state(merger)
            self.assertNotEqual(state, new_state)
            self._page.click_save_usb_settings()
            self._page.open_receiver_usb_settings()
            merger = self._page.get_list_of_port_reservation_merge_checkboxes()[0]
            new_state = self._page.get_port_merge_selector_state(merger)
            self.assertNotEqual(state, new_state)
            self._page.toggle_port_merge_state(merger)
            self._page.click_save_usb_settings()
            self._page.open_receiver_usb_settings()
            merger = self._page.get_list_of_port_reservation_merge_checkboxes()[0]
            self.assertEqual(new_state, self._page.get_port_merge_selector_state(merger))
        menu = self._page.get_list_of_port_reservation_device_dropdowns()[0]
        self._page.select_port_reservation_device_label_by_element(menu, "Not Set")
        state = self._page.get_port_merge_selector_state(merger)
        if not state:
            self._page.toggle_port_merge_state(merger)
        self._page.click_save_usb_settings()    