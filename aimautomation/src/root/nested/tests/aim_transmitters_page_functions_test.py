'''
Created on 7 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.services.telnet_service import TelnetService
import re


class AimTransmittersPageFunctionsTest(BaseAimRegressionTest):

    def test_both_links_operate_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.open_update_transmitter_firmware_page()
        self.assertEquals(self._page.get_text_of_page_header(),
                          "Upgrade AIM Software")
        self._page.open_view_transmitters_page()
        self.assertEquals(self._page.get_text_of_page_header(),
                          "Transmitters")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_name(transmitters[-1])
        self._page.send_search_term_tx_name_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_name()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            name = self._page.get_transmitter_name(transmitter).lower()
            self.assertNotEqual(name.find(search_term.lower()), -1)

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_name(transmitters[-1])
        self._page.send_search_term_tx_name_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_name()
        filtered_txs = self._page.get_list_of_transmitters()
        for transmitter in filtered_txs:
            name = self._page.get_transmitter_name(transmitter).lower()
            self.assertNotEqual(name.find(search_term.lower()), -1)
        self._page.click_on_remove_transmitters_name_filter()
        non_filtered_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_txs) <= len(non_filtered_txs))

    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_name(transmitters[-1])
        self._page.send_search_term_tx_name_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_name()
        filtered_txs = self._page.get_list_of_transmitters()
        for transmitter in filtered_txs:
            name = self._page.get_transmitter_name(transmitter).lower()
            self.assertNotEqual(name.find(search_term.lower()), -1)
        self._page.clear_transmitter_names_filter()
        self._page.click_on_filter_transmitters_by_name()
        non_filtered_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_txs) <= len(non_filtered_txs))

    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_description(transmitters[-1])
        self._page.send_search_term_tx_description_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_description()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            desc = self._page.get_transmitter_description(transmitter).lower()
            self.assertNotEqual(desc.find(search_term.lower()), -1)

    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_description(transmitters[-1])
        self._page.send_search_term_tx_description_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_description()
        filtered_txs = self._page.get_list_of_transmitters()
        for transmitter in filtered_txs:
            desc = self._page.get_transmitter_description(transmitter).lower()
            self.assertNotEqual(desc.find(search_term.lower()), -1)
        self._page.click_on_remove_transmitters_description_filter()
        non_filtered_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_txs) <= len(non_filtered_txs))

    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_description(transmitters[-1])
        self._page.send_search_term_tx_description_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_description()
        filtered_txs = self._page.get_list_of_transmitters()
        for transmitter in filtered_txs:
            desc = self._page.get_transmitter_description(transmitter).lower()
            self.assertNotEqual(desc.find(search_term.lower()), -1)
        self._page.clear_transmitter_descriptions_filter()
        self._page.click_on_filter_transmitters_by_description()
        non_filtered_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_txs) <= len(non_filtered_txs))

    def test_location_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_location(transmitters[-1])
        self._page.send_search_term_tx_location_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_transmitters = self._page.get_list_of_transmitters()
        for transmitter in filtered_transmitters:
            loc = self._page.get_transmitter_location(transmitter).lower()
            self.assertNotEqual(loc.find(search_term.lower()), -1)

    def test_location_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_location(transmitters[-1])
        self._page.send_search_term_tx_location_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_txs = self._page.get_list_of_transmitters()
        for transmitter in filtered_txs:
            loc = self._page.get_transmitter_location(transmitter).lower()
            self.assertNotEqual(loc.find(search_term.lower()), -1)
        self._page.click_on_remove_transmitters_location_filter()
        non_filtered_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_txs) <= len(non_filtered_txs))

    def test_location_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_term = self._page.get_transmitter_location(transmitters[-1])
        self._page.send_search_term_tx_location_field(search_term.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_txs = self._page.get_list_of_transmitters()
        for transmitter in filtered_txs:
            loc = self._page.get_transmitter_location(transmitter).lower()
            self.assertNotEqual(loc.find(search_term.lower()), -1)
        self._page.clear_transmitter_locations_filter()
        self._page.click_on_filter_transmitters_by_location()
        non_filtered_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_txs) <= len(non_filtered_txs))

    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        search_name = self._page.get_transmitter_name(transmitters[-1])
        search_desc = self._page.get_transmitter_description(transmitters[-1])
        search_loc = self._page.get_transmitter_location(transmitters[-1])

        self._page.send_search_term_tx_name_field(search_name.lower())
        self._page.click_on_filter_transmitters_by_name()
        filtered_name_txs = self._page.get_list_of_transmitters()
        self._page.click_on_remove_filters()
        remove_filter_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_name_txs) <= len(remove_filter_txs))

        self._page.send_search_term_tx_description_field(search_desc.lower())
        self._page.click_on_filter_transmitters_by_description()
        filtered_desc_txs = self._page.get_list_of_transmitters()
        self._page.click_on_remove_filters()
        remove_filter_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_desc_txs) <= len(remove_filter_txs))

        self._page.send_search_term_tx_location_field(search_loc.lower())
        self._page.click_on_filter_transmitters_by_location()
        filtered_loc_txs = self._page.get_list_of_transmitters()
        self._page.click_on_remove_filters()
        remove_filter_txs = self._page.get_list_of_transmitters()
        self.assertTrue(len(filtered_loc_txs) <= len(remove_filter_txs))

    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_ascend_transmitter_names()
        sorted_transmitters = self._page.get_list_of_transmitters()
        if len(sorted_transmitters) > 1:
            tx_names = [self._page.get_transmitter_name(transmitter)
                        for transmitter in sorted_transmitters]
            for counter in range(0, (len(tx_names) - 1)):
                prior = tx_names[counter].lower()
                latter = tx_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_decend_transmitter_names()
        sorted_transmitters = self._page.get_list_of_transmitters()
        if len(sorted_transmitters) > 1:
            tx_names = [self._page.get_transmitter_name(transmitter)
                        for transmitter in sorted_transmitters]
            for counter in range(0, (len(tx_names) - 1)):
                prior = tx_names[counter].lower()
                latter = tx_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_ascend_transmitter_descriptions()
        sorted_transmitters = self._page.get_list_of_transmitters()
        if len(sorted_transmitters) > 1:
            tx_descs = [self._page.get_transmitter_description(transmitter)
                        for transmitter in sorted_transmitters]
            for counter in range(0, (len(tx_descs) - 1)):
                prior = tx_descs[counter].lower()
                latter = tx_descs[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_decend_transmitter_descriptions()
        sorted_transmitters = self._page.get_list_of_transmitters()
        if len(sorted_transmitters) > 1:
            tx_descs = [self._page.get_transmitter_description(transmitter)
                        for transmitter in sorted_transmitters]
            for counter in range(0, (len(tx_descs) - 1)):
                prior = tx_descs[counter].lower()
                lower = tx_descs[counter + 1].lower()
                self.assertTrue(prior >= lower)

    def test_can_sort_locations_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_ascend_transmitter_locations()
        sorted_transmitters = self._page.get_list_of_transmitters()
        if len(sorted_transmitters) > 1:
            tx_locs = [self._page.get_transmitter_location(transmitter)
                       for transmitter in sorted_transmitters]
            for counter in range(0, (len(tx_locs) - 1)):
                prior = tx_locs[counter].lower()
                latter = tx_locs[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_locations_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self._page.click_on_decend_transmitter_locations()
        sorted_transmitters = self._page.get_list_of_transmitters()
        if len(sorted_transmitters) > 1:
            tx_locs = [self._page.get_transmitter_location(transmitter)
                       for transmitter in sorted_transmitters]
            for counter in range(0, (len(tx_locs) - 1)):
                prior = tx_locs[counter].lower()
                latter = tx_locs[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_open_config_for_each_transmitter(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        for counter in range(0, len(transmitters)):
            transmitters = self._page.get_list_of_transmitters()
            self._page.click_transmitter_configure(transmitters[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Transmitters > Configure Transmitter")
            self._driver.back()

    def test_can_cancel_reboot_for_each_transmitter(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            self._page.click_transmitter_reboot(transmitter)
            self._page.wait_for_and_click_reboot_cancel()
            src = self._page.get_tx_status_img_src(transmitter)
            self.assertTrue(src in self._device_status_imgs)

    def test_can_identify_each_transmitter(self):
        self.identify_skip_check()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        for transmitter in transmitters:
            ip = self._page.get_transmitter_ip(transmitter)
            before = self.get_value_from_telnet(ip, b"dvix_test fpga 14;" +
                                                     "exit\n")
            self._page.click_transmitter_identify(transmitter)
            after = self.get_value_from_telnet(ip, b"dvix_test fpga 14;" +
                                                    "exit\n")
            self.assertNotEqual(before, after)

    """
    Utilities
    """
    def get_value_from_telnet(self, ip, command, pattern=r"(?P<value>[0-9]+)"):
        telnet = TelnetService(ip, 23)
        returned_value = str(telnet.get_response_from_command(command))
        match = re.search(pattern, returned_value)
        if match:
            return match.group('value')
