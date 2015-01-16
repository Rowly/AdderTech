'''
Created on 16 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage
from root.nested.services.telnet_service import TelnetService
from root.nested.services.parameters import parameter_singleton
import re

class AimTransmitterConfigPageFunctions(BaseAimRegressionTest):
     
    def test_transmitter_ip_address_cannot_be_changed_to_invalid_address(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    page.set_transmitter_ip_via_config_page("1.1.123123123.1")
                    page.click_save_expect_light_box()
                    page.check_for_error_message("configure_device_ajax_message")
                    self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
                    page.click_lightbox_ok_button()
                    page.set_transmitter_ip_via_config_page("abc.ade.ade.adf")
                    page.click_save_expect_light_box()
                    page.check_for_error_message("configure_device_ajax_message")
                    self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
                    page.click_lightbox_ok_button()
                    page.set_transmitter_ip_via_config_page("1.2")
                    page.click_save_expect_light_box()
                    self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
                    page.click_lightbox_ok_button()
                    #page.set_transmitter_ip_via_config_page("192.168.1.255")#KNOW ISSUE
                    #page.click_save()
                    #self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
                    #page.click_lightbox_ok_button()
                    #page.set_transmitter_ip_via_config_page("192.168.16.255")#KNOW ISSUE
                    #page.click_save()
                    #self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
                    #page.click_lightbox_ok_button()
                    page.set_transmitter_ip_via_config_page("255.255.255.255")
                    page.click_save_expect_light_box()
                    self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
                    page.click_lightbox_ok_button()
            finally:
                page.driver.quit()
        elif not self._test_all:
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            self._page.set_transmitter_ip_via_config_page("1.1.123123123.1")
            self._page.click_save_expect_light_box()
            self.assertEquals(self._page.get_lightbox_title_text(), "Device Off Network")
            self._page.click_lightbox_ok_button()
            self._page.set_transmitter_ip_via_config_page("abc.ade.ade.adf")
            self._page.click_save_expect_light_box()
            self.assertEquals(self._page.get_lightbox_title_text(), "Device Off Network")
            self._page.click_lightbox_ok_button()
            self._page.set_transmitter_ip_via_config_page("1.2")
            self._page.click_save_expect_light_box()
            self.assertEquals(self._page.get_lightbox_title_text(), "Device Off Network")
            self._page.click_lightbox_ok_button()
            #page.set_transmitter_ip_via_config_page("192.168.1.255")#KNOW ISSUE
            #page.click_save()
            #self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
            #page.click_lightbox_ok_button()
            #page.set_transmitter_ip_via_config_page("192.168.16.255")#KNOW ISSUE
            #page.click_save()
            #self.assertEquals(page.get_lightbox_title_text(), "Device Off Network")
            #page.click_lightbox_ok_button()
            self._page.set_transmitter_ip_via_config_page("255.255.255.255")
            self._page.click_save_expect_light_box()
            self.assertEquals(self._page.get_lightbox_title_text(), "Device Off Network")
            self._page.click_lightbox_ok_button()
    
    def test_can_select_dummy_boot_keyboard_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()        
                    page.select_dummy_boot_keyboard_no()
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_0"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fake_keyboard; exit\n"))
                    match = re.search(r"fake_keyboard; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "0")
                    page.select_dummy_boot_keyboard_yes()
                    page.click_save()
                    page.confirm_no_longer_on_transmitter_config_page()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_1"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fake_keyboard; exit\n"))
                    match = re.search(r"fake_keyboard; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "1")
                    page.select_dummy_boot_keyboard_global()
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_-1"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fake_keyboard; exit\n"))
                    match = re.search(r"fake_keyboard; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "1")
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()        
            self._page.select_dummy_boot_keyboard_no()
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_0"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fake_keyboard; exit\n"))
#             match = re.search(r"fake_keyboard; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "0")
            self._page.select_dummy_boot_keyboard_yes()
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_1"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fake_keyboard; exit\n"))
#             match = re.search(r"fake_keyboard; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "1")
            self._page.select_dummy_boot_keyboard_global()
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable Dummy Boot Keyboard", "tp_fk_enable_-1"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fake_keyboard; exit\n"))
#             match = re.search(r"fake_keyboard; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "1")
  
    def test_can_select_USB_speed_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    name = page.get_transmitter_name_from_config_page()
                    ip = page.get_ip_address_from_config_page()        
                    page.select_usb_speed_high_speed()
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_0"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fullspeed\n"))
                    match = re.search(r"fullspeed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "0")
                    page.select_usb_speed_full_speed()
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_1"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fullspeed; exit\n"))
                    match = re.search(r"fullspeed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "1", "Error when testing: " + name)
                    page.select_usb_speed_global()
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_-1"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fullspeed; exit\n"))
                    match = re.search(r"fullspeed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "0")
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            name = self._page.get_transmitter_name_from_config_page()
            ip = self._page.get_ip_address_from_config_page()        
            self._page.select_usb_speed_high_speed()
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_0"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fullspeed; exit\n"))
#             match = re.search(r"fullspeed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "0")
            self._page.select_usb_speed_full_speed()
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_1"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fullspeed; exit\n"))
#             match = re.search(r"fullspeed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "1", "Error when testing: " + name)
            self._page.select_usb_speed_global()
            self._page.click_save()
            self._page.confirm_no_longer_on_transmitter_config_page()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("USB Speed", "tp_usb_speed_-1"))
#             self.assertEquals(value, "1", "Error when testing: " + name)
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:fullspeed; exit\n"))
#             match = re.search(r"fullspeed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "0")
  
    def test_can_select_USB_hub_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()        
                    page.click_radio_option_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_13")
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_13"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:hub_size; exit\n"))
                    match = re.search(r"hub_size; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "13")
                    page.click_radio_option_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_7")
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_7"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:hub_size; exit\n"))
                    match = re.search(r"hub_size; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "7")
                    page.click_radio_option_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_-1")
                    page.click_save()
                    page.driver.get(link_text)
                    self.assertTrue(page.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_-1"))
                    telnet = TelnetService(ip, 23)
                    returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:hub_size; exit\n"))
                    match = re.search(r"hub_size; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                    if match:
                        value = match.group('value')
                    self.assertEquals(value, "13")
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()        
            self._page.click_radio_option_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_13")
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_13"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:hub_size; exit\n"))
#             match = re.search(r"hub_size; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "13")
            self._page.click_radio_option_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_7")
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_7"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:hub_size; exit\n"))
#             match = re.search(r"hub_size; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "7")
            self._page.click_radio_option_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_-1")
            self._page.click_save()
            self._page.driver.get(link_text)
            self.assertTrue(self._page.is_option_selected_by_div_text_and_id("USB Hub Size", "tp_usb_hub_size_-1"))
#             telnet = TelnetService(ip, 23)
#             returned_value = str(telnet.get_response_from_command(b"dvix_config_get usb:hub_size; exit\n"))
#             match = re.search(r"hub_size; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#             if match:
#                 value = match.group('value')
#             self.assertEquals(value, "13")
      
    def test_can_select_DDC_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_ddc")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_ddc", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("DDC", value))
                            telnet = TelnetService(ip, 23)
                            found_ddc = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_dddc; exit\n"))
                            match = re.search(r"video_dddc; exit\\r\\n(?P<value>[0-9]+)", found_ddc)
                            if match:
                                found_ddc = match.group('value')
                            if value == '-1' and found_ddc == '0':#unchanged global setting DDDC=0
                                found_ddc = '-1'
                            self.assertEqual(value, found_ddc)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_ddc", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_ddc")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_ddc", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("DDC", value))
#                     telnet = TelnetService(ip, 23)
#                     found_ddc = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_dddc; exit\n"))
#                     match = re.search(r"video_dddc; exit\\r\\n(?P<value>[0-9]+)", found_ddc)
#                     if match:
#                         found_ddc = match.group('value')
#                     if value == '-1' and found_ddc == '0':#unchanged global setting DDDC=0
#                         found_ddc = '-1'
#                     self.assertEqual(value, found_ddc)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_ddc", "-1")
            self._page.click_save()
  
    def test_can_select_hot_plug_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_hpd")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_hpd", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Hot Plug Detect Control", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_hpd; exit\n"))
                            match = re.search(r"video_hpd; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == '1':
                                match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_hpd", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_hpd")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_hpd", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Hot Plug Detect Control", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_hpd; exit\n"))
#                     match = re.search(r"video_hpd; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == '1':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_hpd", "-1")
            self._page.click_save()
  
    def test_can_select_hot_plug_signal_options(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_video_ddc_delay")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_video_ddc_delay", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Hot Plug Detect Signal Period", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_ddc_delay; exit\n"))
                            match = re.search(r"video_ddc_delay; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
                                    if value == '-1' and match_value == '100000':
                                            match_value = '-1'
                            else:
                                if value == '-1' and match_value == '23000':
                                    match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_video_ddc_delay", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_video_ddc_delay")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text )
                    self._page.select_dropdown_item_by_value("tp_video_ddc_delay", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Hot Plug Detect Signal Period", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_ddc_delay; exit\n"))
#                     match = re.search(r"video_ddc_delay; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
#                         if value == '-1' and match_value == '100000':
#                             match_value = '-1'
#                     else:
#                         if value == '-1' and match_value == '23000':
#                             match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_video_ddc_delay", "-1")
            self._page.click_save()
  
    def test_can_select_background_refresh_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    name = page.get_transmitter_name_from_config_page()
                    all_options = page.get_options_from_select_element("tp_video_br")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_video_br", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Background Refresh", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_br; exit\n"))
                            match = re.search(r"video_br; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == '32':
                                match_value = '-1'
                            self.assertEquals(match_value, value, "Error when testing: " + name)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_video_br", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            name = self._page.get_transmitter_name_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_video_br")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_video_br", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Background Refresh", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_br; exit\n"))
#                     match = re.search(r"video_br; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     self.assertTrue(match, "Failed to match")
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == '32':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value, "Error when testing: " + name)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_video_br", "-1")
            self._page.click_save()
            self._page.driver.quit()
  
    def test_can_select_colour_depth_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_video_bpp")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_video_bpp", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Colour Depth", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_bpp; exit\n"))
                            match = re.search(r"video_bpp; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == '24':
                                match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_video_bpp", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_video_bpp")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_video_bpp", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Colour Depth", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:video_bpp; exit\n"))
#                     match = re.search(r"video_bpp; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == '24':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_video_bpp", "-1")
            self._page.click_save()
  
    def test_can_select_serial_parity_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_serial_parity")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_serial_parity", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Serial Parity", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_parity; exit\n"))
                            match = re.search(r"serial_parity; exit\\r\\n(?P<value>[A-Z]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == 'N':
                                match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_serial_parity", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_serial_parity")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_serial_parity", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Serial Parity", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_parity; exit\n"))
#                     match = re.search(r"serial_parity; exit\\r\\n(?P<value>[A-Z]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == 'N':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_serial_parity", "-1")
            self._page.click_save()
              
    def test_can_select_serial_data_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_serial_data_bits")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_serial_data_bits", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Serial Data Bits", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_data_bits; exit\n"))
                            match = re.search(r"serial_data_bits; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == '8':
                                match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_serial_data_bits", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_serial_data_bits")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_serial_data_bits", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Serial Data Bits", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_data_bits; exit\n"))
#                     match = re.search(r"serial_data_bits; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == '8':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_serial_data_bits", "-1")
            self._page.click_save()
  
    def test_can_select_serial_stop_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_serial_stop_bits")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_serial_stop_bits", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Serial Stop Bits", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_stop_bits; exit\n"))
                            match = re.search(r"serial_stop_bits; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == '1':
                                match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_serial_stop_bits", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_serial_stop_bits")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_serial_stop_bits", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Serial Stop Bits", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_stop_bits; exit\n"))
#                     match = re.search(r"serial_stop_bits; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == '1':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_serial_stop_bits", "-1")
            self._page.click_save()
  
    def test_can_select_serial_speed_options(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    ip = page.get_ip_address_from_config_page()
                    all_options = page.get_options_from_select_element("tp_serial_speed")
                    values = []
                    for option in all_options:
                        values.append(option.get_attribute('value'))
                    for value in values:
                            page.driver.get(link_text)
                            page.select_dropdown_item_by_value("tp_serial_speed", value)
                            page.click_save()
                            page.driver.get(link_text)
                            self.assertTrue(page.is_option_selected_by_div_text_and_value("Serial Speed", value))
                            telnet = TelnetService(ip, 23)
                            returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_speed; exit\n"))
                            match = re.search(r"serial_speed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
                            if match:
                                match_value = match.group('value')
                            if value == '-1' and match_value == '115200':
                                match_value = '-1'
                            self.assertEquals(match_value, value)
                    page.driver.get(link_text)
                    page.select_dropdown_item_by_value("tp_serial_speed", "-1")
                    page.click_save()
            finally:
                page.driver.quit()
        elif not self._test_all:
            link_text = self._page.get_transmitter_linktext(transmitters[-1])
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            ip = self._page.get_ip_address_from_config_page()
            all_options = self._page.get_options_from_select_element("tp_serial_speed")
            values = []
            for option in all_options:
                values.append(option.get_attribute('value'))
            for value in values:
                    self._page.driver.get(link_text)
                    self._page.select_dropdown_item_by_value("tp_serial_speed", value)
                    self._page.click_save()
                    self._page.driver.get(link_text)
                    self.assertTrue(self._page.is_option_selected_by_div_text_and_value("Serial Speed", value))
#                     telnet = TelnetService(ip, 23)
#                     returned_value = str(telnet.get_response_from_command(b"dvix_config_get dvix:serial_speed; exit\n"))
#                     match = re.search(r"serial_speed; exit\\r\\n(?P<value>[0-9]+)", returned_value)
#                     if match:
#                         match_value = match.group('value')
#                     if value == '-1' and match_value == '115200':
#                         match_value = '-1'
#                     self.assertEquals(match_value, value)
            self._page.driver.get(link_text)
            self._page.select_dropdown_item_by_value("tp_serial_speed", "-1")
            self._page.click_save()
      
    def test_can_enter_valid_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    original_name = page.get_transmitter_name_from_config_page()
                    new_name = original_name.upper()
                    page.set_transmitter_name_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_name_from_config_page(), original_name.upper())
                    new_name = original_name+"test"
                    page.set_transmitter_name_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_name_from_config_page(), original_name+"test")
                    new_name = original_name+"%%%%%"
                    page.set_transmitter_name_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_name_from_config_page(), original_name+"%%%%%")
                    new_name = original_name.lower()
                    page.set_transmitter_name_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_name_from_config_page(), original_name.lower())
                    page.set_transmitter_name_via_config_page(original_name)
            finally:
                page.driver.quit()
        elif not self._test_all:
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            original_name = self._page.get_transmitter_name_from_config_page()
            new_name = original_name.upper()
            self._page.set_transmitter_name_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_name_from_config_page(), original_name.upper())
            new_name = original_name+"test"
            self._page.set_transmitter_name_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_name_from_config_page(), original_name+"test")
            new_name = original_name+"%%%%%"
            self._page.set_transmitter_name_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_name_from_config_page(), original_name+"%%%%%")
            new_name = original_name.lower()
            self._page.set_transmitter_name_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_name_from_config_page(), original_name.lower())
            self._page.set_transmitter_name_via_config_page(original_name)
              
    def test_can_enter_valid_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    original_name = page.get_transmitter_description_from_config_page()
                    new_name = original_name.upper()
                    page.set_transmitter_description_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_description_from_config_page(), original_name.upper())
                    new_name = original_name+"test"
                    page.set_transmitter_description_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_description_from_config_page(), original_name+"test")
                    new_name = original_name+"%%%%%"
                    page.set_transmitter_description_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_description_from_config_page(), original_name+"%%%%%")
                    new_name = original_name.lower()
                    page.set_transmitter_description_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_description_from_config_page(), original_name.lower())
                    page.set_transmitter_description_via_config_page(original_name)
            finally:
                page.driver.quit()
        elif not self._test_all:
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            original_name = self._page.get_transmitter_description_from_config_page()
            new_name = original_name.upper()
            self._page.set_transmitter_description_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_description_from_config_page(), original_name.upper())
            new_name = original_name+"test"
            self._page.set_transmitter_description_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_description_from_config_page(), original_name+"test")
            new_name = original_name+"%%%%%"
            self._page.set_transmitter_description_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_description_from_config_page(), original_name+"%%%%%")
            new_name = original_name.lower()
            self._page.set_transmitter_description_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_description_from_config_page(), original_name.lower())
            self._page.set_transmitter_description_via_config_page(original_name)
  
    def test_can_enter_valid_location(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        if self._test_all:
            try:
                page = BasePage()
                page.open_AIM_homepage_on_base_url()
                page.login_as("admin", "password", False)
                for transmitter in transmitters:
                    link_text = self._page.get_transmitter_linktext(transmitter)
                    page.driver.get(link_text)
                    self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                    original_name = page.get_transmitter_location_from_config_page()
                    new_name = original_name.upper()
                    page.set_transmitter_location_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_location_from_config_page(), original_name.upper())
                    new_name = original_name+"test"
                    page.set_transmitter_location_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_location_from_config_page(), original_name+"test")
                    new_name = original_name+"%%%%%"
                    page.set_transmitter_location_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_location_from_config_page(), original_name+"%%%%%")
                    new_name = original_name.lower()
                    page.set_transmitter_location_via_config_page(new_name)
                    self.assertEqual(page.get_transmitter_location_from_config_page(), original_name.lower())
                    page.set_transmitter_location_via_config_page(original_name)
            finally:
                page.driver.quit()
        elif not self._test_all:
            self._page.click_transmitter_configure(transmitters[-1])
            self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
            original_name = self._page.get_transmitter_location_from_config_page()
            new_name = original_name.upper()
            self._page.set_transmitter_location_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_location_from_config_page(), original_name.upper())
            new_name = original_name+"test"
            self._page.set_transmitter_location_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_location_from_config_page(), original_name+"test")
            new_name = original_name+"%%%%%"
            self._page.set_transmitter_location_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_location_from_config_page(), original_name+"%%%%%")
            new_name = original_name.lower()
            self._page.set_transmitter_location_via_config_page(new_name)
            self.assertEqual(self._page.get_transmitter_location_from_config_page(), original_name.lower())

