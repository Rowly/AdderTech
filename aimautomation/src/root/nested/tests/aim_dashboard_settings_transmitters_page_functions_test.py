'''
Created on 10 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimDashboardSettingsTransmittersPageFunctionsTest(BaseAimRegressionTest):

    def test_can_change_magic_eye(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        self.assertEqual(self._page.get_slected_global_magic_eye(), "Off")
        for label in self._page.get_global_magic_eye_options():
            self._page.select_global_magic_eye_by_text(label)
            self._page.click_save()
            self.assertEqual(self._page.get_slected_global_magic_eye(), label)
        self._page.select_global_magic_eye_by_text("Off")
        self._page.click_save()
        self.assertEqual(self._page.get_slected_global_magic_eye(), "Off")

    def test_can_change_ddc(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        self.assertEqual(self._page.get_selected_global_ddc(),
                         "USE CONNECTED MONITOR'S DDC")
        for label in self._page.get_global_ddc_options():
            self._page.select_global_ddc_by_text(label)
            self._page.click_transmitters_settings_button()
            self.assertEqual(self._page.get_selected_global_ddc(), label)
        self._page.select_global_ddc_by_text("USE CONNECTED MONITOR'S DDC")
        self._page.click_save()
        self.assertEqual(self._page.get_selected_global_ddc(),
                         "USE CONNECTED MONITOR'S DDC")

    def test_can_change_hot_plug_detect_control(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_hot_plug_detect_control()
        self.assertEqual(selected, "On")
        labels = self._page.get_global_hot_plug_detect_control_options()
        for label in labels:
            self._page.select_global_hot_plug_detect_control_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_hot_plug_detect_control()
            self.assertEqual(selected, label)
        self._page.select_global_hot_plug_detect_control_by_text("On")
        self._page.click_save()
        selected = self._page.get_selected_global_hot_plug_detect_control()
        self.assertEqual(selected, "On")

    def test_can_change_hot_plug_detect_signal_period(self):
        default = "Default - 100ms"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_hot_plug_detect_period()
        self.assertEqual(selected, default)
        labels = self._page.get_global_hot_plug_detect_signal_period_options()
        for label in labels:
            self._page.select_global_hot_plug_detect_signal_period(label)
            self._page.click_save()
            selected = self._page.get_selected_global_hot_plug_detect_period()
            self.assertEqual(selected, label)
        self._page.select_global_hot_plug_detect_signal_period(default)
        self._page.click_save()
        selected = self._page.get_selected_global_hot_plug_detect_period()
        self.assertEqual(selected, default)

    def test_can_change_background_refresh(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_background_refresh()
        self.assertEqual(selected, "Every 32 frames")
        for label in self._page.get_global_background_refresh_options():
            self._page.select_global_background_refresh_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_background_refresh()
            self.assertEqual(selected, label)
        self._page.select_global_background_refresh_by_text("Every 32 frames")
        self._page.click_save()
        selected = self._page.get_selected_global_background_refresh()
        self.assertEqual(selected, "Every 32 frames")

    def test_can_change_compression_level(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_compression_level()
        self.assertEqual(selected, "Pixel Perfect")
        labels = self._page.get_global_compression_level_options()
        labels.remove("Advanced")
        for label in labels:
            self._page.select_global_compression_level_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_compression_level()
            self.assertEqual(selected, label)
        self._page.select_global_compression_level_by_text("Pixel Perfect")
        self._page.click_save()
        selected = self._page.get_selected_global_compression_level()
        self.assertEqual(selected, "Pixel Perfect")

    def test_can_change_compression_level_advanced(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        self._page.select_global_compression_level_by_text("Advanced")
        self._page.select_global_compression_minimum_by_text("1")
        self._page.select_global_compression_maximum_by_text("1")
        self._page.click_save()
        selected = self._page.get_selected_global_compression_level()
        self.assertEqual(selected, "Pixel Perfect")
        self._page.select_global_compression_level_by_text("Advanced")
        self._page.select_global_compression_minimum_by_text("4")
        self._page.select_global_compression_maximum_by_text("4")
        self._page.click_save()
        selected = self._page.get_selected_global_compression_level()
        self.assertEqual(selected, "Smoothest Video")
        self._page.select_global_compression_level_by_text("Advanced")
        self._page.select_global_compression_minimum_by_text("2")
        self._page.select_global_compression_maximum_by_text("2")
        self._page.click_save()
        selected = self._page.get_selected_global_compression_level()
        self.assertEqual(selected, "Advanced")
        self._page.select_global_compression_level_by_text("Pixel Perfect")
        self._page.click_save()

    def test_can_toggle_usd_speed(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        self.assertTrue(self._page.get_global_usb_speed_setting("hi_speed"))
        self._page.set_state_global_usb_speed_full_speed(True)
        self._page.click_save()
        self.assertTrue(self._page.get_global_usb_speed_setting("full_speed"))
        self._page.set_state_global_usb_speed_hi_speed(True)
        self._page.click_save()
        self.assertTrue(self._page.get_global_usb_speed_setting("hi_speed"))

    def test_can_toggle_usd_hub_size(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        self.assertTrue(self._page.get_global_usb_hub_size_setting("13"))
        self._page.set_state_global_usb_hub_size_7(True)
        self._page.click_save()
        self.assertTrue(self._page.get_global_usb_hub_size_setting("7"))
        self._page.set_state_global_usb_hub_size_13(True)
        self._page.click_save()
        self.assertTrue(self._page.get_global_usb_hub_size_setting("13"))

    def test_can_toggle_enable_dummy_boot_keyboard(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        state = self._page.get_global_enable_dummy_boot_keyboard_setting("yes")
        self.assertTrue(state)
        self._page.set_state_global_dummy_keyboard_no(True)
        self._page.click_save()
        state = self._page.get_global_enable_dummy_boot_keyboard_setting("no")
        self.assertTrue(state)
        self._page.set_state_global_dummy_keyboard_yes(True)
        self._page.click_save()
        state = self._page.get_global_enable_dummy_boot_keyboard_setting("yes")
        self.assertTrue(state)

    def test_can_change_reserved_USB_ports(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_global_reserved_usb_port_setting()
        self.assertEqual(selected, "None")
        for label in self._page.get_global_reserved_usb_port_options():
            self._page.select_global_reserved_usb_port_by_text(label)
            self._page.click_save()
            selected = self._page.get_global_reserved_usb_port_setting()
            self.assertEqual(selected, label)
        self._page.select_global_reserved_usb_port_by_text("None")
        self._page.click_save()
        selected = self._page.get_global_reserved_usb_port_setting()
        self.assertEqual(selected, "None")

    def test_can_change_serial_parity(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_serial_parity()
        self.assertEqual(selected, "N (None)")
        for label in self._page.get_global_serial_parity_options():
            self._page.select_global_serial_parity_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_serial_parity()
            self.assertEqual(selected, label)
        self._page.select_global_serial_parity_by_text("N (None)")
        self._page.click_save()
        selected = self._page.get_selected_global_serial_parity()
        self.assertEqual(selected, "N (None)")

    def test_can_change_serial_data_bits(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_serial_data_bits()
        self.assertEqual(selected, "8")
        for label in self._page.get_global_serial_data_bits_options():
            self._page.select_global_serial_data_bits_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_serial_data_bits()
            self.assertEqual(selected, label)
        self._page.select_global_serial_data_bits_by_text("8")
        self._page.click_save()
        selected = self._page.get_selected_global_serial_data_bits()
        self.assertEqual(selected, "8")

    def test_can_change_serial_stop_bits(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_serial_stop_bits()
        self.assertEqual(selected, "1")
        for label in self._page.get_global_serial_stop_bits_options():
            self._page.select_global_serial_stop_bits_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_serial_stop_bits()
            self.assertEqual(selected, label)
        self._page.select_global_serial_stop_bits_by_text("1")
        self._page.click_save()
        selected = self._page.get_selected_global_serial_stop_bits()
        self.assertEqual(selected, "1")

    def test_can_change_serial_speed(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        selected = self._page.get_selected_global_serial_speed()
        self.assertEqual(selected, "115200")
        for label in self._page.get_global_serial_speed_options():
            self._page.select_global_serial_speed_by_text(label)
            self._page.click_save()
            selected = self._page.get_selected_global_serial_speed()
            self.assertEqual(selected, label)
        self._page.select_global_serial_speed_by_text("115200")
        self._page.click_save()
        selected = self._page.get_selected_global_serial_speed()
        self.assertEqual(selected, "115200")
