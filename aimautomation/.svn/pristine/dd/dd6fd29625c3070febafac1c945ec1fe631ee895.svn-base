'''
Created on 3 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage

class AimUserGroupViewPageFunctionsTest(BaseAimRegressionTest):
    
    search_term = "0"
    
    def test_add_user_group_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.click_add_user_group_button()
        self.assertEqual(self._page.get_text_of_page_header(), "User Groups > Add User Group")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.send_search_term_to_user_group_name_field(self.search_term)
        self._page.click_on_filter_user_groups_by_name()
        groups = self._page.get_list_of_user_groups()
        for group in groups:
            self.assertNotEqual(self._page.get_user_group_name(group).lower().find(self.search_term), -1)

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.send_search_term_to_user_group_name_field(self.search_term)
        self._page.click_on_filter_user_groups_by_name()
        filtered_groups = self._page.get_list_of_user_groups()
        for group in filtered_groups:
            self.assertNotEqual(self._page.get_user_group_name(group).lower().find(self.search_term), -1)
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
            self.assertNotEqual(self._page.get_user_group_name(group).lower().find(self.search_term), -1)
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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() <= user_names[counter + 1].lower())
    
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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() >= user_names[counter + 1].lower())
    
    def test_can_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        users = self._page.get_list_of_user_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for user in users:
                link_text = self._page.get_user_group_config_linktext(user)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "User Groups > Configure User Group")
        finally:
            page.driver.quit()
    
    def test_can_open_clone_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        users = self._page.get_list_of_user_groups()
        page = BasePage()
        page.open_AIM_homepage_on_base_url()
        page.login_as("admin", "password", False)
        try:
            for user in users:
                link_text = self._page.get_user_group_clone_linktext(user)
                page.driver.get(link_text)
                self.assertEqual(page.get_text_of_page_header(), "User Groups > Configure Cloned User Group")
        finally:
            page.driver.quit()
    
    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.check_for_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.check_for_batch_delete_checkbox())
    
    def test_can_open_and_cancel_delete_user_group_dialogue(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_user_groups_page()
        users = self._page.get_list_of_user_groups()
        for user in users:
            self._page.click_user_group_delete(user)
            self.assertTrue("Delete User Group" in self._page.get_delete_receiver_text_from_lightbox())
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
        self.assertTrue("Delete User Group" in self._page.get_lightbox_title_text())
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
        self._page.click_batch_delete_selector_for_user_group_element(users[-2])
        self._page.click_batch_delete_selector_for_user_group_element(users[-1])
        self._page.click_batch_delete_user_groups()
        self._page.click_lightbox_delete_button()
        users = self._page.get_list_of_users()
        users_after = len(users)
        self.assertTrue(users_before > users_after)
        self.reset_number_of_user_groups()
    
    def reset_number_of_user_groups(self):
        users = self._page.get_list_of_user_groups()
        if len(users) < 5:
            page = BasePage()
            page.open_AIM_homepage_on_base_url()
            page.login_as("admin", "password", False)
            try:
                counter = 5 - len(users)
                for counter in range(0, counter):
                    users = self._page.get_list_of_user_groups()
                    link_text = self._page.get_user_group_clone_linktext(users[-1])
                    name = self._page.get_user_group_name(users[-1])
                    name = name.split(" ")
                    name[1] = str(int(name[1]) + 1)
                    seperator = " "
                    page.driver.get(link_text)
                    page.set_user_group_name_via_config_page(seperator.join((name[0], name[1])))
                    page.click_save()
                    self._page.driver.refresh()
            finally:
                page.driver.quit()