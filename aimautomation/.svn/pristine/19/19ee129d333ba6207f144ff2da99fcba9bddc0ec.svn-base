'''
Created on 6 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import unittest
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage
from root.nested.services.telnet_service import TelnetService
import re
from root.nested.services.parameters import parameter_singleton

class AimReceiversPageFunctionsTest(BaseAimRegressionTest):
    
    def test_all_links_operate_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receivers_page()
        self.assertEquals(self._page.get_text_of_page_header(), "Receivers")
        self._page.open_view_receiver_groups_page()
        self.assertEquals(self._page.get_text_of_page_header(), "Receiver Groups")
        self._page.open_add_receiver_groups_page()
        self.assertEquals(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")    
        self._page.open_update_receiver_firmware_page()
        self.assertTrue(self._page.get_text_of_page_header(), "Upgrade AIM Software")
         
    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_name(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name_field(search_term)
        self._page.click_on_filter_receivers_by_name()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            self.assertNotEqual(self._page.get_receiver_name(receiver).lower().find(search_term), -1)
             
    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_name(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name_field(search_term)
        self._page.click_on_filter_receivers_by_name()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_name(receiver).lower().find(search_term), -1)
        self._page.click_on_remove_receivers_name_filter()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))
         
    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_name(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name_field(search_term)
        self._page.click_on_filter_receivers_by_name()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_name(receiver).lower().find(search_term), -1)
        self._page.clear_receiver_names_filter()
        self._page.click_on_filter_receivers_by_name()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))
     
    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_description(receivers[1]).lower()
        self._page.send_search_term_to_receiver_description_field(search_term)
        self._page.click_on_filter_receivers_by_description()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            self.assertNotEqual(self._page.get_receiver_description(receiver).lower().find(search_term), -1)
             
    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_description(receivers[1]).lower()
        self._page.send_search_term_to_receiver_description_field(search_term)
        self._page.click_on_filter_receivers_by_description()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_description(receiver).lower().find(search_term), -1)
        self._page.click_on_remove_receivers_description_filter()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))
     
    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_description(receivers[1]).lower()
        self._page.send_search_term_to_receiver_description_field(search_term)
        self._page.click_on_filter_receivers_by_description()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_description(receiver).lower().find(search_term), -1)
        self._page.clear_receiver_descriptions_filter()
        self._page.click_on_filter_receivers_by_description()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))
         
    def test_location_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_location(receivers[1]).lower()
        self._page.send_search_term_to_receiver_location_field(search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_location(receiver).lower().find(search_term), -1)
             
    def test_location_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_location(receivers[1]).lower()
        self._page.send_search_term_to_receiver_location_field(search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_location(receiver).lower().find(search_term), -1)
        self._page.click_on_remove_receivers_location_filter()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))
     
    def test_location_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_location(receivers[1]).lower()
        self._page.send_search_term_to_receiver_location_field(search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            self.assertNotEqual(self._page.get_receiver_location(receiver).lower().find(search_term), -1)
        self._page.clear_receiver_locations_filter()
        self._page.click_on_filter_receivers_by_location()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))
         
    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        name_search_term = self._page.get_receiver_name(receivers[1]).lower()
        desc_search_term = self._page.get_receiver_description(receivers[1]).lower()
        loc_search_term = self._page.get_receiver_location(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name_field(name_search_term)
        self._page.click_on_filter_receivers_by_name()
        filtered_by_name_receivers = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        remove_filter_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_by_name_receivers) <= len(remove_filter_receivers))
        self._page.send_search_term_to_receiver_description_field(desc_search_term)
        self._page.click_on_filter_receivers_by_description()
        filtered_by_description_receivers = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        remove_filter_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_by_description_receivers) <= len(remove_filter_receivers))
        self._page.send_search_term_to_receiver_location_field(loc_search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_by_location_receivers = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        remove_filter_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_by_location_receivers) <= len(remove_filter_receivers))
     
    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_ascend_receiver_names()
        sorted_receivers = self._page.get_list_of_receivers()
        receiver_names = []
        if len(sorted_receivers) > 1:
            for receiver in sorted_receivers:
                receiver_names.append(self._page.get_receiver_name(receiver))
            counter = 0
            for counter in range((len(receiver_names) - 1)):
                self.assertTrue(receiver_names[counter].lower() <= receiver_names[counter + 1].lower())
                 
    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_decend_receiver_names()
        sorted_receivers = self._page.get_list_of_receivers()
        receiver_names = []
        if len(sorted_receivers) > 1:
            for receiver in sorted_receivers:
                receiver_names.append(self._page.get_receiver_name(receiver))
            counter = 0
            for counter in range((len(receiver_names) - 1)):
                self.assertTrue(receiver_names[counter].lower() >= receiver_names[counter + 1].lower())
     
    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_ascend_receiver_descriptions()
        sorted_receivers = self._page.get_list_of_receivers()
        receiver_descriptions = []
        if len(sorted_receivers) > 1:
            for receiver in sorted_receivers:
                receiver_descriptions.append(self._page.get_receiver_description(receiver))
            counter = 0
            for counter in range((len(receiver_descriptions) - 1)):
                self.assertTrue(receiver_descriptions[counter].lower() <= receiver_descriptions[counter + 1].lower())        
     
    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_decend_receiver_descriptions()
        sorted_receivers = self._page.get_list_of_receivers()
        receiver_descriptions = []
        if len(sorted_receivers) > 1:
            for receiver in sorted_receivers:
                receiver_descriptions.append(self._page.get_receiver_description(receiver))
            counter = 0
            for counter in range((len(receiver_descriptions) - 1)):
                self.assertTrue(receiver_descriptions[counter].lower() >= receiver_descriptions[counter + 1].lower())        
 
    def test_can_sort_locations_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_ascend_receiver_locations()
        sorted_receivers = self._page.get_list_of_receivers()
        receiver_locations = []
        if len(sorted_receivers) > 1:
            for receiver in sorted_receivers:
                receiver_locations.append(self._page.get_receiver_location(receiver))
            counter = 0
            for counter in range((len(receiver_locations) - 1)):
                self.assertTrue(receiver_locations[counter].lower() <= receiver_locations[counter + 1].lower())        
 
    def test_can_sort_locations_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_decend_receiver_locations()
        sorted_receivers = self._page.get_list_of_receivers()
        receiver_locations = []
        if len(sorted_receivers) > 1:
            for receiver in sorted_receivers:
                receiver_locations.append(self._page.get_receiver_location(receiver))
            counter = 0
            for counter in range((len(receiver_locations) - 1)):
                self.assertTrue(receiver_locations[counter].lower() >= receiver_locations[counter + 1].lower())
     
    def test_can_open_config_for_each_receiver(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        for receiver in receivers:
            link_text = self._page.get_receiver_linktext(receiver)
            page.driver.get(link_text)
            self.assertEqual(page.get_text_of_page_header(), "Receivers > Configure Receiver")
        page.driver.quit()
     
    def test_can_cancel_reboot_for_each_receiver(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            self._page.click_receiver_reboot(receiver)
            self._page.wait_for_and_click_reboot_cancel()
            self.assertTrue(self._page.get_receiver_status_image_src(receiver) in self._device_status_imgs)
             
    def test_can_identify_each_receiver(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Identify changed in v3.2")
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            ip = self._page.get_receiver_ip(receiver)
            telnet = TelnetService(ip, 23)
            flash_counter_before = telnet.get_response_from_command(b"dvix_test fpga 14; exit\n")
            flash_counter_before = str(flash_counter_before)
            match = re.search(r"(?P<value>[0-9]{8})", flash_counter_before)
            if match:
                flash_counter_before = match.group('value')
            self._page.click_receiver_identify(receiver)
            telnet = TelnetService(ip, 23)
            flash_counter_after = telnet.get_response_from_command(b"dvix_test fpga 14; exit\n")
            flash_counter_after = str(flash_counter_after)
            match = re.search(r"(?P<value>[0-9]{8})", flash_counter_after)
            if match:
                flash_counter_after = match.group('value')
            self.assertNotEqual(flash_counter_before, flash_counter_after)
     
    def test_can_connect_and_disconnect_receiver_to_a_channel_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_connect_to_channel(receivers[1])
        self.assertTrue("Receivers > Change channel on" in self._page.get_text_of_page_header())
        channels = self._page.get_list_of_channels()
        self._page.click_on_connect_receiver_to_channel_view_only(channels[1])
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        self.assertTrue(self._page.get_visibility_of_receiver_disconnect(receivers[1]))
        self._page.click_receiver_disconnect_from_channel(receivers[1])
        receivers = self._page.get_list_of_receivers()
        self.assertFalse(self._page.get_visibility_of_receiver_disconnect(receivers[1]))
 
    def test_can_connect_and_disconnect_receiver_to_a_channel_shared_access(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_connect_to_channel(receivers[1])
        self.assertTrue("Receivers > Change channel on" in self._page.get_text_of_page_header())
        channels = self._page.get_list_of_channels()
        self._page.click_on_connect_receiver_to_channel_shared_access(channels[1])
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        self.assertTrue(self._page.get_visibility_of_receiver_disconnect(receivers[1]))
        self._page.click_receiver_disconnect_from_channel(receivers[1])
        receivers = self._page.get_list_of_receivers()
        self.assertFalse(self._page.get_visibility_of_receiver_disconnect(receivers[1]))
     
    def test_can_connect_and_disconnect_receiver_to_a_channel_exclusive_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_connect_to_channel(receivers[1])
        self.assertTrue("Receivers > Change channel on" in self._page.get_text_of_page_header())
        channels = self._page.get_list_of_channels()
        self._page.click_on_connect_receiver_to_channel_exclusive_only(channels[1])
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        self.assertTrue(self._page.get_visibility_of_receiver_disconnect(receivers[1]))
        self._page.click_receiver_disconnect_from_channel(receivers[1])
        receivers = self._page.get_list_of_receivers()
        self.assertFalse(self._page.get_visibility_of_receiver_disconnect(receivers[1]))
     
    def test_can_disconnect_all_channels(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        for receiver in receivers:
            link_text = self._page.get_receiver_channel_connect_linktext(receiver)
            page.driver.get(link_text)
            channels = page.get_list_of_channels()
            page.click_on_connect_receiver_to_channel_view_only(channels[1])
        page.driver.quit()
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            self.assertTrue(self._page.get_visibility_of_receiver_disconnect(receiver))
        self._page.click_disconnect_all_receivers()
        self._page.click_lightbox_disconnect_button()
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            self.assertFalse(self._page.get_visibility_of_receiver_disconnect(receiver))
                 