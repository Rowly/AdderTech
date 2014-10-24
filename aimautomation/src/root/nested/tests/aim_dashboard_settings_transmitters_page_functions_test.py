'''
Created on 10 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.tests.base_aim_regression_test import unittest
from root.nested.services.parameters import parameter_singleton

class AimDashboardSettingsTransmittersPageFunctionsTest(BaseAimRegressionTest):
    
    def test_can_change_magic_eye(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_magic_eye_options()
        for label in labels:
            self._page.select_magic_eye_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_magic_eye_selection_text(), label)
        self._page.select_magic_eye_by_label("Off")
        self._page.click_save()

    def test_can_change_ddc(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_ddc_options()
        for label in labels:
            self._page.select_ddc_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_ddc_selection_text(), label)
        self._page.select_ddc_by_label("USE CONNECTED MONITOR'S DDC")
        self._page.click_save()

    def test_can_change_hot_plug_detect_control(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_hot_plug_detect_control_options()
        for label in labels:
            self._page.select_hot_plug_detect_control_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_hot_plug_detect_control_selection_text(), label)
        self._page.select_hot_plug_detect_control_by_label("On")
        self._page.click_save()

    def test_can_change_hot_plug_detect_signal_period(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_hot_plug_detect_signal_period_options()
        for label in labels:
            self._page.select_hot_plug_detect_signal_period_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_hot_plug_detect_signal_period_selection_text(), label)
        self._page.select_hot_plug_detect_signal_period_by_label("Default - 25ms")
        self._page.click_save()

    def test_can_change_background_refresh(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_background_refresh_options()
        for label in labels:
            self._page.select_background_refresh_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_background_refresh_selection_text(), label)
        self._page.select_background_refresh_by_label("Every 32 frames")
        self._page.click_save()

    def test_can_change_colour_depth(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            raise unittest.SkipTest("Colour Depth removed in v3.3")    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_colour_depth_options()
        for label in labels:
            self._page.select_colour_depth_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_colour_depth_selection_text(), label)
        self._page.select_colour_depth_by_label("24 bit")
        self._page.click_save()
    
    def test_can_change_compression_level(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_compression_level_options()
        labels.remove("Advanced")
        for label in labels:
            self._page.select_compression_level_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_compression_level_selection_text(), label)
        self._page.select_compression_level_by_label("Pixel Perfect")
        self._page.click_save()
    
    def test_can_change_compression_level_advanced(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        self._page.select_compression_level_by_label("Advanced")
        self._page.select_compression_minimum_by_label("1")
        self._page.select_compression_maximum_by_label("1")
        self._page.click_save()
        self.assertEqual(self._page.get_current_compression_level_selection_text(), "Pixel Perfect")
        self._page.select_compression_level_by_label("Advanced")
        self._page.select_compression_minimum_by_label("4")
        self._page.select_compression_maximum_by_label("4")
        self._page.click_save()
        self.assertEqual(self._page.get_current_compression_level_selection_text(), "Smoothest Video")
        self._page.select_compression_level_by_label("Advanced")
        self._page.select_compression_minimum_by_label("2")
        self._page.select_compression_maximum_by_label("2")
        self._page.click_save()
        self.assertEqual(self._page.get_current_compression_level_selection_text(), "Advanced")
        self._page.select_compression_level_by_label("Pixel Perfect")
        self._page.click_save()
    
    def test_can_toggle_usd_speed(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        current_setting = self._page.get_usb_speed_setting()
        self._page.toggle_usb_speed()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        new_setting = self._page.get_usb_speed_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_usb_speed()
        self._page.click_save()

    def test_can_toggle_usd_hub_size(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        current_setting = self._page.get_usb_hub_size_setting()
        self._page.toggle_usb_hub_size()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        new_setting = self._page.get_usb_hub_size_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_usb_hub_size()
        self._page.click_save()

    def test_can_toggle_enable_dummy_boot_keyboard(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        current_setting = self._page.get_enable_dummy_boot_keyboard_setting()
        self._page.toggle_enable_dummy_boot_keyboard()
        self._page.click_save()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        new_setting = self._page.get_enable_dummy_boot_keyboard_setting()
        self.assertNotEqual(current_setting, new_setting)
        self._page.toggle_enable_dummy_boot_keyboard()
        self._page.click_save()
    
    def test_can_change_reserved_USB_ports(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        current_setting = self._page.get_reserved_usb_port_setting()
        labels = self._page.get_reserved_usb_port_options()
        for label in labels:
            self._page.select_reserved_usb_port_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_reserved_usb_port_selection_text(), label)
        self._page.select_reserved_usb_port_by_label(current_setting)
        self._page.click_save()
    
    def test_can_change_serial_parity(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_serial_parity_options()
        for label in labels:
            self._page.select_serial_parity_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_serial_parity_selection_text(), label)
        self._page.select_serial_parity_by_label("N (None)")
        self._page.click_save()

    def test_can_change_serial_data_bits(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_serial_data_bits_options()
        for label in labels:
            self._page.select_serial_data_bits_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_serial_data_bits_selection_text(), label)
        self._page.select_serial_data_bits_by_label("8")
        self._page.click_save()

    def test_can_change_serial_stop_bits(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_serial_stop_bits_options()
        for label in labels:
            self._page.select_serial_stop_bits_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_serial_stop_bits_selection_text(), label)
        self._page.select_serial_stop_bits_by_label("1")
        self._page.click_save()

    def test_can_change_serial_speed(self):    
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_serial_speed_options()
        for label in labels:
            self._page.select_serial_speed_by_label(label)
            self._page.click_save()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_current_serial_speed_selection_text(), label)
        self._page.select_serial_speed_by_label("115200")
        self._page.click_save()