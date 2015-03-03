'''
Created on 14 May 2013

@author: Mark.rowlands
'''
import re
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimTransmitterConfigPageDefaultsTest(BaseAimRegressionTest):

    def test_device_id_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        row_id = self._page.get_row_id_of_transmitter(transmitter)
        device_id = self._page.get_device_id_from_row_id(row_id)
        self._page.click_transmitter_configure(transmitter)
        id_ = self._page.get_device_id_from_config_page()
        self.assertEqual(id_, device_id)

    def test_online_status_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(self._page.get_online_img_src_from_config_page(),
                         self._silk_dir + "tick.png")

    def test_date_added_is_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        date_added = self._page.get_date_added_from_config_page()
        pattern = r"[0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{2}/[0-9]{2}/[0-9]{2}"
        match = re.search(pattern, date_added)
        self.assertTrue(match)

    def test_mac_address_is_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        mac_address = self._page.get_mac_address_from_config_page()
        pattern = (r"[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:" +
                    "[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}")
        match = re.search(pattern, mac_address)
        self.assertTrue(match)

    def test_main_firmware_is_shown_and_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        firmware = self._page.get_main_firmware_from_config_page()
        self.assertNotEqual(firmware, "")

    def test_backup_firmware_is_shown_and_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        firmware = self._page.get_backup_firmware_from_config_page()
        self.assertNotEqual(firmware, "")

    def test_ip_address_is_shown_and_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        ip = self._page.get_ip_address_from_config_page()
        self.assertNotEqual(ip, "")
        match = re.search(r"[0-9]+.[0-9]+.[0-9]+.[0-9]+", ip)
        self.assertTrue(match)

    def test_ip_address_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        text = self._page.get_ip_help_text_from_config_page()
        self.assertEqual(text, "Changing the IP address will " +
                               "end any connections")

    def test_dummy_keyboard_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        text = self._page.get_dummy_keyboard_help_text_from_config_page()
        self.assertEqual(text, "Present a dummy keyboard for booting")

    def test_usb_speed_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        text = self._page.get_usb_speed_help_text_from_config_page()
        self.assertEqual(text, "Limit USB to 12 Mbits/s?")

    def test_usb_hub_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        text = self._page.get_usb_hub_help_text_from_config_page()
        self.assertEqual(text, "Limit number of USB devices that " +
                               "can be connected via a hub")

    def test_peak_bandwidth_limiter_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        label = self._page.get_bandwidth_limit_from_config_page()
        self.assertEqual(label, "95%")

    def test_video_setting_DDC_menu_has_all_values(self):
        sl_validation = ["USE GLOBAL SETTING", "USE CONNECTED MONITOR'S DDC",
                         "GENERIC 4:3", "GENERIC 16:10", "GENERIC 16:9",
                         "GENERIC LOW", "640x480 VGA", "720x480 NTSC",
                         "768x576 PAL", "800x480 WVGA", "800x600 SVGA",
                         "1024x600 WSVGA", "1024x768 XGA", "1152x768",
                         "1152x864", "1280x720 HD720", "1280x768 WXGA",
                         "1280x800 WXGA", "1280x854", "1280x960",
                         "1280x1024 SXGA", "1366x768", "1400x1050+ XSGA",
                         "1440x900", "1440x960", "1600x900",
                         "1600x1200 UXGA", "1680x1050+ WSXGA", "1920x540@60",
                         "1920x1080 HD1080", "1920x1200 WUXGA", "2048x768",
                         "2048x1080", "2048x1152"]
        dl_validation = ["USE GLOBAL SETTING", "USE CONNECTED MONITOR'S DDC",
                         "GENERIC 4:3", "GENERIC 16:10", "GENERIC 16:9",
                         "GENERIC LOW", "640x480 VGA", "720x480 NTSC",
                         "768x576 PAL", "800x480 WVGA", "800x600 SVGA",
                         "1024x600 WSVGA", "1024x768 XGA", "1152x768",
                         "1152x864", "1280x720 HD720", "1280x768 WXGA",
                         "1280x800 WXGA", "1280x854", "1280x960",
                         "1280x1024 SXGA", "1366x768", "1400x1050+ XSGA",
                         "1440x900", "1440x960", "1600x900",
                         "1600x1200 UXGA", "1680x1050+ WSXGA", "1920x540@60",
                         "1920x1080 HD1080", "1920x1200 WUXGA", "2048x768",
                         "2048x1080", "2048x1152", "1920x1440 (Dual Link)",
                         "2048x1536 (Dual Link)", "2048x2048 (Dual Link)",
                         "2560x1080 (Dual Link)", "2560x1440 (Dual Link)",
                         "2560x1600 (Dual Link)", "2560x2048@50 (Dual Link)"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        if self.get_validation_set_via_device_info():
            validation = dl_validation
        else:
            validation = sl_validation
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_ddc_options())

    def test_video_setting_DDC_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        text = self._page.get_ddc_help_text_from_config_page()
        self.assertEqual(text, "Use the DDC selected here, or else use " +
                               "the DDC of the monitor connected to the " +
                               "receiver")

    def test_hot_plug_detect_has_correct_values(self):
        validation = ["USE GLOBAL SETTING", "On", "Off"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_hot_plug_detect_options())

    def test_hot_plug_signal_has_correct_values(self):
        validation = ["USE GLOBAL SETTING", "Default - 100ms",
                      "Minimum - less than 10ms", "Monitor - 25ms",
                      "Legacy - 200ms", "Very long - 1000ms"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_hot_plug_period_options())

    def test_hot_plug_signal_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        text = self._page.get_hot_plug_signal_help_text_from_config_page()
        self.assertEqual(text, "Use the hot plug detect signal period " +
                               "timing selected here")

    def test_background_refresh_has_correct_values(self):
        validation = ["USE GLOBAL SETTING", "Every 32 frames",
                      "Every 64 frames", "Every 128 frames",
                      "Every 256 frames", "Disabled"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        options = self._page.get_background_refresh_period_options()
        self.assertEqual(validation, options)

    def test_frame_skipping_slider_ranger_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        label = self._page.get_frame_skipping_label_from_config_page()
        self.assertEqual(label, "0%")

    def test_serial_parity_setting_values_are_correct(self):
        validation = ["USE GLOBAL SETTING", "N (None)", "E (Even)", "O (Odd)"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_serial_parity_options())

    def test_serial_data_setting_values_are_correct(self):
        validation = ["USE GLOBAL SETTING", "5", "6", "7", "8"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_serial_data_bit_options())

    def test_serial_stop_setting_values_are_correct(self):
        validation = ["USE GLOBAL SETTING", "1", "2"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_serial_data_stop_options())

    def test_serial_speed_setting_values_are_correct(self):
        validation = ["USE GLOBAL SETTING", "1200", "9600", "19200", "38400",
                      "57600", "115200"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.open_transmitter_config_page_for_tx_under_test()
        self.assertEqual(validation, self._page.get_serial_speed_options())

    """
    Utils
    """
    def get_validation_set_via_device_info(self):
        transmitters = self._page.get_list_of_transmitters()
        device_info = self._page.get_device_version_via_api()
        row_id = self._page.get_row_id_of_transmitter(transmitters[0])
        device_id = self._page.get_device_id_from_row_id(row_id)
        return device_info[device_id] == "2"

    def open_transmitter_config_page_for_tx_under_test(self):
        transmitter = self._page.get_list_of_transmitters()[0]
        self._page.click_transmitter_configure(transmitter)
