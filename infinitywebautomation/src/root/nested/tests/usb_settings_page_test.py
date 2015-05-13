'''
Created on 17 Dec 2013

@author: Mark
'''
from root.nested.pages.home_page import HomePage
from root.nested.tests.base_infinity_regression_test import \
    BaseInfinityRegressionTest


class UsbSettingsPageTest(BaseInfinityRegressionTest):

    def test_can_open_usb_settings_page(self):
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual("USB Settings", usb_page.get_logo_text())
        self.assertEqual("USB Settings", usb_page.get_main_header_text())
    
    def test_can_enable_allow_human_interface_devices_only(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_allow_human_interface_devices_only_state())
        usb_page.set_allow_human_interface_devices_only_state(True)
        usb_page.update_config_form()
        self.assertTrue(usb_page.get_allow_human_interface_devices_only_state())
        usb_page.set_allow_human_interface_devices_only_state(False)
        usb_page.update_config_form()
        
    def test_can_disable_isochronous_endpoint_osd_alerts(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_isochronous_endpoint_osd_alerts_state())
        usb_page.set_isochronous_endpoint_osd_alert_state(False)
        usb_page.update_config_form()
        self.assertFalse(usb_page.get_isochronous_endpoint_osd_alerts_state())
        usb_page.set_isochronous_endpoint_osd_alert_state(True)
        usb_page.update_config_form()

    def test_can_enable_isochronous_endpoint_attach(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_isochronous_endpoint_attach_state())
        usb_page.set_isochronous_endpoint_attach_state(True)
        usb_page.update_config_form()
        self.assertTrue(usb_page.get_isochronous_endpoint_attach_state())
        usb_page.set_isochronous_endpoint_attach_state(False)
        usb_page.update_config_form()
    
    def test_default_states_of_port_reservation(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_merge_top_left_state())
        self.assertTrue(usb_page.get_merge_top_right_state())
        self.assertTrue(usb_page.get_merge_bottom_left_state())
        self.assertTrue(usb_page.get_merge_bottom_right_state())
        self.assertEqual(usb_page.get_map_top_left(), "None")
        self.assertEqual(usb_page.get_map_top_right(), "None")
        self.assertEqual(usb_page.get_map_bottom_left(), "None")
        self.assertEqual(usb_page.get_map_bottom_right(), "None")
    
    def test_can_disable_merge_top_left(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_merge_top_left_state())
        usb_page.set_merge_top_left_state(False)
        usb_page.update_config_form()
        self.assertFalse(usb_page.get_merge_top_left_state())
        usb_page.set_merge_top_left_state(True)
        usb_page.update_config_form()
    
    def test_can_disable_merge_top_right(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_merge_top_right_state())
        usb_page.set_merge_top_right_state(False)
        usb_page.update_config_form()
        self.assertFalse(usb_page.get_merge_top_right_state())
        usb_page.set_merge_top_right_state(True)
        usb_page.update_config_form()

    def test_can_disable_merge_bottom_left(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_merge_bottom_left_state())
        usb_page.set_merge_bottom_left_state(False)
        usb_page.update_config_form()
        self.assertFalse(usb_page.get_merge_bottom_left_state())
        usb_page.set_merge_bottom_left_state(True)
        usb_page.update_config_form()

    def test_can_disable_merge_bottom_right(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_merge_bottom_right_state())
        usb_page.set_merge_bottom_right_state(False)
        usb_page.update_config_form()
        self.assertFalse(usb_page.get_merge_bottom_right_state())
        usb_page.set_merge_bottom_right_state(True)
        usb_page.update_config_form()
    
    def test_can_change_map_top_left(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual(usb_page.get_map_top_left(), "None")
        for visible_text_option in usb_page.get_map_top_left_options():
            usb_page.set_map_top_left(visible_text_option)
            usb_page.update_config_form()
            self.assertEqual(usb_page.get_map_top_left(), visible_text_option)
        usb_page.set_map_top_left("None")
        usb_page.update_config_form()

    def test_can_change_map_top_right(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual(usb_page.get_map_top_right(), "None")
        for visible_text_option in usb_page.get_map_top_right_options():
            usb_page.set_map_top_right(visible_text_option)
            usb_page.update_config_form()
            self.assertEqual(usb_page.get_map_top_right(), visible_text_option)
        usb_page.set_map_top_right("None")
        usb_page.update_config_form()
            
    def test_can_change_map_bottom_left(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual(usb_page.get_map_bottom_left(), "None")
        for visible_text_option in usb_page.get_map_top_left_options():
            usb_page.set_map_bottom_left(visible_text_option)
            usb_page.update_config_form()
            self.assertEqual(usb_page.get_map_bottom_left(), visible_text_option)
        usb_page.set_map_bottom_left("None")
        usb_page.update_config_form()

    def test_can_change_map_bottom_right(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual(usb_page.get_map_bottom_right(), "None")
        for visible_text_option in usb_page.get_map_bottom_right_options():
            usb_page.set_map_bottom_right(visible_text_option)
            usb_page.update_config_form()
            self.assertEqual(usb_page.get_map_bottom_right(), visible_text_option)
        usb_page.set_map_bottom_right("None")
        usb_page.update_config_form()
    
    def test_advanced_features_disabled_by_default(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_enabled_advanced_features_state())
        self.assertFalse(usb_page.get_top_left_kernel_enabled())
        self.assertFalse(usb_page.get_top_left_user_enabled())
        self.assertFalse(usb_page.get_top_right_kernel_enabled())
        self.assertFalse(usb_page.get_top_right_user_enabled())
        self.assertFalse(usb_page.get_bottom_left_kernel_enabled())
        self.assertFalse(usb_page.get_bottom_left_user_enabled())
        self.assertFalse(usb_page.get_bottom_right_kernel_enabled())
        self.assertFalse(usb_page.get_bottom_right_user_enabled())
    
    def test_can_enable_advanced_features(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_enabled_advanced_features_state())
        usb_page.set_enabled_advanced_features_state(True)
        self.assertTrue(usb_page.get_enabled_advanced_features_state())
        self.assertTrue(usb_page.get_top_left_kernel_enabled())
        self.assertTrue(usb_page.get_top_left_user_enabled())
        self.assertTrue(usb_page.get_top_right_kernel_enabled())
        self.assertTrue(usb_page.get_top_right_user_enabled())
        self.assertTrue(usb_page.get_bottom_left_kernel_enabled())
        self.assertTrue(usb_page.get_bottom_left_user_enabled())
        self.assertTrue(usb_page.get_bottom_right_kernel_enabled())
        self.assertTrue(usb_page.get_bottom_right_user_enabled())
        usb_page.set_enabled_advanced_features_state(False)
        usb_page.update_config_form()
    
    def test_advanced_features_cannot_be_saved_without_hex_numbers(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_enabled_advanced_features_state())
        usb_page.set_enabled_advanced_features_state(True)
        usb_page.set_top_left_kernel_value("text")
        verification = usb_page.update_config_form()
        self.assertEqual(verification, "Unsupported data format for advanced feature setting")
    
    def test_all_advanced_features_will_accept_a_hex_number(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_enabled_advanced_features_state())
        usb_page.set_enabled_advanced_features_state(True)
        usb_page.set_top_left_kernel_value("0x1")
        usb_page.set_top_left_user_value("0x1")
        usb_page.set_bottom_left_kernel_value("0x1")
        usb_page.set_bottom_left_user_value("0x1")
        usb_page.set_top_right_kernel_value("0x1")
        usb_page.set_top_right_user_value("0x1")
        usb_page.set_bottom_right_kernel_value("0x1")
        usb_page.set_bottom_right_user_value("0x1")
        usb_page.update_config_form()
        self.assertEqual(usb_page.get_top_left_kernel_value(), "0x1")
        self.assertEqual(usb_page.get_top_left_user_value(), "0x1")
        self.assertEqual(usb_page.get_bottom_left_kernel_value(), "0x1")
        self.assertEqual(usb_page.get_bottom_left_user_value(), "0x1")
        self.assertEqual(usb_page.get_top_right_kernel_value(), "0x1")
        self.assertEqual(usb_page.get_top_right_user_value(), "0x1")
        self.assertEqual(usb_page.get_bottom_right_kernel_value(), "0x1")
        self.assertEqual(usb_page.get_bottom_right_user_value(), "0x1")
        usb_page.set_enabled_advanced_features_state(False)
        usb_page.update_config_form()
    
    def test_can_disable_dummy_boot_keyboard(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertTrue(usb_page.get_enable_dummy_boot_keyboard_state())
        usb_page.set_enable_dummy_boot_keyboard_state(False)
        usb_page.update_config_form()
        self.assertFalse(usb_page.get_enable_dummy_boot_keyboard_state())
        usb_page.set_enable_dummy_boot_keyboard_state(True)
        usb_page.update_config_form()
        
    def test_can_enable_disable_hi_speed(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertFalse(usb_page.get_disable_hi_speed_state())
        usb_page.set_disable_hi_speed_state(True)
        usb_page.update_config_form()
        self.assertTrue(usb_page.get_disable_hi_speed_state())
        usb_page.set_disable_hi_speed_state(False)
        usb_page.update_config_form()
    
    def test_can_change_hub_size(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual(usb_page.get_selected_hub_size_option(), "13")
        options = usb_page.get_hub_size_options()
        counter = 0
        for counter in range(len(options)):
            options = usb_page.get_hub_size_options()
            usb_page.set_hub_size_option(options[counter])
            usb_page.update_config_form()
            self.assertEqual(usb_page.get_selected_hub_size_option(), options[counter])
        usb_page.set_hub_size_option("13")
        usb_page.update_config_form()
    
    def test_can_change_reserved_port_range(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        usb_page = home_page.open_usb_settings_page()
        self.assertEqual(usb_page.get_selected_reserved_port_range_option(), "0")
        options = usb_page.get_reserved_port_range_options()
        counter = 0
        for counter in range(len(options)):
            options = usb_page.get_reserved_port_range_options()
            usb_page.set_reserved_port_range_option(options[counter])
            usb_page.update_config_form()
            self.assertEqual(usb_page.get_selected_reserved_port_range_option(), options[counter])
        usb_page.set_reserved_port_range_option("0")
        usb_page.update_config_form()