'''
Created on 26 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimUsersViewPageFunctionsTest(BaseAimRegressionTest):

    search_term = "admin"

    def test_all_subtab_links_operate_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_users_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Users")
        self._page.open_add_user_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Users > Add User")
        self._page.open_view_user_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "User Groups")
        self._page.open_add_user_group_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "User Groups > Add User Group")
        self._page.open_active_directory_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Import Users from Active Directory")

    def test_username_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_users_page()
        self._page.send_search_term_to_user_username_field(self.search_term)
        self._page.click_on_filter_users_by_username()
        users = self._page.get_list_of_users()
        for user in users:
            name = self._page.get_user_username(user).lower()
            self.assertNotEqual(name.find(self.search_term), -1)

    def test_username_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_username_field(self.search_term)
        self._page.click_on_filter_users_by_username()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            name = self._page.get_user_username(user).lower()
            self.assertNotEqual(name.find(self.search_term), -1)
        self._page.click_on_remove_user_username_filter()
        non_filtered_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_users) <= len(non_filtered_users))

    def test_username_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_username_field(self.search_term)
        self._page.click_on_filter_users_by_username()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            name = self._page.get_user_username(user).lower()
            self.assertNotEqual(name.find(self.search_term), -1)
        self._page.clear_user_usernames_filter()
        self._page.click_on_filter_users_by_username()
        non_filtered_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_users) <= len(non_filtered_users))

    def test_firstname_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_users_page()
        self._page.send_search_term_to_user_firstname_field(self.search_term)
        self._page.click_on_filter_users_by_firstname()
        users = self._page.get_list_of_users()
        for user in users:
            first_name = self._page.get_user_firstname(user).lower()
            self.assertNotEqual(first_name.find(self.search_term), -1)

    def test_firstname_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_firstname_field(self.search_term)
        self._page.click_on_filter_users_by_firstname()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            first_name = self._page.get_user_firstname(user).lower()
            self.assertNotEqual(first_name.find(self.search_term), -1)
        self._page.click_on_remove_user_firstname_filter()
        non_filtered_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_users) <= len(non_filtered_users))

    def test_firstname_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_firstname_field(self.search_term)
        self._page.click_on_filter_users_by_firstname()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            first_name = self._page.get_user_firstname(user).lower()
            self.assertNotEqual(first_name.find(self.search_term), -1)
        self._page.clear_user_firstnames_filter()
        self._page.click_on_filter_users_by_firstname()
        non_filtered_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_users) <= len(non_filtered_users))

    def test_lastname_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_users_page()
        self._page.send_search_term_to_user_lastname_field(self.search_term)
        self._page.click_on_filter_users_by_lastname()
        users = self._page.get_list_of_users()
        for user in users:
            last_name = self._page.get_user_lastname(user).lower()
            self.assertNotEqual(last_name.find(self.search_term), -1)

    def test_lastname_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_lastname_field(self.search_term)
        self._page.click_on_filter_users_by_lastname()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            last_name = self._page.get_user_lastname(user).lower()
            self.assertNotEqual(last_name.find(self.search_term), -1)
        self._page.click_on_remove_user_lastname_filter()
        non_filtered_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_users) <= len(non_filtered_users))

    def test_lastname_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_lastname_field(self.search_term)
        self._page.click_on_filter_users_by_lastname()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            last_name = self._page.get_user_lastname(user).lower()
            self.assertNotEqual(last_name.find(self.search_term), -1)
        self._page.clear_user_lastnames_filter()
        self._page.click_on_filter_users_by_lastname()
        non_filtered_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_users) <= len(non_filtered_users))

    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_username_field(self.search_term)
        self._page.click_on_filter_users_by_username()
        filtered_name = self._page.get_list_of_users()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_users()
        self.assertTrue(len(filtered_name) <= len(no_filter))

        self._page.send_search_term_to_user_firstname_field(self.search_term)
        self._page.click_on_filter_users_by_firstname()
        filtered_firstname = self._page.get_list_of_users()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_users()
        self.assertTrue(len(filtered_firstname) <= len(no_filter))

        self._page.send_search_term_to_user_lastname_field(self.search_term)
        self._page.click_on_filter_users_by_lastname()
        filtered_lastname = self._page.get_list_of_users()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_users()
        self.assertTrue(len(filtered_lastname) <= len(no_filter))

    def test_can_sort_usernames_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_on_ascend_user_usernames()
        sorted_users = self._page.get_list_of_users()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_username(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_firstnames_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_on_ascend_user_firstnames()
        sorted_users = self._page.get_list_of_users()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_firstname(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_lastnames_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_on_ascend_user_lastnames()
        sorted_users = self._page.get_list_of_users()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_lastname(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_usernames_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_on_decend_user_usernames()
        sorted_users = self._page.get_list_of_users()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_username(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_firstnames_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_on_decend_user_firstnames()
        sorted_users = self._page.get_list_of_users()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_firstname(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_lastnames_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_on_decend_user_lastnames()
        sorted_users = self._page.get_list_of_users()
        user_names = []
        if len(sorted_users) > 1:
            for user in sorted_users:
                user_names.append(self._page.get_user_lastname(user))
            for counter in range(0, (len(user_names) - 1)):
                prior = user_names[counter].lower()
                latter = user_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_open_user_configuration(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        for counter in range(0, len(users)):
            users = self._page.get_list_of_users()
            self._page.click_user_config(users[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Users > Configure User")
            self._driver.back()

    def test_can_open_user_clone(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        for counter in range(0, len(users)):
            users = self._page.get_list_of_users()
            self._page.click_user_clone(users[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Users > Configure Cloned User")
            self._driver.back()

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.verify_batch_delete_checkbox())

    def test_can_cancel_user_delete(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self.assertTrue("Delete User" in self._page.get_lightbox_title_text())
        self._page.click_lightbox_cancel_button()
        self.assertFalse(self._page.check_lightbox_visibility())

    def test_can_delete_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self.reset_test_users()
        users = self._page.get_list_of_users()
        users_before = len(users)
        self._page.click_user_delete(users[-1])
        self.assertTrue("Delete User" in self._page.get_lightbox_title_text())
        self._page.click_lightbox_delete_button()
        self.assertFalse(self._page.check_lightbox_visibility())
        users = self._page.get_list_of_users()
        users_after = len(users)
        self.assertTrue(users_before > users_after)
        self.reset_test_users()

    def test_can_batch_delete_users(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self.reset_test_users()
        self._page.click_batch_delete_mode()
        users = self._page.get_list_of_users()
        users_before = len(users)
        self._page.click_batch_delete_selector_for_user_element(users[-2])
        self._page.click_batch_delete_selector_for_user_element(users[-1])
        self._page.click_batch_delete_users()
        self._page.click_lightbox_delete_button()
        users = self._page.get_list_of_users()
        users_after = len(users)
        self.assertTrue(users_before > users_after)
        self.reset_test_users()

    def reset_test_users(self):
        fixed_users = ["admin", "anon", "api_anon"]
        users = self._page.get_list_of_users()
        usernames = []
        for user in users:
            usernames.append(self._page.get_user_username(user))
        test_users = list(set(usernames) - set(fixed_users))
        if len(test_users) < 5:
            counter = 5 - len(test_users)
            for counter in range(0, counter):
                users = self._page.get_list_of_users()
                username = self._page.get_user_username(users[-1])
                username = username.split(" ")
                username[1] = str(int(username[1]) + 1)
                self._page.click_user_clone(users[-1])
                name = " ".join((username[0], username[1]))
                self._page.set_user_username_via_config_page(name)
                self._page.set_user_password_via_config_page("password")
                self._page.set_user_password2_via_config_page("password")
                self._page.click_save()

    """
    Default appearances
    """
    def test_users_page_opened_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Users")
        self.assertEqual(self._page.get_text_of_view_users_link(),
                         "View Users")
        self.assertEqual(self._page.get_text_of_add_user_link(),
                         "Add User")
        self.assertEqual(self._page.get_text_of_view_user_groups_link(),
                         "View User Groups")
        self.assertEqual(self._page.get_text_of_add_user_group_link(),
                         "Add User Group")
        self.assertEqual(self._page.get_text_of_active_directory_link(),
                         "Active Directory")

    def test_users_are_shown_in_paginated_table(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_receivers()
        self.assertTrue(len(users) >= 1)
        total_users = self._page.get_pagination_total()
        if int(total_users) <= 20:
            self.assertTrue(len(users) <= int(total_users))
        elif int(total_users) > 20:
            pass

    def test_each_user_row_comprises_correct_elements(self):
        ignore_names = ["admin", "anon", "api_anon"]
        remote_osd_srcs = [self._silk_dir + "inherit.png",
                           self._silk_dir + "tick.png"]
        suspended_srcs = [self._silk_dir + "cross.png",
                          self._silk_dir + "tick.png"]
        aim_admin_srcs = [self._silk_dir + "cross.png",
                          self._silk_dir + "tick.png"]
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self.assertTrue(len(users) >= 1)
        for user in users:
            cells = self._page.get_cell_elements(user)
            self.assertEqual(len(cells), 12)
            self.assertEquals(self._page.get_element_class_attribute(cells[1]),
                              "left u_username")
            self.assertNotEqual(self._page.get_text_of_element(cells[1]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[2]), "")
            self.assertNotEqual(self._page.get_text_of_element(cells[3]), "")
            self.assertEquals(self._page.get_class_attribute_of_link(cells[4]),
                              "tooltip")
            self.assertEquals(self._page.get_class_attribute_of_link(cells[5]),
                              "tooltip")
            self.assertEquals(self._page.get_class_attribute_of_link(cells[6]),
                              "tooltip")
            src = self._page.get_user_allowed_connections_img_src(cells[7])
            self.assertEqual(src, self._silk_dir + "inherit.png")
            self.assertTrue(self._page.get_user_remote_osd_image_src(cells[8])
                            in remote_osd_srcs)
            self.assertTrue(self._page.get_user_suspended_image_src(cells[9])
                            in suspended_srcs)
            self.assertTrue(self. _page.get_user_aim_admin_image_src(cells[10])
                            in aim_admin_srcs)
            src = self._page.get_configure_channel_img_src(cells[11])
            self.assertEqual(src, self._silk_dir + "pencil.png")
            self.assertEqual(self._page.get_clone_channel_img_src(cells[11]),
                             self._silk_dir + "page_copy_green.png")
            if self._page.get_user_username(user) not in ignore_names:
                src = self._page.get_delete_channel_img_src(cells[11])
                self.assertEqual(src, self._silk_dir + "delete.png")

    def test_search_fields_are_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self.assertTrue(self._page.get_located_search_by_username())
        self.assertTrue(self._page.get_located_search_by_firstname())
        self.assertTrue(self._page.get_located_search_by_lastname())
