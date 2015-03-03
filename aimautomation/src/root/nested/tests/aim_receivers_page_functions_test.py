'''
Created on 6 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.services.telnet_service import TelnetService
import re


class AimReceiversPageFunctionsTest(BaseAimRegressionTest):

    def test_all_links_operate_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receivers_page()
        self.assertEquals(self._page.get_text_of_page_header(),
                          "Receivers")
        self._page.open_view_receiver_groups_page()
        self.assertEquals(self._page.get_text_of_page_header(),
                          "Receiver Groups")
        self._page.open_add_receiver_groups_page()
        self.assertEquals(self._page.get_text_of_page_header(),
                          "Receiver Groups > Add Receiver Group")
        self._page.open_update_receiver_firmware_page()
        self.assertTrue(self._page.get_text_of_page_header(),
                        "Upgrade AIM Software")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_name(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name(search_term)
        self._page.click_on_filter_receivers_by_name()
        for receiver in self._page.get_list_of_receivers():
            rx_name = self._page.get_receiver_name(receiver).lower()
            self.assertNotEqual(rx_name.find(search_term), -1)

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_name(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name(search_term)
        self._page.click_on_filter_receivers_by_name()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_name = self._page.get_receiver_name(receiver).lower()
            self.assertNotEqual(rx_name.find(search_term), -1)
        self._page.click_on_remove_receivers_name_filter()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))

    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_name(receivers[1]).lower()
        self._page.send_search_term_to_receiver_name(search_term)
        self._page.click_on_filter_receivers_by_name()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_name = self._page.get_receiver_name(receiver).lower()
            self.assertNotEqual(rx_name.find(search_term), -1)
        self._page.clear_receiver_names_filter()
        self._page.click_on_filter_receivers_by_name()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))

    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_desc(receivers[1]).lower()
        self._page.send_search_term_to_receiver_desc(search_term)
        self._page.click_on_filter_receivers_by_description()
        for receiver in self._page.get_list_of_receivers():
            rx_desc = self._page.get_receiver_desc(receiver).lower()
            self.assertNotEqual(rx_desc.find(search_term), -1)

    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_desc(receivers[1]).lower()
        self._page.send_search_term_to_receiver_desc(search_term)
        self._page.click_on_filter_receivers_by_description()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_desc = self._page.get_receiver_desc(receiver).lower()
            self.assertNotEqual(rx_desc.find(search_term), -1)
        self._page.click_on_remove_receivers_description_filter()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))

    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_desc(receivers[1]).lower()
        self._page.send_search_term_to_receiver_desc(search_term)
        self._page.click_on_filter_receivers_by_description()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_desc = self._page.get_receiver_desc(receiver).lower()
            self.assertNotEqual(rx_desc.find(search_term), -1)
        self._page.clear_receiver_descriptions_filter()
        self._page.click_on_filter_receivers_by_description()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))

    def test_location_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_loc(receivers[1]).lower()
        self._page.send_search_term_to_receiver_loc(search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_loc = self._page.get_receiver_loc(receiver).lower()
            self.assertNotEqual(rx_loc.find(search_term), -1)

    def test_location_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_loc(receivers[1]).lower()
        self._page.send_search_term_to_receiver_loc(search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_loc = self._page.get_receiver_loc(receiver).lower()
            self.assertNotEqual(rx_loc.find(search_term), -1)
        self._page.click_on_remove_receivers_location_filter()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))

    def test_location_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        search_term = self._page.get_receiver_loc(receivers[1]).lower()
        self._page.send_search_term_to_receiver_loc(search_term)
        self._page.click_on_filter_receivers_by_location()
        filtered_receivers = self._page.get_list_of_receivers()
        for receiver in filtered_receivers:
            rx_loc = self._page.get_receiver_loc(receiver).lower()
            self.assertNotEqual(rx_loc.find(search_term), -1)
        self._page.clear_receiver_locations_filter()
        self._page.click_on_filter_receivers_by_location()
        non_filtered_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_receivers) <= len(non_filtered_receivers))

    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        name_search = self._page.get_receiver_name(receivers[1]).lower()
        desc_search = self._page.get_receiver_desc(receivers[1]).lower()
        loc_search = self._page.get_receiver_loc(receivers[1]).lower()

        self._page.send_search_term_to_receiver_name(name_search)
        self._page.click_on_filter_receivers_by_name()
        filtered_name = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_name) <= len(no_filter))

        self._page.send_search_term_to_receiver_desc(desc_search)
        self._page.click_on_filter_receivers_by_description()
        filtered_descs = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_descs) <= len(no_filter))

        self._page.send_search_term_to_receiver_loc(loc_search)
        self._page.click_on_filter_receivers_by_location()
        filtered_locs = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_locs) <= len(no_filter))

    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_ascend_receiver_names()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            receiver_names = [self._page.get_receiver_name(receiver)
                              for receiver in sorted_receivers]
            for counter in range(0, (len(receiver_names) - 1)):
                prior = receiver_names[counter].lower()
                latter = receiver_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_decend_receiver_names()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            receiver_names = [self._page.get_receiver_name(receiver)
                              for receiver in sorted_receivers]
            for counter in range(0, (len(receiver_names) - 1)):
                prior = receiver_names[counter].lower()
                latter = receiver_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_ascend_receiver_descriptions()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            receiver_descriptions = [self._page.get_receiver_desc(receiver)
                                     for receiver in sorted_receivers]
            for counter in range(0, (len(receiver_descriptions) - 1)):
                prior = receiver_descriptions[counter].lower()
                latter = receiver_descriptions[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_decend_receiver_descriptions()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            receiver_descriptions = [self._page.get_receiver_desc(receiver)
                                     for receiver in sorted_receivers]
            for counter in range(0, (len(receiver_descriptions) - 1)):
                prior = receiver_descriptions[counter].lower()
                latter = receiver_descriptions[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_locations_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_ascend_receiver_locations()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            receiver_locations = [self._page.get_receiver_loc(receiver)
                                  for receiver in sorted_receivers]
            for counter in range(0, (len(receiver_locations) - 1)):
                prior = receiver_locations[counter].lower()
                latter = receiver_locations[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_locations_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.click_on_decend_receiver_locations()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            receiver_locations = [self._page.get_receiver_loc(receiver)
                                  for receiver in sorted_receivers]
            for counter in range(0, (len(receiver_locations) - 1)):
                prior = receiver_locations[counter].lower()
                latter = receiver_locations[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_open_config_for_each_receiver(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        for counter in range(0, len(self._page.get_list_of_receivers())):
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Receivers > Configure Receiver")
            self._driver.back()

    def test_can_cancel_reboot_for_each_receiver(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        for receiver in self._page.get_list_of_receivers():
            self._page.click_receiver_reboot(receiver)
            self._page.wait_for_and_click_reboot_cancel()
            self.assertTrue(self._page.get_receiver_status_image_src(receiver)
                            in self._device_status_imgs)

    def test_can_identify_each_receiver(self):
        self.identify_skip_check()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        for receiver in self._page.get_list_of_receivers():
            ip = self._page.get_receiver_ip(receiver)
            telnet = TelnetService(ip, 23)
            command = b"dvix_test fpga 14; exit\n"
            flash_counter_before = telnet.get_response_from_command(command)
            flash_counter_before = str(flash_counter_before)
            match = re.search(r"(?P<value>[0-9]{8})", flash_counter_before)
            if match:
                flash_counter_before = match.group('value')
            self._page.click_receiver_identify(receiver)
            telnet = TelnetService(ip, 23)
            flash_counter_after = telnet.get_response_from_command(command)
            flash_counter_after = str(flash_counter_after)
            match = re.search(r"(?P<value>[0-9]{8})", flash_counter_after)
            if match:
                flash_counter_after = match.group('value')
            self.assertNotEqual(flash_counter_before, flash_counter_after)

    def test_connect_and_disconnect_receiver_to_channel_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self._page.click_receiver_connect_to_channel(rx)
        self.assertTrue("Receivers > Change channel on"
                        in self._page.get_text_of_page_header())
        channels = self._page.get_list_of_channels()
        self._page.click_connect_receiver_to_channel_view_only(channels[1])
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self.assertTrue(self._page.get_visibility_of_receiver_disconnect(rx))
        self._page.click_receiver_disconnect_from_channel(rx)
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self.assertFalse(self._page.get_visibility_of_receiver_disconnect(rx))

    def test_connect_and_disconnect_receiver_to_channel_shared_access(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self._page.click_receiver_connect_to_channel(rx)
        self.assertTrue("Receivers > Change channel on"
                        in self._page.get_text_of_page_header())
        channels = self._page.get_list_of_channels()
        chl = channels[1]
        self._page.click_on_connect_receiver_to_channel_shared_access(chl)
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self.assertTrue(self._page.get_visibility_of_receiver_disconnect(rx))
        self._page.click_receiver_disconnect_from_channel(rx)
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self.assertFalse(self._page.get_visibility_of_receiver_disconnect(rx))

    def test_connect_and_disconnect_receiver_to_a_channel_exclusive_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self._page.click_receiver_connect_to_channel(rx)
        self.assertTrue("Receivers > Change channel on"
                        in self._page.get_text_of_page_header())
        channels = self._page.get_list_of_channels()
        chl = channels[1]
        self._page.click_on_connect_receiver_to_channel_exclusive_only(chl)
        self._page.driver.refresh()
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self.assertTrue(self._page.get_visibility_of_receiver_disconnect(rx))
        self._page.click_receiver_disconnect_from_channel(rx)
        receivers = self._page.get_list_of_receivers()
        rx = receivers[1]
        self.assertFalse(self._page.get_visibility_of_receiver_disconnect(rx))

    def test_can_disconnect_all_channels(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        for counter in range(0, len(self._page.get_list_of_receivers())):
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_connect_to_channel(receivers[counter])
            channels = self._page.get_list_of_channels()
            chl = channels[1]
            self._page.click_connect_receiver_to_channel_view_only(chl)
        self._page.driver.refresh()
        for rx in self._page.get_list_of_receivers():
            visible = self._page.get_visibility_of_receiver_disconnect(rx)
            self.assertTrue(visible)
        self._page.click_disconnect_all_receivers()
        self._page.click_lightbox_disconnect_button()
        self._page.driver.refresh()
        for rx in self._page.get_list_of_receivers():
            visible = self._page.get_visibility_of_receiver_disconnect(rx)
            self.assertFalse(visible)

    """
    Default appearances
    """
    def test_receiver_page_opened_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers")
        self.assertEqual(self._page.get_text_of_view_receivers_link(),
                         "View Receivers")
        self.assertEqual(self._page.get_text_of_view_receiver_groups_link(),
                         "View Receiver Groups")
        self.assertEqual(self._page.get_text_of_add_receiver_groups_link(),
                         "Add Receiver Group")
        self.assertEqual(self._page.get_text_of_update_rx_firmware_link(),
                         "Update Firmware")

    def test_receivers_are_shown_in_paginated_table(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receviers = self._page.get_list_of_receivers()
        self.assertTrue(len(receviers) >= 1)
        total_receivers = self._page.get_pagination_total()
        if int(total_receivers) <= 20:
            self.assertTrue(len(receviers) <= int(total_receivers))
        elif int(total_receivers) > 20:
            pass

    def test_each_receiver_row_comprises_correct_elements(self):
        device_info = self._page.get_device_version_via_api()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(receivers) >= 1)
        for receiver in receivers:
            row_id = self._page.get_row_id_of_receiver(receiver)
            device_id = self._page.get_device_id_from_row_id(row_id)
            cells = self._page.get_cell_elements(receiver)
            self.assertEqual(len(cells), 11)
            self.assertEquals(self._page.check_for_span_type_tooltip(cells[0]),
                              "tooltip")
            self.assertEqual(self._page.get_device_type_image_src(cells[0]),
                             self._silk_dir + "monitor_green.png")
            self.assertEqual(self._page.get_device_type(cells[0]),
                             device_info[device_id])
            self.assertEqual(self._page.get_element_class_attribute(cells[1]),
                             "left device_name")
            self.assertNotEqual(self._page.get_text_of_element(cells[1]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[2]), "")
            self.assertEquals(self._page.check_for_span_type_tooltip(cells[3]),
                              "tooltip")
            self.assertNotEqual(self._page.get_text_of_element(cells[3]), "")
            self.assertEqual(self._page.get_form_edit_image_src(cells[4]),
                             self._silk_dir + "inherit.png")
            self.assertEquals(self._page.get_class_attribute_of_link(cells[5]),
                              "tooltip")
            self.assertNotEqual(self._page.get_text_of_element(cells[5]), "")
            self.assertEquals(self._page.get_class_attribute_of_link(cells[6]),
                              "tooltip")
            self.assertNotEqual(self._page.get_text_of_element(cells[6]), "")
            self.assertEquals(self._page.get_class_attribute_of_link(cells[7]),
                              "tooltip")
            self.assertNotEqual(self._page.get_text_of_element(cells[7]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[8]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[9]), "")
            self.assertEqual(self._page.get_config_device_img_src(cells[10]),
                             self._silk_dir + "pencil.png")
            self.assertEqual(self._page.get_refresh_arrow_image_src(cells[10]),
                             self._silk_dir + "arrow_refresh.png")
            self.assertEqual(self._page.get_identify_image_src(cells[10]),
                             self._silk_dir + "lightbulb.png")
            self.assertEqual(self._page.get_delete_image_src(cells[10]),
                             self._silk_dir + "delete.png")
            self.assertEqual(self._page.get_connect_device_src(cells[10]),
                             self._silk_dir + "connect_green.png")

    def test_search_fields_are_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertTrue(self._page.get_located_search_by_name())
        self.assertTrue(self._page.get_located_search_by_description())
        self.assertTrue(self._page.get_located_search_by_location())
