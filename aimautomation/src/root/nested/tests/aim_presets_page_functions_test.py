'''
Created on 17 Jun 2013
@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimPresetsPageFunctionsTest(BaseAimRegressionTest):

    def test_subtab_links_operate_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        self._page.open_view_presets_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Presets")
        self._page.open_add_presets_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Presets > Add Preset")

    def test_add_preset_button_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        self._page.click_add_preset_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Presets > Add Preset")

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.verify_batch_delete_checkbox())
        for preset in self._page.get_list_of_presets():
            self.assertTrue(self._page.verify_batch_delete_preset(preset))
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.verify_batch_delete_checkbox())
        presets = self._page.get_list_of_presets()
        for preset in presets:
            self.assertFalse(self._page.verify_batch_delete_preset(preset))

    def test_can_connect_preset_as_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        for counter in range(0, len(presets)):
            p = presets[counter]
            self._page.click_preset_connect_view_only(p)
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertTrue("green_image_button"
                            in self._page.check_connect_view_only_button(p))
            self.assertTrue(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_disconnect(p)
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertFalse("green_image_button"
                             in self._page.check_connect_view_only_button(p))
            self.assertFalse(self._page.check_for_preset_disconnect_button(p))

    def test_can_connect_preset_as_shared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        for counter in range(0, len(presets)):
            p = presets[counter]
            self._page.click_preset_connect_shared(p)
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertTrue("green_image_button"
                            in self._page.check_connect_shared_button(p))
            self.assertTrue(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_disconnect(p)
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertFalse("green_image_button"
                             in self._page.check_connect_shared_button(p))
            self.assertFalse(self._page.check_for_preset_disconnect_button(p))

    def test_can_connect_preset_as_exclusive(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        for counter in range(0, len(presets)):
            p = presets[counter]
            self._page.click_preset_connect_exclusive(p)
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertTrue("green_image_button"
                            in self._page.check_connect_exclusive_button(p))
            self.assertTrue(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_disconnect(p)
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertFalse("green_image_button"
                             in self._page.check_connect_exclusive_button(p))
            self.assertFalse(self._page.check_for_preset_disconnect_button(p))

    def test_can_cycle_all_preset_connection_types(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        for counter in range(0, len(presets)):
            self._page.click_preset_connect_view_only(presets[counter])
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertTrue("green_image_button"
                            in self._page.check_connect_view_only_button(p))
            self.assertTrue(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_disconnect(presets[counter])
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertFalse("green_image_button"
                             in self._page.check_connect_view_only_button(p))
            self.assertFalse(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_connect_shared(presets[counter])
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertTrue("green_image_button"
                            in self._page.check_connect_shared_button(p))
            self.assertTrue(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_disconnect(presets[counter])
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertFalse("green_image_button"
                             in self._page.check_connect_shared_button(p))
            self.assertFalse(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_connect_exclusive(presets[counter])
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertTrue("green_image_button"
                            in self._page.check_connect_exclusive_button(p))
            self.assertTrue(self._page.check_for_preset_disconnect_button(p))
            self._page.click_preset_disconnect(presets[counter])
            presets = self._page.get_list_of_presets()
            p = presets[counter]
            self.assertFalse("green_image_button"
                             in self._page.check_connect_exclusive_button(p))
            self.assertFalse(self._page.check_for_preset_disconnect_button(p))

    def test_can_open_preset_config(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        for counter in range(0, len(presets)):
            presets = self._page.get_list_of_presets()
            self._page.click_preset_configure(presets[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Presets > Configure Preset")
            self._driver.back()

    def test_can_open_preset_clone(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        for counter in range(0, len(presets)):
            presets = self._page.get_list_of_presets()
            self._page.click_preset_clone(presets[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Presets > Configure Cloned Preset")
            self._driver.back()

    def test_can_cancel_preset_delete(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        presets_before = len(presets)
        self._page.click_preset_delete(presets[-1])
        self._page.click_cancel()
        presets = self._page.get_list_of_presets()
        presets_after = len(presets)
        self.assertEqual(presets_before, presets_after)

    def test_can_delete_preset(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        self.reset_number_of_presets()
        presets = self._page.get_list_of_presets()
        presets_before = len(presets)
        self._page.click_preset_delete(presets[-1])
        self._page.click_lightbox_delete_button()
        presets = self._page.get_list_of_presets()
        presets_after = len(presets)
        self.assertTrue(presets_before > presets_after)
        self.reset_number_of_presets()

    def reset_number_of_presets(self):
        presets = self._page.get_list_of_presets()
        if len(presets) < 4:
            counter = 4 - len(presets)
            for counter in range(0, counter):
                presets = self._page.get_list_of_presets()
                last_name = self._page.get_preset_name(presets[-1])
                last_desc = self._page.get_preset_description(presets[-1])
                last_name = last_name.split(" ")
                last_desc = last_desc.split(" ")
                last_name[1] = str(int(last_name[1]) + 1)
                last_desc[1] = str(int(last_desc[1]) + 1)
                self._page.click_preset_clone(presets[-1])
                name = " ".join((last_name[0], last_name[1]))
                self._page.set_preset_name_via_config_page(name)
                desc = " ".join((last_desc[0], last_desc[1]))
                self._page.set_preset_description_via_config_page(desc)
                self._page.click_save()

    """
    Default appearances
    """
    def test_preset_page_opened_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Presets")
        self.assertEqual(self._page.get_text_of_view_presets_link(),
                         "View Presets")
        self.assertEqual(self._page.get_text_of_add_preset_link(),
                         "Add Preset")

    def test_presets_are_shown_in_paginated_table(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self.assertTrue(len(presets) >= 1)
        total_presets = self._page.get_pagination_total()
        if int(total_presets) <= 20:
            self.assertTrue(len(presets) <= int(total_presets))
        elif int(total_presets) > 20:
            pass

    def test_each_preset_row_comprises_correct_elements(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        presets = self._page.get_list_of_presets()
        self.assertTrue(len(presets) >= 1)
        for preset in presets:
            cells = self._page.get_cell_elements(preset)
            self.assertEqual(len(cells), 6)
            self.assertEqual(self._page.get_element_class_attribute(cells[0]),
                             "left connection_preset_name_id")
            self.assertNotEqual(self._page.get_text_of_element(cells[0]), "")
            self.assertEqual(self._page.get_element_class_attribute(cells[1]),
                             "left")
            self.assertNotEqual(self._page.get_text_of_element(cells[1]), "")
            self.assertEqual(self._page.get_form_edit_image_src(cells[2]),
                             self._silk_dir + "inherit.png")
            self.assertNotEqual(self._page.get_text_of_element(cells[3]), "")
            self.assertEqual(self._page.get_preset_view_only_img_src(cells[4]),
                             self._silk_dir + "eye.png")
            self.assertEqual(self._page.get_preset_shared_img_src(cells[4]),
                             self._silk_dir + "multicast.png")
            self.assertEqual(self._page.get_preset_exclusive_img_src(cells[4]),
                             self._silk_dir + "lock.png")
            self.assertEqual(self._page.get_preset_configure_img_src(cells[5]),
                             self._silk_dir + "pencil.png")
            self.assertEqual(self._page.get_preset_clone_image_src(cells[5]),
                             self._silk_dir + "page_copy_green.png")
            self.assertEqual(self._page.get_preset_delete_image_src(cells[5]),
                             self._silk_dir + "delete.png")

    def test_search_fields_are_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        self.assertTrue(self._page.get_preset_search_by_name())
        self.assertTrue(self._page.get_preset_search_by_description())
