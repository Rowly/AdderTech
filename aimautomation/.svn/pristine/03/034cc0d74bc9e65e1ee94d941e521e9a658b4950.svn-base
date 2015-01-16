'''
Created on 7 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import unittest
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage
from root.nested.services.telnet_service import TelnetService
import re
from root.nested.services.parameters import parameter_singleton

class AimTransmittersPageFunctionsTest(BaseAimRegressionTest):
    
    def test_both_links_operate_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.open_update_transmitter_firmware_page()
        self.assertEquals(self._page.get_text_of_page_header(), "Upgrade AIM Software")
        self._page.open_view_transmitters_page()
        self.assertEquals(self._page.get_text_of_page_header(), "Transmitters")
        
    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_name(transmitters[0])
        self._page.send_search_term_to_transmitter_name_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_name()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            self.assertNotEqual(self._page.get_transmitter_name(transmitter).lower().find(search_term.lower()), -1)
            
    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_name(transmitters[0])
        self._page.send_search_term_to_transmitter_name_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_name()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_name(transmitter).lower().find(search_term.lower()), -1)
        self._page.click_on_remove_transmitters_name_filter()
        non_filtered_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_transmitters) <= len(non_filtered_transmitters))
    
    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_name(transmitters[0])
        self._page.send_search_term_to_transmitter_name_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_name()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_name(transmitter).lower().find(search_term.lower()), -1)
        self._page.clear_transmitter_names_filter()
        self._page.click_on_filter_transmitters_by_name()
        non_filtered_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_transmitters) <= len(non_filtered_transmitters))
        
    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_description(transmitters[0])
        self._page.send_search_term_to_transmitter_description_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_description()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            self.assertNotEqual(self._page.get_transmitter_description(transmitter).lower().find(search_term.lower()), -1)
            
    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_description(transmitters[0])
        self._page.send_search_term_to_transmitter_description_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_description()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_description(transmitter).lower().find(search_term.lower()), -1)
        self._page.click_on_remove_transmitters_description_filter()
        non_filtered_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_transmitters) <= len(non_filtered_transmitters))
    
    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_description(transmitters[0])
        self._page.send_search_term_to_transmitter_description_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_description()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_description(transmitter).lower().find(search_term.lower()), -1)
        self._page.clear_transmitter_descriptions_filter()
        self._page.click_on_filter_transmitters_by_description()
        non_filtered_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_transmitters) <= len(non_filtered_transmitters))
        
    def test_location_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_location(transmitters[0])
        self._page.send_search_term_to_transmitter_location_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_location(transmitter).lower().find(search_term.lower()), -1)
            
    def test_location_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_location(transmitters[0])
        self._page.send_search_term_to_transmitter_location_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_location(transmitter).lower().find(search_term.lower()), -1)
        self._page.click_on_remove_transmitters_location_filter()
        non_filtered_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_transmitters) <= len(non_filtered_transmitters))
    
    def test_location_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_location(transmitters[0])
        self._page.send_search_term_to_transmitter_location_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            self.assertNotEqual(self._page.get_transmitter_location(transmitter).lower().find(search_term.lower()), -1)
        self._page.clear_transmitter_locations_filter()
        self._page.click_on_filter_transmitters_by_location()
        non_filtered_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_transmitters) <= len(non_filtered_transmitters))
    
    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_name = self._page.get_transmitter_name(transmitters[0])
        search_description = self._page.get_transmitter_description(transmitters[0])
        search_location = self._page.get_transmitter_location(transmitters[0])
        self._page.send_search_term_to_transmitter_name_field(search_name.lower())
        self._page.click_on_filter_transmitters_by_name()
        filtered_by_name_transmitters = self._page.get_list_of_transmitters()
        self._page.click_on_remove_filters()
        remove_filter_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_by_name_transmitters) <= len(remove_filter_transmitters))
        self._page.send_search_term_to_transmitter_description_field(search_description.lower())
        self._page.click_on_filter_transmitters_by_description()
        filtered_by_description_transmitters = self._page.get_list_of_transmitters()
        self._page.click_on_remove_filters()
        remove_filter_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_by_description_transmitters) <= len(remove_filter_transmitters))
        self._page.send_search_term_to_transmitter_location_field(search_location.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_by_location_transmitters = self._page.get_list_of_transmitters()
        self._page.click_on_remove_filters()
        remove_filter_transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_by_location_transmitters) <= len(remove_filter_transmitters))
        
    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_ascend_transmitter_names()
        sorted_transmitters = self._page.get_list_of_transmitters()
        transmitter_names = []
        if len(sorted_transmitters) > 1:
            for transmitter in sorted_transmitters:
                transmitter_names.append(self._page.get_transmitter_name(transmitter))
            counter = 0
            for counter in range((len(transmitter_names) - 1)):
                self.assertTrue(transmitter_names[counter].lower() <= transmitter_names[counter + 1].lower())
                
    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_decend_transmitter_names()
        sorted_transmitters = self._page.get_list_of_transmitters()
        transmitter_names = []
        if len(sorted_transmitters) > 1:
            for transmitter in sorted_transmitters:
                transmitter_names.append(self._page.get_transmitter_name(transmitter))
            counter = 0
            for counter in range((len(transmitter_names) - 1)):
                self.assertTrue(transmitter_names[counter].lower() >= transmitter_names[counter + 1].lower())
                
    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_ascend_transmitter_descriptions()
        sorted_transmitters = self._page.get_list_of_transmitters()
        transmitter_descriptions = []
        if len(sorted_transmitters) > 1:
            for transmitter in sorted_transmitters:
                transmitter_descriptions.append(self._page.get_transmitter_description(transmitter))
            counter = 0
            for counter in range((len(transmitter_descriptions) - 1)):
                self.assertTrue(transmitter_descriptions[counter].lower() <= transmitter_descriptions[counter + 1].lower())        
    
    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_decend_transmitter_descriptions()
        sorted_transmitters = self._page.get_list_of_transmitters()
        transmitter_descriptions = []
        if len(sorted_transmitters) > 1:
            for transmitter in sorted_transmitters:
                transmitter_descriptions.append(self._page.get_transmitter_description(transmitter))
            counter = 0
            for counter in range((len(transmitter_descriptions) - 1)):
                self.assertTrue(transmitter_descriptions[counter].lower() >= transmitter_descriptions[counter + 1].lower())        

    def test_can_sort_locations_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_ascend_transmitter_locations()
        sorted_transmitters = self._page.get_list_of_transmitters()
        transmitter_locations = []
        if len(sorted_transmitters) > 1:
            for transmitter in sorted_transmitters:
                transmitter_locations.append(self._page.get_transmitter_location(transmitter))
            counter = 0
            for counter in range((len(transmitter_locations) - 1)):
                self.assertTrue(transmitter_locations[counter].lower() <= transmitter_locations[counter + 1].lower())        

    def test_can_sort_locations_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_decend_transmitter_locations()
        sorted_transmitters = self._page.get_list_of_transmitters()
        transmitter_locations = []
        if len(sorted_transmitters) > 1:
            for transmitter in sorted_transmitters:
                transmitter_locations.append(self._page.get_transmitter_location(transmitter))
            counter = 0
            for counter in range((len(transmitter_locations) - 1)):
                self.assertTrue(transmitter_locations[counter].lower() >= transmitter_locations[counter + 1].lower())
                
    def test_can_open_config_for_each_transmitter(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for transmitter in transmitters:
                link_text = self._page.get_transmitter_linktext(transmitter)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
        finally:
            page.driver.quit()
            
    def test_can_cancel_reboot_for_each_transmitter(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            self._page.click_transmitter_reboot(transmitter)
            self._page.wait_for_and_click_reboot_cancel()
            self.assertTrue(self._page.get_transmitter_status_image_src(transmitter) in self._device_status_imgs)
            
    def test_can_identify_each_transmitter(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Identify changed in v3.2")
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            ip = self._page.get_transmitter_ip(transmitter)
            telnet = TelnetService(ip, 23)
            flash_counter_before = telnet.get_response_from_command(b"dvix_test fpga 14; exit\n")
            flash_counter_before = str(flash_counter_before)
            match = re.search(r"(?P<value>[0-9]{8})", flash_counter_before)
            if match:
                flash_counter_before = match.group('value')
            self._page.click_transmitter_identify(transmitter)
            telnet = TelnetService(ip, 23)
            flash_counter_after = telnet.get_response_from_command(b"dvix_test fpga 14; exit\n")
            flash_counter_after = str(flash_counter_after)
            match = re.search(r"(?P<value>[0-9]{8})", flash_counter_after)
            if match:
                flash_counter_after = match.group('value')
            self.assertNotEqual(flash_counter_before, flash_counter_after)