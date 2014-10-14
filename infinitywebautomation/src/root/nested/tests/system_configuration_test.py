'''
Created on 12 Nov 2013

@author: Mark
'''
import time
from root.nested.tests.base_infinity_regression_test import unittest
from root.nested.tests.base_infinity_regression_test import BaseInfinityRegressionTest
from root.nested.pages.home_page import HomePage
from root.nested.services.parameters import parameter_singleton

class SystemConfigurationTest(BaseInfinityRegressionTest):
    
    def test_can_open_system_configuration_settings_page(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual("System Configuration", config_page.get_logo_text())
        self.assertEqual("System Configuration", config_page.get_main_header_text())
                      
    def test_can_change_unit_name(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        original_name = config_page.get_unit_name()
        self.assertEqual(original_name, "Name")
        config_page.set_unit_name("%s edit" %original_name)
        config_page.update_config_form()
        editted_name = config_page.get_unit_name()
        self.assertNotEqual(original_name, editted_name)
        config_page.set_unit_name(original_name)
        config_page.update_config_form()
              
    def test_can_change_unit_description(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        original_description = config_page.get_unit_description()
        self.assertEqual(original_description, "Description")
        config_page.set_unit_description("%s edit" %original_description)
        config_page.update_config_form()
        editted_description = config_page.get_unit_description()
        self.assertNotEqual(original_description, editted_description)
        config_page.set_unit_description(original_description)
        config_page.update_config_form()
                     
    def test_cannot_change_system_ip_to_invalid(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_system_ip(), self._ip)
        for ip in self._invalid_ips:
            config_page.set_unit_system_ip(ip)
            verification = config_page.update_config_form()
            self.assertEqual(verification, "Error: Invalid System IP Address.")
            config_page.dismiss_alert_if_present()
            
    def test_cannot_change_system_netmask_to_invalid(self):
        if self._ip.startswith("169.254"):
            netmask = "255.255.0.0"
        if self._ip.startswith("192.168"):
            netmask = "255.255.255.0"
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_system_netmask(), netmask)
        for mask in self._invalid_netmasks:
            config_page.set_unit_system_netmask(mask)
            verification = config_page.update_config_form()
            self.assertEqual(verification, "Error: Invalid System Netmask.")
            config_page.dismiss_alert_if_present()
            
    def test_cannot_change_system_gateway_to_invalid(self):
        if self._ip.startswith("169.254"):
            gateway = "169.254.1.1"
        if self._ip.startswith("192.168"):
            gateway = "192.168.1.1"
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_system_gateway(), gateway)
        for ip in self._invalid_ips:
            config_page.set_unit_system_gateway(ip)
            verification = config_page.update_config_form()
            self.assertEqual(verification, "Error: Invalid Gateway.")
            config_page.dismiss_alert_if_present()
               
    def test_can_disable_management_port(self):
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_management_port_state())
        config_page.set_enable_management_port_state(False)
        config_page.update_config_form_that_starts_reboot(self._base_url)
        self.assertFalse(config_page.get_enable_management_port_state())
        config_page.set_enable_management_port_state(True)
        config_page.update_config_form_that_starts_reboot(self._base_url)
               
    def test_cannot_change_management_port_ip_address_to_invalid(self):
        self.check_device_is_dual()
        if self._device != "TX2v":
            error_text = "Error: Invalid Management Port IP Address."
        if self._device == "TX2v":
            error_text = "Error: Invalid VNC Port IP Address."
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_management_port_ip(), "192.168.1.42")
        for ip in self._invalid_ips:
            config_page.set_unit_management_port_ip(ip)
            verification = config_page.update_config_form()
            self.assertEqual(verification, error_text)
            config_page.dismiss_alert_if_present()
               
    def test_cannot_change_management_port_netmask_to_invalid(self):
        self.check_device_is_dual()
        if self._device != "TX2v":
            error_text = "Error: Invalid Management Port Netmask."
        if self._device == "TX2v":
            error_text = "Error: Invalid VNC Port Netmask."
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_management_port_netmask(), "255.255.0.0")
        for mask in self._invalid_netmasks:
            config_page.set_unit_management_port_netmask(mask)
            verification = config_page.update_config_form()
            self.assertEqual(verification, error_text)
            config_page.dismiss_alert_if_present()
               
    def test_cannot_change_management_port_gateway_to_invalid(self):
        self.check_device_is_dual()
        if self._device != "TX2v":
            error_text = "Error: Invalid Management Port Gateway."
        if self._device == "TX2v":
            error_text = "Error: Invalid VNC Port Gateway."
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_management_port_gateway(), "192.168.1.1")
        for ip in self._invalid_ips:
            config_page.set_unit_management_port_gateway(ip)
            verification = config_page.update_config_form()
            self.assertEqual(verification, error_text)
            config_page.dismiss_alert_if_present()
               
    def test_can_disable_teaming_port(self):
        self.check_device_is_rx2_rx2s_tx2_tx2b_tx2v()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_teaming_port_state())
        config_page.set_enable_teaming_port_state(False)
        config_page.update_config_form_that_starts_reboot(self._base_url)
        self.assertFalse(config_page.get_enable_teaming_port_state())
        config_page.set_enable_teaming_port_state(True)
        config_page.update_config_form_that_starts_reboot(self._base_url)
               
    def test_cannot_change_teaming_port_ip_address_to_invalid(self):
        self.check_device_is_rx2_rx2s_tx2_tx2b_tx2v()
        if self._ip.startswith("169.254"):
            expected = "169.254"
        if self._ip.startswith("192.168"):
            expected = "192.168"
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_unit_teaming_port_ip().startswith(expected))
        for ip in self._invalid_ips:
            config_page.set_unit_teaming_port_ip(ip)
            verification = config_page.update_config_form()
            self.assertEqual(verification, "Error: Invalid Teaming Port IP Address.")
            config_page.dismiss_alert_if_present()
               
    def test_cannot_change_teaming_port_netmask_to_invalid(self):
        self.check_device_is_rx2_rx2s_tx2_tx2b_tx2v()
        if self._ip.startswith("169.254"):
            netmask = "255.255.0.0"
        if self._ip.startswith("192.168"):
            netmask = "255.255.255.0"
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_teaming_port_netmask(), netmask)
        for mask in self._invalid_netmasks:
            config_page.set_unit_teaming_port_netmask(mask)
            verification = config_page.update_config_form()
            self.assertEqual(verification, "Error: Invalid Teaming Port Netmask.")
            config_page.dismiss_alert_if_present()
               
    def test_cannot_change_teaming_port_gateway_to_invalid(self):
        self.check_device_is_rx2_rx2s_tx2_tx2b_tx2v()
        if self._ip.startswith("169.254"):
            gateway = "169.254.1.1"
        if self._ip.startswith("192.168"):
            gateway = "192.168.1.1"
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_unit_teaming_port_gateway(), gateway)
        for ip in self._invalid_ips:
            config_page.set_unit_teaming_port_gateway(ip)
            verification = config_page.update_config_form()
            self.assertEqual(verification, "Error: Invalid Teaming Port Gateway.")
            config_page.dismiss_alert_if_present()
               
    def test_can_disable_dvi_d1(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_dvi_d1_state())
        config_page.set_enable_dvi_d1_state(False)
        config_page.update_config_form()
        self.assertFalse(config_page.get_enable_dvi_d1_state())
        config_page.set_enable_dvi_d1_state(True)
        config_page.update_config_form()
           
    def test_can_disable_dvi_d2(self):
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_dvi_d2_state())
        config_page.set_enable_dvi_d2_state(False)
        config_page.update_config_form()
        self.assertFalse(config_page.get_enable_dvi_d2_state())
        config_page.set_enable_dvi_d2_state(True)
        config_page.update_config_form()
           
    def test_can_disable_audio(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_audio_state())
        config_page.set_enable_audio_state(False)
        config_page.update_config_form()
        self.assertFalse(config_page.get_enable_audio_state())
        config_page.set_enable_audio_state(True)
        config_page.update_config_form()
               
    def test_can_disable_usb(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_usb_state())
        config_page.set_enable_usb_state(False)
        config_page.update_config_form()
        self.assertFalse(config_page.get_enable_usb_state())
        config_page.set_enable_usb_state(True)
        config_page.update_config_form()
  
    def test_can_enable_serial(self):
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_serial_state())
        config_page.set_enable_serial_state(True)
        config_page.update_config_form()
        self.assertTrue(config_page.get_enable_serial_state())
        config_page.set_enable_serial_state(False)
        config_page.update_config_form()
           
    def test_can_disable_osd_alerts(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_enable_osd_alerts_state())
        config_page.set_enable_osd_alerts_state(False)
        config_page.update_config_form()
        self.assertFalse(config_page.get_enable_osd_alerts_state())
        config_page.set_enable_osd_alerts_state(True)
        config_page.update_config_form()
               
    def test_can_change_keyboard_country_code(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        default_code = config_page.get_selected_keyboard_country_code()
        codes = config_page.get_all_keyboard_country_codes()
        for code in codes:
            config_page.select_keyboard_country_code(code)
            config_page.update_config_form()
            self.assertEqual(code, config_page.get_selected_keyboard_country_code())
        config_page.select_keyboard_country_code(default_code)
        config_page.update_config_form()
               
    def test_can_change_audio_input_type(self):
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_audio_mic_state())
        self.assertFalse(config_page.get_audio_mic_boost_state())
        config_page.set_audio_mic_state(False)
        config_page.set_audio_mic_boost_state(True)
        config_page.update_config_form()
        self.assertFalse(config_page.get_audio_mic_state())
        self.assertTrue(config_page.get_audio_mic_boost_state())
        config_page.set_audio_mic_state(True)
        config_page.set_audio_mic_boost_state(False)
        config_page.update_config_form()
               
    def test_can_enable_video_compatibility_check_for_dvi_d1(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_video_compatibility_for_dvi_d1_state())
        config_page.set_video_compatibility_for_dvi_d1_state(True)
        config_page.update_config_form()
        self.assertTrue(config_page.get_video_compatibility_for_dvi_d1_state())
        config_page.set_video_compatibility_for_dvi_d1_state(False)
        config_page.update_config_form()
           
    def test_can_enable_video_compatibility_check_for_dvi_d2(self):
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_video_compatibility_for_dvi_d2_state())
        config_page.set_video_compatibility_for_dvi_d2_state(True)
        config_page.update_config_form()
        self.assertTrue(config_page.get_video_compatibility_for_dvi_d2_state())
        config_page.set_video_compatibility_for_dvi_d2_state(False)
        config_page.update_config_form()
     
    def test_can_enable_force_video_refresh_rate_for_dvi_d1(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            self.check_device_is_rx2_or_rx2s()
            home_page = HomePage(self._driver, self._wait)
            config_page = home_page.open_system_configuration_page()
            self.assertFalse(config_page.get_force_video_refresh_rate_for_dvi_d1_state())
            config_page.set_force_video_refresh_rate_for_dvi_d1_state(True)
            config_page.update_config_form()
            self.assertTrue(config_page.get_force_video_refresh_rate_for_dvi_d1_state())
            config_page.set_force_video_refresh_rate_for_dvi_d1_state(False)
            config_page.update_config_form()
 
    def test_can_enable_force_video_refresh_rate_for_dvi_d2(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            self.check_device_is_rx2()
            home_page = HomePage(self._driver, self._wait)
            config_page = home_page.open_system_configuration_page()
            self.assertFalse(config_page.get_force_video_refresh_rate_for_dvi_d2_state())
            config_page.set_force_video_refresh_rate_for_dvi_d2_state(True)
            config_page.update_config_form()
            self.assertTrue(config_page.get_force_video_refresh_rate_for_dvi_d2_state())
            config_page.set_force_video_refresh_rate_for_dvi_d2_state(False)
            config_page.update_config_form()
     
    def test_can_change_video_switching_mode_for_dvi_d1(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            self.check_device_is_rx2_or_rx2s()
            home_page = HomePage(self._driver, self._wait)
            config_page = home_page.open_system_configuration_page()
            self.assertTrue(config_page.get_video_switching_mode_for_dvi_d1_fast_switching_mode_state())
            config_page.set_video_switching_mode_for_dvi_d1_to_match_frame_rate()
            config_page.update_config_form()
            self.assertTrue(config_page.get_video_switching_mode_for_dvi_d1_match_frame_rate_mode_state())
            config_page.set_video_switching_mode_for_dvi_d1_to_fast_switching()
            config_page.update_config_form()
 
    def test_can_change_video_switching_mode_for_dvi_d2(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            self.check_device_is_rx2()
            home_page = HomePage(self._driver, self._wait)
            config_page = home_page.open_system_configuration_page()
            self.assertTrue(config_page.get_video_switching_mode_for_dvi_d2_fast_switching_mode_state())
            config_page.set_video_switching_mode_for_dvi_d2_to_match_frame_rate()
            config_page.update_config_form()
            self.assertTrue(config_page.get_video_switching_mode_for_dvi_d2_match_frame_rate_mode_state())
            config_page.set_video_switching_mode_for_dvi_d2_to_fast_switching()
            config_page.update_config_form()
               
    def test_can_short_identify_unit(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Identify changed in v3.2")
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        counter_before = config_page.get_identify_counter(self._base_url)
        config_page.click_short_identify()
        counter_after = config_page.get_identify_counter(self._base_url) 
        self.assertNotEqual(counter_before, counter_after)
         
    def test_can_long_identify_unit(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Identify changed in v3.2")
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        counter_before = config_page.get_identify_counter(self._base_url)
        config_page.click_long_identify()
        counter_after = config_page.get_identify_counter(self._base_url)
        self.assertNotEqual(counter_before, counter_after)
        config_page.click_short_identify()
          
    def test_can_change_serial_baud_rate(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_selected_serial_baud_rate(), "115200")
        options = config_page.get_serial_baud_rate_options()
        counter = 0
        for counter in range(len(options)):
            options = config_page.get_serial_baud_rate_options()
            config_page.set_serial_baud_rate_option(options[counter])
            config_page.update_config_form()
            self.assertEquals(config_page.get_selected_serial_baud_rate(), options[counter])
        config_page.set_serial_baud_rate_option("115200")
        config_page.update_config_form()
      
    def test_can_change_serial_data_bit(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_selected_serial_data_bit(), "8")
        options = config_page.get_serial_data_bit_options()
        counter = 0
        for counter in range(len(options)):
            options = config_page.get_serial_data_bit_options()
            config_page.set_serial_data_bit_option(options[counter])
            config_page.update_config_form()
            self.assertEqual(config_page.get_selected_serial_data_bit(), options[counter])
        config_page.set_serial_data_bit_option("8")
        config_page.update_config_form()
      
    def test_can_change_serial_stop_bit(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_selected_serial_stop_bit(), "1")
        options = config_page.get_serial_stop_bit_options()
        counter = 0
        for counter in range(len(options)):
            options = config_page.get_serial_stop_bit_options()
            config_page.set_serial_stop_bit_option(options[counter])
            config_page.update_config_form()
            self.assertEqual(config_page.get_selected_serial_stop_bit(), options[counter])
        config_page.set_serial_stop_bit_option("1")
        config_page.update_config_form() 
          
    def test_can_change_serial_parity(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertEqual(config_page.get_selected_serial_parity(), "None")
        options = config_page.get_serial_parity_options()
        counter = 0
        for counter in range(len(options)):
            options = config_page.get_serial_parity_options()
            config_page.set_serial_parity_option(options[counter])
            config_page.update_config_form()
            self.assertEqual(config_page.get_selected_serial_parity(), options[counter])
        config_page.set_serial_parity_option("None")
        config_page.update_config_form()
   
    def test_target_transmitter_default_settings_correct(self):
        self.check_device_is_receiver()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_target_transmitter_ip_address() != None)
           
    def test_target_transmitter_default_settings_correct_for_rx2(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()     
        self.assertTrue(config_page.get_target_transmitter_ip_address_eth2() != None)
          
    def test_target_transmitter_disable_use_eth2(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertTrue(config_page.get_target_transmitter_use_eth2_for_audio_state())
        config_page.set_target_transmitter_use_eth2_state(False)
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_audio_state())
        config_page.update_rx_config_form()
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_audio_state())
        config_page.set_target_transmitter_use_eth2_state(True)
        config_page.set_target_transmitter_ip_address_eth2("169.254.1.43")
        config_page.update_rx_config_form()
          
    def test_target_transmiter_can_reveal_advanced_settings(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) <= 3 and int(split_version[1]) < 2:
            self.assertFalse(config_page.get_visibility_target_transmitter_use_eth2_for_dvi_d1())
            self.assertFalse(config_page.get_visibility_target_transmitter_use_eth2_for_dvi_d2())
            self.assertFalse(config_page.get_visibility_target_transmitter_use_eth2_for_audio())
            self.assertFalse(config_page.get_visibility_target_transmitter_use_eth2_for_usb())
            self.assertFalse(config_page.get_visibility_target_transmitter_use_eth2_for_serial())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_for_dvi_d1())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_2_for_dvi_d1())
        self.assertFalse(config_page.get_visibility_target_transmitter_video_no_for_dvi_d1())
        if self._device == "RX2":
            self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_for_dvi_d2())
            self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_2_for_dvi_d2())
            self.assertFalse(config_page.get_visibility_target_transmitter_video_no_for_dvi_d2())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_for_audio())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_2_for_audio())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_for_usb())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_2_for_usb())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_for_serial())
        self.assertFalse(config_page.get_visibility_target_transmitter_ip_address_2_for_serial())
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_for_dvi_d1())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_2_for_dvi_d1())
        self.assertTrue(config_page.get_visibility_target_transmitter_video_no_for_dvi_d1())
        if self._device == "RX2":
            self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_for_dvi_d2())
            self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_2_for_dvi_d2())
            self.assertTrue(config_page.get_visibility_target_transmitter_video_no_for_dvi_d2())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_for_audio())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_2_for_audio())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_for_usb())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_2_for_usb())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_for_serial())
        self.assertTrue(config_page.get_visibility_target_transmitter_ip_address_2_for_serial())
        if int(split_version[0]) <= 3 and int(split_version[1]) < 2:
            self.assertTrue(config_page.get_visibility_target_transmitter_use_eth2_for_dvi_d1())
            self.assertTrue(config_page.get_visibility_target_transmitter_use_eth2_for_dvi_d2())
            self.assertTrue(config_page.get_visibility_target_transmitter_use_eth2_for_audio())
            self.assertTrue(config_page.get_visibility_target_transmitter_use_eth2_for_usb())
            self.assertTrue(config_page.get_visibility_target_transmitter_use_eth2_for_serial())
          
    def test_target_transmitter_ip_address_for_dvi_d1_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_for_dvi_d1() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_for_dvi_d1(ip)
            verification = config_page.update_rx_config_form()
            if self._device == "RX2":
                self.assertEqual(verification, "Error: Invalid IP Address for DVI-D-1")
            if self._device == "RX2s":
                self.assertEqual(verification, "Error: Invalid Video IP Address")
            config_page.dismiss_alert_if_present()
          
    def test_target_transmitter_ip_address_2_for_dvi_d1_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_2_for_dvi_d1() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_2_for_dvi_d1(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid IP Address 2 for DVI-D-1")
            config_page.dismiss_alert_if_present()
         
    def test_target_transmitter_video_no_for_dvi_d1_can_be_changed(self):
        self.check_for_phantomjs()
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertEqual(config_page.get_selected_target_transmitter_video_no_for_dvi_d1(), "DVI-D-1")
        config_page.set_target_transmitter_video_no_for_dvi_d1("DVI-D-2")
        config_page.update_rx_config_form()
        time.sleep(2)
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertEqual(config_page.get_selected_target_transmitter_video_no_for_dvi_d1(), "DVI-D-2")
        config_page.set_target_transmitter_video_no_for_dvi_d1("DVI-D-1")
        config_page.update_rx_config_form()
         
    def test_target_transmitter_use_eth2_for_dvi_d1_can_be_disabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_use_eth2_for_dvi_d1_state())
        config_page.set_target_transmitter_use_eth2_for_dvi_d1_state(False)
        config_page.update_rx_config_form()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_dvi_d1_state())
        config_page.set_target_transmitter_use_eth2_for_dvi_d1_state(True)
        config_page.set_target_transmitter_ip_address_2_for_dvi_d1("169.254.1.43")
        config_page.update_rx_config_form()
         
    def test_target_transmitter_ip_address_for_dvi_d2_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_for_dvi_d2() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_for_dvi_d2(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid IP Address for DVI-D-2")
            config_page.dismiss_alert_if_present()
         
    def test_target_transmitter_ip_address_2_for_dvi_d2_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_2_for_dvi_d2() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_2_for_dvi_d2(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid IP Address 2 for DVI-D-2")
            config_page.dismiss_alert_if_present()
             
    def test_target_transmitter_video_no_for_dvi_d2_can_be_changed(self):
        self.check_for_phantomjs()
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertEqual(config_page.get_selected_target_transmitter_video_no_for_dvi_d2(), "DVI-D-2")
        config_page.set_target_transmitter_video_no_for_dvi_d2("DVI-D-1")
        config_page.update_rx_config_form()
        time.sleep(2)
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertEqual(config_page.get_selected_target_transmitter_video_no_for_dvi_d2(), "DVI-D-1")
        config_page.set_target_transmitter_video_no_for_dvi_d2("DVI-D-2")
        config_page.update_rx_config_form()
         
    def test_target_transmitter_use_eth2_for_dvi_d2_can_be_disabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_use_eth2_for_dvi_d2_state())
        config_page.set_target_transmitter_use_eth2_for_dvi_d2_state(False)
        config_page.update_rx_config_form()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_dvi_d2_state())
        config_page.set_target_transmitter_use_eth2_for_dvi_d2_state(True)
        config_page.set_target_transmitter_ip_address_2_for_dvi_d2("169.254.1.43")
        config_page.update_rx_config_form()
        
    def test_target_transmitter_audio_ip_address_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_for_audio() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_for_audio(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid Audio IP Address")
            config_page.dismiss_alert_if_present()
    
    def test_target_transmitter_audio_ip_address_2_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_2_for_audio() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_2_for_audio(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid Audio IP Address 2")
            config_page.dismiss_alert_if_present()
        
    def test_target_transmitter_use_eth2_for_audio_can_be_disabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_use_eth2_for_audio_state())
        config_page.set_target_transmitter_use_eth2_for_audio_state(False)
        config_page.update_rx_config_form()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_audio_state())
        config_page.set_target_transmitter_use_eth2_for_audio_state(True)
        config_page.set_target_transmitter_ip_address_2_for_audio("169.254.1.43")
        config_page.update_rx_config_form()
    
    def test_target_transmitter_usb_ip_address_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_for_usb() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_for_usb(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid USB IP Address")
            config_page.dismiss_alert_if_present()
    
    def test_target_transmitter_usb_ip_address_2_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_2_for_usb() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_2_for_usb(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid USB IP Address 2")
            config_page.dismiss_alert_if_present()
        
    def test_target_transmitter_use_eth2_for_usb_can_be_disabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_use_eth2_for_usb_state())
        config_page.set_target_transmitter_use_eth2_for_usb_state(False)
        config_page.update_rx_config_form()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_usb_state())
        config_page.set_target_transmitter_use_eth2_for_usb_state(True)
        config_page.set_target_transmitter_ip_address_2_for_usb("169.254.1.43")
        config_page.update_rx_config_form()
    
    def test_target_transmitter_serial_ip_address_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_for_serial() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_for_serial(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid Serial IP Address")
            config_page.dismiss_alert_if_present()
    
    def test_target_transmitter_serial_ip_address_2_cannot_be_set_to_invalid(self):
        self.check_device_is_rx2_or_rx2s()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_ip_address_2_for_serial() != None)
        for ip in self._invalid_ips:
            config_page.click_show_advanced_target_transmitter_settings_button()
            config_page.set_target_transmitter_ip_address_2_for_serial(ip)
            verification = config_page.update_rx_config_form()
            self.assertEqual(verification, "Error: Invalid Serial IP Address 2")
            config_page.dismiss_alert_if_present()
        
    def test_target_transmitter_use_eth2_for_serial_can_be_disabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertTrue(config_page.get_target_transmitter_use_eth2_for_serial_state())
        config_page.set_target_transmitter_use_eth2_for_serial_state(False)
        config_page.update_rx_config_form()
        config_page.click_show_advanced_target_transmitter_settings_button()
        self.assertFalse(config_page.get_target_transmitter_use_eth2_for_serial_state())
        config_page.set_target_transmitter_use_eth2_for_serial_state(True)
        config_page.set_target_transmitter_ip_address_2_for_serial("169.254.1.43")
        config_page.update_rx_config_form()
   
    def test_multicast_can_enable_multicast_dvi_d1(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_dvi_d1_state())
        config_page.set_enable_multicast_dvi_d1_state(True)
        config_page.set_dvi_d1_multicast_ip_address("224.0.0.1")
        config_page.set_dvi_d1_multicast_ip_address_2("224.0.0.2")
        config_page.update_multicast_config_form()
        self.assertTrue(config_page.get_enable_multicast_dvi_d1_state())
        config_page.set_enable_multicast_dvi_d1_state(False)
        config_page.update_multicast_config_form()
        
    def test_multicast_dvi_d1_ip_address_cannot_be_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_dvi_d1_state())
        config_page.set_enable_multicast_dvi_d1_state(True)
        config_page.set_dvi_d1_multicast_ip_address_2("224.0.0.2")
        for ip in self._invalid_ips:
            config_page.set_dvi_d1_multicast_ip_address(ip)
            verification = config_page.update_multicast_config_form()
            self.assertEqual(verification, "Error: Video 1 multicast IP address incorrect")
            config_page.dismiss_alert_if_present()
        
    def test_multicast_dvi_d1_ip_address_2_cannot_be_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_dvi_d1_state())
        config_page.set_enable_multicast_dvi_d1_state(True)
        config_page.set_dvi_d1_multicast_ip_address("224.0.0.2")
        for ip in self._invalid_ips:
            config_page.set_dvi_d1_multicast_ip_address_2(ip)
            verification = config_page.update_multicast_config_form()
            self.assertEqual(verification, "Error: Video 1 multicast IP address 2 incorrect")
            config_page.dismiss_alert_if_present()
    
    def test_multicast_can_enable_multicast_dvi_d2(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_dvi_d2_state())
        config_page.set_enable_multicast_dvi_d2_state(True)
        config_page.set_dvi_d2_multicast_ip_address("224.0.0.1")
        config_page.set_dvi_d2_multicast_ip_address_2("224.0.0.2")
        config_page.update_multicast_config_form()
        self.assertTrue(config_page.get_enable_multicast_dvi_d2_state())
        config_page.set_enable_multicast_dvi_d2_state(False)
        config_page.update_multicast_config_form()
        
    def test_multicast_dvi_d2_ip_address_cannot_be_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_dvi_d2_state())
        config_page.set_enable_multicast_dvi_d2_state(True)
        config_page.set_dvi_d2_multicast_ip_address_2("224.0.0.2")
        for ip in self._invalid_ips:
            config_page.set_dvi_d2_multicast_ip_address(ip)
            verification = config_page.update_multicast_config_form()
            self.assertEqual(verification, "Error: Video 2 multicast IP address incorrect")
            config_page.dismiss_alert_if_present()
        
    def test_multicast_dvi_d2_ip_address_2_cannot_be_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_dvi_d2_state())
        config_page.set_enable_multicast_dvi_d2_state(True)
        config_page.set_dvi_d2_multicast_ip_address("224.0.0.2")
        for ip in self._invalid_ips:
            config_page.set_dvi_d2_multicast_ip_address_2(ip)
            verification = config_page.update_multicast_config_form()
            self.assertEqual(verification, "Error: Video 2 multicast IP address 2 incorrect")
            config_page.dismiss_alert_if_present()
    
    def test_multicast_can_enable_multicast_audio(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_audio_state())
        config_page.set_enable_multicast_audio_state(True)
        config_page.set_audio_multicast_ip_address("224.0.0.1")
        config_page.set_audio_multicast_ip_address_2("224.0.0.2")
        config_page.update_multicast_config_form()
        self.assertTrue(config_page.get_enable_multicast_audio_state())
        config_page.set_enable_multicast_audio_state(False)
        config_page.update_multicast_config_form()
        
    def test_multicast_audio_ip_address_cannot_be_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_audio_state())
        config_page.set_enable_multicast_audio_state(True)
        config_page.set_audio_multicast_ip_address_2("224.0.0.2")
        for ip in self._invalid_ips:
            config_page.set_audio_multicast_ip_address(ip)
            verification = config_page.update_multicast_config_form()
            self.assertEqual(verification, "Error: Audio multicast IP address incorrect")
            config_page.dismiss_alert_if_present()
        
    def test_multicast_audio_ip_address_2_cannot_be_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Changed in v3.2")
        self.check_device_is_rx2()
        home_page = HomePage(self._driver, self._wait)
        config_page = home_page.open_system_configuration_page()
        self.assertFalse(config_page.get_enable_multicast_audio_state())
        config_page.set_enable_multicast_audio_state(True)
        config_page.set_audio_multicast_ip_address("224.0.0.2")
        for ip in self._invalid_ips:
            config_page.set_audio_multicast_ip_address_2(ip)
            verification = config_page.update_multicast_config_form()
            self.assertEqual(verification, "Error: Audio multicast IP address 2 incorrect")
            config_page.dismiss_alert_if_present()