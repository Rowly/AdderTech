'''
Created on 3 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimUserGroupViewPageFunctionsTest(BaseAimRegressionTest):

    search_term = "0"

    def test_add_user_group_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.click_add_user_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "User Groups > Add User Group")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.send_search_term_to_user_group_name_field(self.search_term)
        self._page.click_on_filter_user_groups_by_name()
        groups = self._page.get_list_of_user_groups()
        for group in groups:
            name = self._page.get_user_group_name(group).lower()
            self.assertNotEqual(name.find(self.search_term), -1)

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.send_search_term_to_user_group_name_field(self.search_term)
        self._page.click_on_filter_user_groups_by_name()
        filtered_groups = self._page.get_list_of_user_groups()
        for group in filtered_groups:
            name = self._page.get_user_group_name(group).lower()
            self.assertNotEqual(name.find(self.search_term), -1)
        self._page.click_on_remove_user_groups_name_filter()
        non_filtered_groups = self._page.get_list_of_user_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.send_search_term_to_user_group_name_field(self.search_term)
        self._page.click_on_filter_user_groups_by_name()
        filtered_groups = self._page.get_list_of_user_groups()
        for group in filtered_groups:
            name = self._page.get_user_group_name(group).lower()
            self.assertNotEqual(name.find(self.search_term), -1)
        self._page.clear_user_groups_names_filter()
        self._page.click_on_filter_user_groups_by_name()
        non_filtered_groups = self._page.get_list_of_user_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.click_on_ascend_user_group_names()
        sorted_users = self._page.get_list_of_user_groups()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_group_name(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                prior = user_names[counter + 1].lower()
                self.assertTrue(prior <= prior)

    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.click_on_decend_user_group_names()
        sorted_users = self._page.get_list_of_user_groups()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_group_name(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        users = self._page.get_list_of_user_groups()
        for counter in range(0, len(users)):
            users = self._page.get_list_of_user_groups()
            self._page.click_user_group_config(users[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "User Groups > Configure User Group")
            self._driver.back()

    def test_can_open_clone_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        users = self._page.get_list_of_user_groups()
        for counter in range(0, len(users)):
            users = self._page.get_list_of_user_groups()
            self._page.click_user_group_clone(users[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "User Groups > Configure Cloned User Group")
            self._driver.back()

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.verify_batch_delete_checkbox())

    def test_can_open_and_cancel_delete_user_group_dialogue(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        users = self._page.get_list_of_user_groups()
        for user in users:
            self._page.click_user_group_delete(user)
            text = self._page.get_lightbox_title_text()
            self.assertTrue("Delete User Group" in text)
            self._page.click_lightbox_cancel_button()
            self.assertFalse(self._page.check_lightbox_visibility())

    def test_can_delete_user_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self.reset_number_of_user_groups()
        users = self._page.get_list_of_user_groups()
        user_groups_before = len(users)
        self._page.click_user_group_delete(users[-1])
        text = self._page.get_lightbox_title_text()
        self.assertTrue("Delete User Group" in text)
        self._page.click_lightbox_delete_button()
        self.assertFalse(self._page.check_lightbox_visibility())
        users = self._page.get_list_of_user_groups()
        user_groups_after = len(users)
        self.assertTrue(user_groups_before > user_groups_after)
        self.reset_number_of_user_groups()

    def test_can_batch_delete_user_groups(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self.reset_number_of_user_groups()
        self._page.click_batch_delete_mode()
        users = self._page.get_list_of_user_groups()
        users_before = len(users)
        self._page.click_batch_delete_user_group(users[-2])
        self._page.click_batch_delete_user_group(users[-1])
        self._page.click_batch_delete_user_groups()
        self._page.click_lightbox_delete_button()
        users = self._page.get_list_of_users()
        users_after = len(users)
        self.assertTrue(users_before > users_after)
        self.reset_number_of_user_groups()

    def reset_number_of_user_groups(self):
        users = self._page.get_list_of_user_groups()
        if len(users) < 5:
            counter = 5 - len(users)
            for counter in range(0, counter):
                users = self._page.get_list_of_user_groups()
                name = self._page.get_user_group_name(users[-1])
                name = name.split(" ")
                name[1] = str(int(name[1]) + 1)
                self._page.click_user_group_clone(users[-1])
                name = " ".join((name[0], name[1]))
                self._page.set_user_group_name_via_config_page(name)
                self._page.click_save()

    """
    Default Appearances
    """
    def test_user_group_page_opened_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "User Groups")

    def test_user_groups_are_shown_in_paginated_table(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        groups = self._page.get_list_of_user_groups()
        self.assertTrue(len(groups) >= 1)
        total_groups = self._page.get_pagination_total()
        if int(total_groups) <= 20:
            self.assertTrue(len(groups) <= int(total_groups))
        elif int(total_groups) > 20:
            pass

    def test_each_user_group_row_comprises_correct_elements(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        groups = self._page.get_list_of_user_groups()
        self.assertTrue(len(groups) >= 1)
        for group in groups:
            cells = self._page.get_cell_elements(group)
            self.assertEqual(len(cells), 8)
            self.assertEqual(self._page.get_element_class_attribute(cells[1]),
                             "left user_group_name")
            self.assertNotEqual(self._page.get_text_of_element(cells[1]), "")
            self.assertEqual(self._page.get_user_group_users_class(cells[2]),
                             "tooltip")
            self.assertEqual(self._page.get_u_group_channels_class(cells[3]),
                             "tooltip")
            self.assertEqual(self._page.get_u_group_receivers_class(cells[4]),
                             "tooltip")
            self.assertEqual(self._page.get_form_edit_image_src(cells[5]),
                             self._silk_dir + "inherit.png")
            self.assertEqual(self._page.get_form_edit_image_src(cells[6]),
                             self._silk_dir + "inherit.png")
            self.assertEqual(self._page.get_u_group_config_img_src(cells[7]),
                             self._silk_dir + "pencil.png")
            self.assertEqual(self._page.get_user_group_clone_img_src(cells[7]),
                             self._silk_dir + "page_copy_green.png")
            self.assertEqual(self._page.get_u_group_delete_img_src(cells[7]),
                             self._silk_dir + "delete.png")

    def test_search_fields_are_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self.assertTrue(self._page.get_user_group_search_by_name())
