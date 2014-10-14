'''
Created on 12 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage

class AimReceiverGroupConfigFunctionsTest(BaseAimRegressionTest):
    
    def test_change_receiver_group_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                index = groups.index(group)
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                name = page.get_receiver_group_name_from_config_page()
                page.set_receiver_group_name_via_config_page("%s edit"%name)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                new_group = page.get_list_of_receiver_groups()[index]
                new_name = page.get_receiver_group_name(new_group)
                self.assertEqual(new_name, "%s edit"%name)
                page.driver.get(link_text)
                page.set_receiver_group_name_via_config_page(name)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
        finally:
            page.driver.quit()
       
    def test_can_change_receiver_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                index = groups.index(group)
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                description = page.get_receiver_group_description_from_config_page()
                page.set_receiver_group_description_via_config_page("%s edit"%description)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                new_group = page.get_list_of_receiver_groups()[index]
                new_description = page.get_receiver_group_description(new_group)
                self.assertEqual(new_description, "%s edit"%description)
                page.driver.get(link_text)
                page.set_receiver_group_description_via_config_page(description)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
        finally:
            page.driver.quit()
        
       
    def test_can_change_login_required(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for grooup in groups:
                link_text = self._page.get_receiver_group_config_linktext(grooup)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.select_receiver_group_login_required_no()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Login Required", "rg_login_required_0"))
                page.select_receiver_group_login_required_yes()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Login Required", "rg_login_required_1"))
                page.select_receiver_group_login_required_global()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Login Required", "rg_login_required_-1"))
        finally:
            page.driver.quit()
   
    def test_can_change_enable_receiver_osd_alerts(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.select_receiver_group_osd_alerts_no()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_0"))
                page.select_receiver_group_osd_alerts_yes()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_1"))
                page.select_receiver_group_osd_alerts_global()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_-1"))
        finally:
            page.driver.quit()
   
   
    def test_can_change_enable_video_compatibility_check(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.select_receiver_group_video_compatibility_no()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_0"))
                page.select_receiver_group_video_compatibility_yes()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_1"))
                page.select_receiver_group_video_compatibility_global()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_-1"))
        finally:
            page.driver.quit()
       
    def test_can_change_which_receivers_are_member_of_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.remove_all_member_receivers_from_receiver_group()
                recevier_name = page.get_first_receiver_name_from_add_select()
                page.add_member_receiver_to_receiver_group(recevier_name)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.driver.get(link_text)
                self.assertTrue(page.check_receiver_name_is_member_of_receiver_group(recevier_name))
                page.remove_all_member_receivers_from_receiver_group()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
        finally:
            page.driver.quit()
       
    def test_can_change_receiver_group_users(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receivers()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.show_user_permissions()
                name = page.get_first_user_name_from_add_select()
                page.add_user_to_receiver_group(name)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                page.show_user_permissions()
                self.assertTrue(page.check_user_has_receiver_group_permission(name))
                page.remove_all_users_from_receiver_group()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
        finally:
            page.driver.quit()    
   
    def test_can_change_receiver_group_user_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receivers()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.show_user_permissions()
                name = page.get_first_user_group_name_from_add_select()
                page.add_user_group_to_receiver_group(name)
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
                page.driver.get(link_text)
                page.show_user_permissions()
                self.assertTrue(page.check_user_group_has_receiver_group_permission(name))
                page.remove_all_user_groups_from_receiver_group()
                page.click_save()
                page.check_for_error_message("configure_receiver_group_ajax_message")
                page.confirm_no_longer_on_receiver_group_config_page()
        finally:
            page.driver.quit()    
  
  
    """
    USB Settings Tests
    """
    def test_can_change_hid_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.open_receiver_usb_settings()
                page.select_receiver_group_HID_connection_no()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("HID Only", "hid_only_0"))
                page.select_receiver_group_HID_connection_yes()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("HID Only", "hid_only_1"))
                page.select_receiver_group_HID_connection_global()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("HID Only", "hid_only_-1"))
        finally:
            page.driver.quit()
 
    def test_can_change_disable_isochronous_endpoint_osd_alerts(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.open_receiver_usb_settings()
                page.select_receiver_group_disable_isochronous_endpoint_osd_alerts_no()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_0"))
                page.select_receiver_group_disable_isochronous_endpoint_osd_alerts_yes()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_1"))
                page.select_receiver_group_disable_isochronous_endpoint_osd_alerts_global()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Disable Isochronous Endpoint OSD Alerts", "isochronous_user_warning_-1"))
        finally:
            page.driver.quit()
 
    def test_can_change_enable_isochronous_endpoint_attach(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for group in groups:
                link_text = self._page.get_receiver_group_config_linktext(group)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Receiver Groups > Configure Receiver Group")
                page.open_receiver_usb_settings()
                page.select_receiver_group_enable_isochronous_endpoint_attach_no()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_0"))
                page.select_receiver_group_enable_isochronous_endpoint_attach_yes()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_1"))
                page.select_receiver_group_enable_isochronous_endpoint_attach_global()
                page.click_save_usb_settings()
                page.check_for_error_message("usb_settings_ajax_message")
                page.open_receiver_usb_settings()
                self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Isochronous Endpoint Attach", "isochronous_enabled_-1"))
        finally:
            page.driver.quit()

    def test_can_change_port_reservation_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        current_setting = self._page.get_reserved_usb_port_setting()
        labels = self._page.get_reserved_usb_port_options()
        labels.remove("None")
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for label in labels:
                self._page.select_reserved_usb_port_by_label(label)
                self._page.click_save()
                self.assertEqual(self._page.get_current_reserved_usb_port_selection_text(), label)
                converted_label = str(int(label)+3)
                page.open_receivers_tab()
                page.open_view_receiver_groups_page()
                group = page.get_list_of_receiver_groups()[0]
                page.click_receiver_group_config(group)
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
                    page.select_port_reservation_label_by_element(menu, "Inherited")
                page.click_save_usb_settings()
        finally:
            page.driver.quit()
        self._page.select_reserved_usb_port_by_label(current_setting)
        self._page.click_save()
     
    def test_can_change_port_reservation_device(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        menus = self._page.get_list_of_port_reservation_device_dropdowns()
        labels = self._page.get_list_of_reserved_devices(menus[0])
        labels.remove("Not Set")
        labels.remove("Inherited")
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
            self._page.select_port_reservation_device_label_by_element(menu, "Inherited")
        self._page.click_save_usb_settings()
           
    def test_can_change_displayed_port_reservation_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
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
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
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
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
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
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
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
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
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
         
