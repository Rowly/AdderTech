'''
Created on 3 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimTransmittersPageDefaultTest(BaseAimRegressionTest):

    def test_transmitter_page_opened_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Transmitters")
        self.assertEqual(self._page.get_text_of_view_transmitters_link(),
                         "View Transmitters")
        self.assertEqual(self._page.get_text_of_update_firmware_link(),
                         "Update Firmware")

    def test_transmitters_are_shown_in_paginated_table(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(transmitters) >= 1)
        total_transmitters = self._page.get_pagination_total()
        if int(total_transmitters) <= 20:
            self.assertTrue(len(transmitters) <= int(total_transmitters))
        elif int(total_transmitters) > 20:
            pass

    def test_each_transmitter_row_comprises_correct_elements(self):
        device_info = self._page.get_device_version_via_api()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        transmitters = self._page.get_list_of_transmitters()
        self.assertTrue(len(transmitters) >= 1)
        for transmitter in transmitters:
            row_id = self._page.get_row_id_of_transmitter(transmitter)
            device_id = self._page.get_device_id_from_row_id(row_id)
            cells = self._page.get_cell_elements(transmitter)
            self.assertEqual(len(cells), 10)
            self.assertEquals(self._page.check_for_span_type_tooltip(cells[0]),
                              "tooltip")
            self.assertEquals(self._page.get_device_type(cells[0]),
                              device_info[device_id])
            self.assertEqual(self._page.get_device_type_image_src(cells[0]),
                             self._silk_dir + "computer_purple.png")
            self.assertTrue(self._page.get_tx_status_img_src(transmitter)
                            in self._device_status_imgs)
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
            self.assertNotEqual(self._page.get_text_of_element(cells[6]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[7]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[8]), "")
            self.assertEqual(self._page.get_config_device_img_src(cells[9]),
                             self._silk_dir + "pencil.png")
            self.assertEqual(self._page.get_refresh_arrow_image_src(cells[9]),
                             self._silk_dir + "arrow_refresh.png")
            self.assertEqual(self._page.get_identify_image_src(cells[9]),
                             self._silk_dir + "lightbulb.png")
            self.assertEqual(self._page.get_delete_image_src(cells[9]),
                             self._silk_dir + "delete.png")

    def test_search_fields_are_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertTrue(self._page.get_located_search_by_name())
        self.assertTrue(self._page.get_located_search_by_description())
        self.assertTrue(self._page.get_located_search_by_location())
