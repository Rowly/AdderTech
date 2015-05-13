'''
Created on 12 Nov 2013

@author: Mark
'''
import re
import time
from root.nested.pages.base_page import BasePage
from root.nested.services.telnet_service import TelnetService


class SystemConfigurationPage(BasePage):

    def get_unit_name(self):
        patj = "#webui_unit_name"
        return self.get_attribute_of_element_via_css(patj, "value")

    def set_unit_name(self, name):
        self.set_text_of_element_via_css("#webui_unit_name", name)

    def get_unit_description(self):
        path = "#webui_unit_description"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_unit_description(self, description):
        path = "#webui_unit_description"
        self.set_text_of_element_via_css(path, description)

    def get_unit_system_ip(self):
        return self.get_attribute_of_element_via_css("#eth1_ip", "value")

    def set_unit_system_ip(self, ip):
        self.set_text_of_element_via_css("#eth1_ip", ip)

    def get_unit_system_netmask(self):
        return self.get_attribute_of_element_via_css("#eth1_netmask", "value")

    def set_unit_system_netmask(self, mask):
        self.set_text_of_element_via_css("#eth1_netmask", mask)

    def get_unit_system_gateway(self):
        return self.get_attribute_of_element_via_css("#eth1_gateway", "value")

    def set_unit_system_gateway(self, ip):
        self.set_text_of_element_via_css("#eth1_gateway", ip)

    def get_enable_management_port_state(self):
        return self.get_state_of_element_via_css("#eth0_enable")

    def set_enable_management_port_state(self, state):
        self.set_state_of_element_via_css("#eth0_enable", state)

    def get_unit_management_port_ip(self):
        return self.get_attribute_of_element_via_css("#eth0_ip", "value")

    def set_unit_management_port_ip(self, ip):
        self.set_text_of_element_via_css("#eth0_ip", ip)

    def get_unit_management_port_netmask(self):
        return self.get_attribute_of_element_via_css("#eth0_netmask", "value")

    def set_unit_management_port_netmask(self, mask):
        self.set_text_of_element_via_css("#eth0_netmask", mask)

    def get_unit_management_port_gateway(self):
        return self.get_attribute_of_element_via_css("#eth0_gateway", "value")

    def set_unit_management_port_gateway(self, ip):
        self.set_text_of_element_via_css("#eth0_gateway", ip)

    def get_enable_teaming_port_state(self):
        return self.get_state_of_element_via_css("#eth2_enable")

    def set_enable_teaming_port_state(self, state):
        self.set_state_of_element_via_css("#eth2_enable", state)

    def get_unit_teaming_port_ip(self):
        return self.get_attribute_of_element_via_css("#eth2_ip", "value")

    def set_unit_teaming_port_ip(self, ip):
        self.set_text_of_element_via_css("#eth2_ip", ip)

    def get_unit_teaming_port_netmask(self):
        return self.get_attribute_of_element_via_css("#eth2_netmask", "value")

    def set_unit_teaming_port_netmask(self, mask):
        self.set_text_of_element_via_css("#eth2_netmask", mask)

    def get_unit_teaming_port_gateway(self):
        return self.get_attribute_of_element_via_css("#eth2_gateway", "value")

    def set_unit_teaming_port_gateway(self, mask):
        self.set_text_of_element_via_css("#eth2_gateway", mask)

    def get_enable_dvi_d1_state(self):
        return self.get_state_of_element_via_css("#video_enable")

    def set_enable_dvi_d1_state(self, state):
        self.set_state_of_element_via_css("#video_enable", state)

    def get_enable_dvi_d2_state(self):
        return self.get_state_of_element_via_css("#video1_enable")

    def set_enable_dvi_d2_state(self, state):
        self.set_state_of_element_via_css("#video1_enable", state)

    def get_enable_audio_state(self):
        return self.get_state_of_element_via_css("#audio_enable")

    def set_enable_audio_state(self, state):
        self.set_state_of_element_via_css("#audio_enable", state)

    def get_enable_usb_state(self):
        return self.get_state_of_element_via_css("#usb_enable")

    def set_enable_usb_state(self, state):
        self.set_state_of_element_via_css("#usb_enable", state)

    def get_enable_serial_state(self):
        return self.get_state_of_element_via_css("#serial_enable")

    def set_enable_serial_state(self, state):
        self.set_state_of_element_via_css("#serial_enable", state)

    def get_enable_osd_alerts_state(self):
        return self.get_state_of_element_via_css("#osd_alerts_enable")

    def set_enable_osd_alerts_state(self, state):
        self.set_state_of_element_via_css("#osd_alerts_enable", state)

    def get_selected_keyboard_country_code(self):
        return self.get_selected_value_of_select_element_by_css("#kbd_ccode")

    def get_all_keyboard_country_codes(self):
        codes = self.get_options_from_select_element_by_css("#kbd_ccode")
        return codes

    def select_keyboard_country_code(self, code):
        self.select_text_of_select_element_by_css("#kbd_ccode", code)

    def get_audio_mic_boost_state(self):
        return self.get_state_of_element_via_css("#audio_micboost")

    def set_audio_mic_boost_state(self, state):
        self.set_state_of_element_via_css("#audio_micboost", state)

    def get_audio_mic_state(self):
        return self.get_state_of_element_via_css("#audio_mic")

    def set_audio_mic_state(self, state):
        self.set_state_of_element_via_css("#audio_mic", state)

    def get_video_compatibility_for_dvi_d1_state(self):
        return self.get_state_of_element_via_css("#video_compat_check_enable")

    def set_video_compatibility_for_dvi_d1_state(self, state):
        self.set_state_of_element_via_css("#video_compat_check_enable", state)

    def get_video_compatibility_for_dvi_d2_state(self):
        return self.get_state_of_element_via_css("#video1_compat_check_enable")

    def set_video_compatibility_for_dvi_d2_state(self, state):
        self.set_state_of_element_via_css("#video1_compat_check_enable", state)

    def get_force_video_refresh_rate_for_dvi_d1_state(self):
        return self.get_state_of_element_via_css("#video_compat_check_enable")

    def set_force_video_refresh_rate_for_dvi_d1_state(self, state):
        self.set_state_of_element_via_css("#video_compat_check_enable", state)

    def get_force_video_refresh_rate_for_dvi_d2_state(self):
        return self.get_state_of_element_via_css("#video1_compat_check_enable")

    def set_force_video_refresh_rate_for_dvi_d2_state(self, state):
        self.set_state_of_element_via_css("#video1_compat_check_enable", state)

    def get_video_switching_mode_for_dvi_d1_fast_switching_mode_state(self):
        path = "#video_match_params_fast_switching"
        return self.get_state_of_element_via_css(path)

    def get_video_switching_mode_for_dvi_d1_match_frame_rate_mode_state(self):
        path = "#video_match_params_match_frame_rate"
        return self.get_state_of_element_via_css(path)

    def get_video_switching_mode_for_dvi_d2_fast_switching_mode_state(self):
        path = "#video1_match_params_fast_switching"
        return self.get_state_of_element_via_css(path)

    def get_video_switching_mode_for_dvi_d2_match_frame_rate_mode_state(self):
        path = "#video1_match_params_match_frame_rate"
        return self.get_state_of_element_via_css(path)

    def set_video_switching_mode_for_dvi_d1_to_fast_switching(self):
        self.click_button_by_css("#video_match_params_fast_switching")

    def set_video_switching_mode_for_dvi_d1_to_match_frame_rate(self):
        self.click_button_by_css("#video_match_params_match_frame_rate")

    def set_video_switching_mode_for_dvi_d2_to_fast_switching(self):
        self.click_button_by_css("#video1_match_params_fast_switching")

    def set_video_switching_mode_for_dvi_d2_to_match_frame_rate(self):
        self.click_button_by_css("#video1_match_params_match_frame_rate")

    def get_selected_serial_baud_rate(self):
        path = "#serial_baud_rate"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_serial_baud_rate_options(self):
        return self.get_options_from_select_element_by_css("#serial_baud_rate")

    def set_serial_baud_rate_option(self, text):
        self.select_text_of_select_element_by_css("#serial_baud_rate", text)

    def get_selected_serial_data_bit(self):
        path = "#serial_data_bits"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_serial_data_bit_options(self):
        return self.get_options_from_select_element_by_css("#serial_data_bits")

    def set_serial_data_bit_option(self, text):
        self.select_text_of_select_element_by_css("#serial_data_bits", text)

    def get_selected_serial_stop_bit(self):
        path = "#serial_stop_bits"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_serial_stop_bit_options(self):
        return self.get_options_from_select_element_by_css("#serial_stop_bits")

    def set_serial_stop_bit_option(self, text):
        self.select_text_of_select_element_by_css("#serial_stop_bits", text)

    def get_selected_serial_parity(self):
        path = "#serial_parity"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_serial_parity_options(self):
        return self.get_options_from_select_element_by_css("#serial_parity")

    def set_serial_parity_option(self, text):
        self.select_text_of_select_element_by_css("#serial_parity", text)

    def click_short_identify(self):
        self.click_button_by_css("#video_identify_short")

    def click_long_identify(self):
        self.click_button_by_css("#video_identify_long")

    def get_identify_counter(self, ip):
        try:
            telnet = TelnetService(ip, 23)
            command = b"dvix_test fpga 14\n"
            counter = telnet.get_response_from_command(command)
            counter = str(counter)
            match = re.search(r"fpga_ident      [0-9a-zA-Z]{8}", counter)
            if match:
                counter = match.group().replace("fpga_ident      ", "")
                return counter
            else:
                raise RuntimeError("Could not get Identify Counter " +
                                   "via TelnetService.")
        except ConnectionRefusedError:
            self.driver.get("%s/cgi-bin/show?page=set.html" % ip)
            pword = "Ajg8NB3XtcKdecdp"
            self.set_text_of_element_via_css("#admin_passwd", pword)
            self.set_state_of_element_via_css("#telnet_enable", True)
            self.click_button_by_css(".submit")
            self.driver.refresh()
            if self.get_state_of_element_via_css("#telnet_enable"):
                self.driver.get("%s/cgi-bin/show?page=index.html" % ip)
                telnet = TelnetService(ip, 23)
                counter = telnet.get_response_from_command(command)
                counter = str(counter)
                match = re.search(r"fpga_ident      [0-9a-zA-Z]{8}", counter)
                if match:
                    counter = match.group().replace("fpga_ident      ", "")
                    return counter
                else:
                    raise RuntimeError("Could not get Identify Counter " +
                                       "via TelnetService.")

    def get_target_transmitter_ip_address(self):
        path = "#server_unit_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address(self, ip):
        self.set_text_of_element_via_css("#server_unit_ip1", ip)

    def get_target_transmitter_use_eth2_state(self):
        return self.get_state_of_element_via_css("#server_unit_ip_eth2_used")

    def set_target_transmitter_use_eth2_state(self, state):
        self.set_state_of_element_via_css("#server_unit_ip_eth2_used", state)

    def get_target_transmitter_ip_address_eth2(self):
        path = "#server_unit_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_eth2(self, ip):
        self.set_text_of_element_via_css("#server_unit_ip2", ip)

    def click_show_advanced_target_transmitter_settings_button(self):
        try:
            self.click_button_by_css("#rxconfig_expand_icon")
        except Exception:
            pass

    def get_visibility_target_transmitter_ip_address_for_dvi_d1(self):
        return self.get_visibility_of_element_by_css("#server_video_ip1")

    def get_target_transmitter_ip_address_for_dvi_d1(self):
        path = "#server_video_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_for_dvi_d1(self, ip):
        self.set_text_of_element_via_css("#server_video_ip1", ip)

    def get_visibility_target_transmitter_use_eth2_for_dvi_d1(self):
        path = "#server_video_ip_eth2_used"
        return self.get_visibility_of_element_by_css(path)

    def get_target_transmitter_use_eth2_for_dvi_d1_state(self):
        return self.get_state_of_element_via_css("#server_video_ip_eth2_used")

    def set_target_transmitter_use_eth2_for_dvi_d1_state(self, state):
        self.set_state_of_element_via_css("#server_video_ip_eth2_used", state)

    def get_visibility_target_transmitter_ip_address_2_for_dvi_d1(self):
        return self.get_visibility_of_element_by_css("#server_video_ip2")

    def get_target_transmitter_ip_address_2_for_dvi_d1(self):
        path = "#server_video_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_2_for_dvi_d1(self, ip):
        self.set_text_of_element_via_css("#server_video_ip2", ip)

    def get_visibility_target_transmitter_video_no_for_dvi_d1(self):
        return self.get_visibility_of_element_by_css("#server_video_num")

    def get_selected_target_transmitter_video_no_for_dvi_d1(self):
        path = "#server_video_num"
        return self.get_selected_value_of_select_element_by_css(path)

    def set_target_transmitter_video_no_for_dvi_d1(self, text):
        self.select_text_of_select_element_by_css("#server_video_num", text)

    def get_visibility_target_transmitter_ip_address_for_dvi_d2(self):
        return self.get_visibility_of_element_by_css("#server_video1_ip1")

    def get_target_transmitter_ip_address_for_dvi_d2(self):
        path = "#server_video1_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_for_dvi_d2(self, ip):
        self.set_text_of_element_via_css("#server_video1_ip1", ip)

    def get_visibility_target_transmitter_use_eth2_for_dvi_d2(self):
        path = "#server_video1_ip_eth2_used"
        return self.get_visibility_of_element_by_css(path)

    def get_target_transmitter_use_eth2_for_dvi_d2_state(self):
        return self.get_state_of_element_via_css("#server_video1_ip_eth2_used")

    def set_target_transmitter_use_eth2_for_dvi_d2_state(self, state):
        self.set_state_of_element_via_css("#server_video1_ip_eth2_used", state)

    def get_visibility_target_transmitter_ip_address_2_for_dvi_d2(self):
        return self.get_visibility_of_element_by_css("#server_video1_ip2")

    def get_target_transmitter_ip_address_2_for_dvi_d2(self):
        path = "#server_video1_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_2_for_dvi_d2(self, ip):
        self.set_text_of_element_via_css("#server_video1_ip2", ip)

    def get_visibility_target_transmitter_video_no_for_dvi_d2(self):
        return self.get_visibility_of_element_by_css("#server_video1_num")

    def get_selected_target_transmitter_video_no_for_dvi_d2(self):
        path = "#server_video1_num"
        return self.get_selected_value_of_select_element_by_css(path)

    def set_target_transmitter_video_no_for_dvi_d2(self, text):
        self.select_text_of_select_element_by_css("#server_video1_num", text)

    def get_visibility_target_transmitter_ip_address_for_audio(self):
        return self.get_visibility_of_element_by_css("#server_audio_ip1")

    def get_target_transmitter_ip_address_for_audio(self):
        path = "#server_audio_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_for_audio(self, ip):
        self.set_text_of_element_via_css("#server_audio_ip1", ip)

    def get_visibility_target_transmitter_use_eth2_for_audio(self):
        path = "#server_audio_ip_eth2_used"
        return self.get_visibility_of_element_by_css(path)

    def get_target_transmitter_use_eth2_for_audio_state(self):
        return self.get_state_of_element_via_css("#server_audio_ip_eth2_used")

    def set_target_transmitter_use_eth2_for_audio_state(self, state):
        self.set_state_of_element_via_css("#server_audio_ip_eth2_used", state)

    def get_visibility_target_transmitter_ip_address_2_for_audio(self):
        return self.get_visibility_of_element_by_css("#server_audio_ip2")

    def get_target_transmitter_ip_address_2_for_audio(self):
        path = "#server_audio_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_2_for_audio(self, ip):
        self.set_text_of_element_via_css("#server_audio_ip2", ip)

    def get_visibility_target_transmitter_ip_address_for_usb(self):
        return self.get_visibility_of_element_by_css("#server_usb_ip1")

    def get_target_transmitter_ip_address_for_usb(self):
        path = "#server_usb_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_for_usb(self, ip):
        self.set_text_of_element_via_css("#server_usb_ip1", ip)

    def get_visibility_target_transmitter_use_eth2_for_usb(self):
        path = "#server_usb_ip_eth2_used"
        return self.get_visibility_of_element_by_css(path)

    def get_target_transmitter_use_eth2_for_usb_state(self):
        return self.get_state_of_element_via_css("#server_usb_ip_eth2_used")

    def set_target_transmitter_use_eth2_for_usb_state(self, state):
        self.set_state_of_element_via_css("#server_usb_ip_eth2_used", state)

    def get_visibility_target_transmitter_ip_address_2_for_usb(self):
        return self.get_visibility_of_element_by_css("#server_usb_ip2")

    def get_target_transmitter_ip_address_2_for_usb(self):
        path = "#server_usb_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_2_for_usb(self, ip):
        self.set_text_of_element_via_css("#server_usb_ip2", ip)

    def get_visibility_target_transmitter_ip_address_for_serial(self):
        return self.get_visibility_of_element_by_css("#server_serial_ip1")

    def get_target_transmitter_ip_address_for_serial(self):
        path = "#server_serial_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_for_serial(self, ip):
        self.set_text_of_element_via_css("#server_serial_ip1", ip)

    def get_visibility_target_transmitter_use_eth2_for_serial(self):
        path = "#server_serial_ip_eth2_used"
        return self.get_visibility_of_element_by_css(path)

    def get_target_transmitter_use_eth2_for_serial_state(self):
        return self.get_state_of_element_via_css("#server_serial_ip_eth2_used")

    def set_target_transmitter_use_eth2_for_serial_state(self, state):
        self.set_state_of_element_via_css("#server_serial_ip_eth2_used", state)

    def get_visibility_target_transmitter_ip_address_2_for_serial(self):
        return self.get_visibility_of_element_by_css("#server_serial_ip2")

    def get_target_transmitter_ip_address_2_for_serial(self):
        path = "#server_serial_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_target_transmitter_ip_address_2_for_serial(self, ip):
        self.set_text_of_element_via_css("#server_serial_ip2", ip)

    def get_enable_multicast_dvi_d1_state(self):
        return self.get_state_of_element_via_css("#multicast_video_enable")

    def set_enable_multicast_dvi_d1_state(self, state):
        self.set_state_of_element_via_css("#multicast_video_enable", state)

    def get_dvi_d1_multicast_ip_address(self):
        path = "#multicast_video_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_dvi_d1_multicast_ip_address(self, ip):
        self.set_text_of_element_via_css("#multicast_video_ip1", ip)

    def get_dvi_d1_multicast_ip_address_2(self):
        path = "#multicast_video_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_dvi_d1_multicast_ip_address_2(self, ip):
        self.set_text_of_element_via_css("#multicast_video_ip2", ip)

    def get_enable_multicast_dvi_d2_state(self):
        return self.get_state_of_element_via_css("#multicast_video1_enable")

    def set_enable_multicast_dvi_d2_state(self, state):
        self.set_state_of_element_via_css("#multicast_video1_enable", state)

    def get_dvi_d2_multicast_ip_address(self):
        path = "#multicast_video1_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_dvi_d2_multicast_ip_address(self, ip):
        self.set_text_of_element_via_css("#multicast_video1_ip1", ip)

    def get_dvi_d2_multicast_ip_address_2(self):
        path = "#multicast_video1_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_dvi_d2_multicast_ip_address_2(self, ip):
        self.set_text_of_element_via_css("#multicast_video1_ip2", ip)

    def get_enable_multicast_audio_state(self):
        return self.get_state_of_element_via_css("#multicast_audio_enable")

    def set_enable_multicast_audio_state(self, state):
        self.set_state_of_element_via_css("#multicast_audio_enable", state)

    def get_audio_multicast_ip_address(self):
        path = "#multicast_audio_ip1"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_audio_multicast_ip_address(self, ip):
        self.set_text_of_element_via_css("#multicast_audio_ip1", ip)

    def get_audio_multicast_ip_address_2(self):
        path = "#multicast_audio_ip2"
        return self.get_attribute_of_element_via_css(path, "value")

    def set_audio_multicast_ip_address_2(self, ip):
        self.set_text_of_element_via_css("#multicast_audio_ip2", ip)

    def update_config_form(self):
        return self.click_update_button("#configForm_submit")

    def update_rx_config_form(self):
        return self.click_update_button("#rxConfigForm_submit")

    def update_multicast_config_form(self):
        return self.click_update_button("#multicastConfigForm_submit")

    def update_config_form_that_starts_reboot(self, base_url):
        self.driver.find_element_by_css_selector("#configForm_submit").click()
        waiting = True
        while(waiting):
            url = self.driver.current_url
            if url == base_url + "/cgi-bin/show":
                waiting = False
            else:
                time.sleep(0.5)
        self.click_menu_link("System Configuration")

    def dismiss_alert_if_present(self):
        try:
            self.driver.switch_to_default_content()
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception:
            pass
