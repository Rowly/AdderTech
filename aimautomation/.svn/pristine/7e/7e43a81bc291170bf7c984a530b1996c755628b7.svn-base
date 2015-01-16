'''
Created on 14 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
import re

class AimTransmitterConfigPageDefaultsTest(BaseAimRegressionTest):

    def test_device_id_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        device_id = self._page.get_device_id_from_row_id(self._page.get_row_id_of_transmitter(transmitter))
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_device_id_from_config_page(), device_id)

    def test_online_status_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_online_img_src_from_config_page(), self._baseurl + "/admin/images/silk_icons/tick.png")
    
    def test_date_added_is_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        date_added = self._page.get_date_added_from_config_page()
        match = re.search(r"[0-9]{2}:[0-9]{2}:[0-9]{2} [0-9]{2}/[0-9]{2}/[0-9]{2}", date_added)
        self.assertTrue(match)
        
    def test_mac_address_is_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        mac_address = self._page.get_mac_address_from_config_page()
        match = re.search(r"[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}:[0-9A-Fa-f]{2}", mac_address)
        self.assertTrue(match)
    
    def test_main_firmware_is_shown_and_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        firmware = self._page.get_main_firmware_from_config_page()
        self.assertNotEqual(firmware, "")
    
    def test_backup_firmware_is_shown_and_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        firmware = self._page.get_backup_firmware_from_config_page()
        self.assertNotEqual(firmware, "")
    
    def test_ip_address_is_shown_and_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        ip = self._page.get_ip_address_from_config_page()
        self.assertNotEqual(ip, "")
        match = re.search(r"[0-9]+.[0-9]+.[0-9]+.[0-9]+", ip)
        self.assertTrue(match)
    
    def test_ip_address_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_ip_help_text_from_config_page(), "Changing the IP address will end any connections")
    
    def test_dummy_keyboard_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_dummy_keyboard_default_correct())
    
    def test_dummy_keyboard_radio_buttons_correct_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_label_of_dummy_keyboard_radio_one(), "Global Setting")
        self.assertEqual(self._page.get_label_of_dummy_keyboard_radio_two(), "No")
        self.assertEqual(self._page.get_label_of_dummy_keyboard_radio_three(), "Yes")
    
    def test_dummy_keyboard_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_dummy_keyboard_help_text_from_config_page(), "Present a dummy keyboard for booting")
    
    def test_usb_speed_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_usb_speed_default_correct())
        
    def test_usb_speed_radio_buttons_correct_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_label_of_usb_speed_radio_one(), "Global Setting")
        self.assertEqual(self._page.get_label_of_usb_speed_radio_two(), "USB 2 Hi-Speed")
        self.assertEqual(self._page.get_label_of_usb_speed_radio_three(), "USB 1 Full Speed")
    
    def test_usb_speed_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_usb_speed_help_text_from_config_page(), "Limit USB to 12 Mbits/s?")
    
    def test_usb_hub_size_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_usb_hub_default_correct())
    
    def test_usb_hub_size_radio_buttons_correct_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_label_of_usb_hub_radio_one(), "Global Setting")
        self.assertEqual(self._page.get_label_of_usb_hub_radio_two(), "13")
        self.assertEqual(self._page.get_label_of_usb_hub_radio_three(), "7")
    
    def test_usb_hub_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_usb_hub_help_text_from_config_page(), "Limit number of USB devices that can be connected via a hub")
    
    def test_peak_bandwidth_limiter_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_bandwidth_limit_from_config_page(), "95%")
       
    def test_video_settings_DDC_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_DDC_setting_from_config_page_correct())
    
    def test_video_setting_DDC_menu_has_all_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_ddc_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_ddc_option_label("0"), "USE CONNECTED MONITOR'S DDC")
        self.assertEqual(self._page.get_ddc_option_label("1"), "GENERIC 4:3")
        self.assertEqual(self._page.get_ddc_option_label("2"), "GENERIC 16:10")
        self.assertEqual(self._page.get_ddc_option_label("3"), "GENERIC 16:9")
        self.assertEqual(self._page.get_ddc_option_label("4"), "GENERIC LOW")
        self.assertEqual(self._page.get_ddc_option_label("7"), "640x480 VGA")
        self.assertEqual(self._page.get_ddc_option_label("8"), "720x480 NTSC")
        self.assertEqual(self._page.get_ddc_option_label("9"), "768x576 PAL")
        self.assertEqual(self._page.get_ddc_option_label("10"), "800x480 WVGA")
        self.assertEqual(self._page.get_ddc_option_label("11"), "800x600 SVGA")
        self.assertEqual(self._page.get_ddc_option_label("13"), "1024x600 WSVGA")
        self.assertEqual(self._page.get_ddc_option_label("14"), "1024x768 XGA")
        self.assertEqual(self._page.get_ddc_option_label("15"), "1152x768")
        self.assertEqual(self._page.get_ddc_option_label("40"), "1152x864")
        self.assertEqual(self._page.get_ddc_option_label("16"), "1280x720 HD720")
        self.assertEqual(self._page.get_ddc_option_label("17"), "1280x768 WXGA")
        self.assertEqual(self._page.get_ddc_option_label("18"), "1280x800 WXGA")
        self.assertEqual(self._page.get_ddc_option_label("19"), "1280x854")
        self.assertEqual(self._page.get_ddc_option_label("20"), "1280x960")
        self.assertEqual(self._page.get_ddc_option_label("21"), "1280x1024 SXGA")
        self.assertEqual(self._page.get_ddc_option_label("22"), "1366x768")
        self.assertEqual(self._page.get_ddc_option_label("23"), "1400x1050+ XSGA")
        self.assertEqual(self._page.get_ddc_option_label("24"), "1440x900")
        self.assertEqual(self._page.get_ddc_option_label("25"), "1440x960")
        self.assertEqual(self._page.get_ddc_option_label("30"), "1600x900")
        self.assertEqual(self._page.get_ddc_option_label("26"), "1600x1200 UXGA")
        self.assertEqual(self._page.get_ddc_option_label("27"), "1680x1050+ WSXGA")
        self.assertEqual(self._page.get_ddc_option_label("28"), "1920x1080 HD1080")
        self.assertEqual(self._page.get_ddc_option_label("29"), "1920x1200 WUXGA")
        self.assertEqual(self._page.get_ddc_option_label("31"), "2048x768")
        self.assertEqual(self._page.get_ddc_option_label("34"), "2048x1080")
        self.assertEqual(self._page.get_ddc_option_label("35"), "2048x1152")
    
    def test_video_setting_DDC_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_ddc_help_text_from_config_page(), "Use the DDC selected here, or else use the DDC of the monitor connected to the receiver")
    
    def test_hot_plug_detect_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_hot_plug_setting_from_config_page_correct())
    
    def test_hot_plug_detect_has_correct_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_hot_plug_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_hot_plug_option_label("1"), "On")
        self.assertEqual(self._page.get_hot_plug_option_label("0"), "Off")
    
    def test_hot_plug_signal_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_hot_plug_signal_setting_from_config_page_correct())

    def test_hot_plug_signal_has_correct_valuess(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_hot_plug_signal_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_hot_plug_signal_option_label("23000"), "Monitor - 25ms")
        self.assertEqual(self._page.get_hot_plug_signal_option_label("0"), "Minimum - less than 10ms")
        self.assertEqual(self._page.get_hot_plug_signal_option_label("100000"), "Default - 100ms")
        self.assertEqual(self._page.get_hot_plug_signal_option_label("200000"), "Legacy - 200ms")
        self.assertEqual(self._page.get_hot_plug_signal_option_label("1000000"), "Very long - 1000ms")
#         self.assertEqual(self._page.get_hot_plug_signal_option_label("-1"), "USE GLOBAL SETTING")
#         self.assertEqual(self._page.get_hot_plug_signal_option_label("23000"), "Default - 25ms")
#         self.assertEqual(self._page.get_hot_plug_signal_option_label("0"), "Minimum - less than 10ms")
#         self.assertEqual(self._page.get_hot_plug_signal_option_label("100000"), "Repeater - 100ms")
#         self.assertEqual(self._page.get_hot_plug_signal_option_label("200000"), "Legacy - 200ms")
#         self.assertEqual(self._page.get_hot_plug_signal_option_label("1000000"), "Very long - 1000ms")

    def test_hot_plug_signal_help_text_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_hot_plug_signal_help_text_from_config_page(), "Use the hot plug detect signal period timing selected here")
    
    def test_background_refresh_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_back_ground_refresh_setting_from_config_page_correct())
    
    def test_background_refresh_has_correct_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_background_refresh_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_background_refresh_option_label("32"), "Every 32 frames")
        self.assertEqual(self._page.get_background_refresh_option_label("64"), "Every 64 frames")
        self.assertEqual(self._page.get_background_refresh_option_label("128"), "Every 128 frames")
        self.assertEqual(self._page.get_background_refresh_option_label("256"), "Every 256 frames")
        self.assertEqual(self._page.get_background_refresh_option_label("0"), "Disabled")
    
    def test_colour_depth_default_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_colour_depth_setting_from_config_page_correct())
    
    def test_colour_depth_values_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_colour_depth_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_colour_depth_option_label("8"), "8 bit")
        self.assertEqual(self._page.get_colour_depth_option_label("16"), "16 bit")
        self.assertEqual(self._page.get_colour_depth_option_label("24"), "24 bit")
    
    def test_frame_skipping_slider_ranger_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_frame_skipping_label_from_config_page(), "0%")
    
    def test_serial_parity_setting_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_serial_parity_setting_from_config_page_correct())
    
    def test_serial_parity_setting_values_are_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_serial_parity_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_serial_parity_option_label("N"), "N (None)")
        self.assertEqual(self._page.get_serial_parity_option_label("E"), "E (Even)")
        self.assertEqual(self._page.get_serial_parity_option_label("O"), "O (Odd)")

    def test_serial_data_setting_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_serial_data_setting_from_config_page_correct())
    
    def test_serial_data_setting_values_are_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_serial_data_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_serial_data_option_label("5"), "5")
        self.assertEqual(self._page.get_serial_data_option_label("6"), "6")
        self.assertEqual(self._page.get_serial_data_option_label("7"), "7")
        self.assertEqual(self._page.get_serial_data_option_label("8"), "8")

    def test_serial_stop_setting_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_serial_stop_setting_from_config_page_correct())
    
    def test_serial_stop_setting_values_are_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_serial_stop_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_serial_stop_option_label("1"), "1")
        self.assertEqual(self._page.get_serial_stop_option_label("2"), "2")

    def test_serial_speed_setting_default_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertTrue(self._page.ensure_selected_serial_speed_setting_from_config_page_correct())
    
    def test_serial_speed_setting_values_are_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[-1]
        self._page.click_transmitter_configure(transmitter)
        self.assertEqual(self._page.get_serial_speed_option_label("-1"), "USE GLOBAL SETTING")
        self.assertEqual(self._page.get_serial_speed_option_label("9600"), "9600")
        self.assertEqual(self._page.get_serial_speed_option_label("19200"), "19200")
        self.assertEqual(self._page.get_serial_speed_option_label("38400"), "38400")
        self.assertEqual(self._page.get_serial_speed_option_label("57600"), "57600")
        self.assertEqual(self._page.get_serial_speed_option_label("115200"), "115200")