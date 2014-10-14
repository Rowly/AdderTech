'''
Created on 26 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.pages.base_page import BasePage

class AimUsersViewPageFunctionsTest(BaseAimRegressionTest):
    
    search_term = "admin"
    
    def test_all_subtab_links_operate_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_users_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Users")
        self._page.open_add_user_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Users > Add User")
        self._page.open_view_user_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "User Groups")
        self._page.open_add_user_group_page()
        self.assertEqual(self._page.get_text_of_page_header(), "User Groups > Add User Group")
        self._page.open_active_directory_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Import Users from Active Directory")
    
    def test_username_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.open_view_users_page()
        self._page.send_search_term_to_user_username_field(self.search_term)
        self._page.click_on_filter_users_by_username()
        users = self._page.get_list_of_users()
        for user in users:
            self.assertNotEqual(self._page.get_user_username(user).lower().find(self.search_term), -1)
    
    def test_username_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_username_field(self.search_term)
        self._page.click_on_filter_users_by_username()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            self.assertNotEqual(self._page.get_user_username(user).lower().find(self.search_term), -1)
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
            self.assertNotEqual(self._page.get_user_username(user).lower().find(self.search_term), -1)
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
            self.assertNotEqual(self._page.get_user_firstname(user).lower().find(self.search_term), -1)
        
    def test_firstname_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_firstname_field(self.search_term)
        self._page.click_on_filter_users_by_firstname()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            self.assertNotEqual(self._page.get_user_firstname(user).lower().find(self.search_term), -1)
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
            self.assertNotEqual(self._page.get_user_firstname(user).lower().find(self.search_term), -1)
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
            self.assertNotEqual(self._page.get_user_lastname(user).lower().find(self.search_term), -1)
    
    def test_lastname_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.send_search_term_to_user_lastname_field(self.search_term)
        self._page.click_on_filter_users_by_lastname()
        filtered_users = self._page.get_list_of_users()
        for user in filtered_users:
            self.assertNotEqual(self._page.get_user_lastname(user).lower().find(self.search_term), -1)
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
            self.assertNotEqual(self._page.get_user_lastname(user).lower().find(self.search_term), -1)
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
        filtered_by_name_users = self._page.get_list_of_users()
        self._page.click_on_remove_filters()
        remove_filter_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_by_name_users) <= len(remove_filter_users))
        self._page.send_search_term_to_user_firstname_field(self.search_term)
        self._page.click_on_filter_users_by_firstname()
        filtered_by_firstname_users = self._page.get_list_of_users()
        self._page.click_on_remove_filters()
        remove_filter_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_by_firstname_users) <= len(remove_filter_users))
        self._page.send_search_term_to_user_lastname_field(self.search_term)
        self._page.click_on_filter_users_by_lastname()
        filtered_by_lastname_users = self._page.get_list_of_users()
        self._page.click_on_remove_filters()
        remove_filter_users = self._page.get_list_of_users()
        self.assertTrue(len(filtered_by_lastname_users) <= len(remove_filter_users))

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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() <= user_names[counter + 1].lower())

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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() <= user_names[counter + 1].lower())

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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() <= user_names[counter + 1].lower())
        
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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() >= user_names[counter + 1].lower())

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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() >= user_names[counter + 1].lower())

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
            counter = 0
            for counter in range((len(user_names) - 1)):
                self.assertTrue(user_names[counter].lower() >= user_names[counter + 1].lower())
        
    def test_can_open_user_configuration(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        for user in users:
            link_text = self._page.get_user_config_linktext(user)
            page = BasePage()
            page.driver.get(link_text)
            page.login_as("admin", "password", False)
            self.assertEqual(page.get_text_of_page_header(), "Users > Configure User")
            page.driver.quit()

    def test_can_open_user_clone(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        for user in users:
            link_text = self._page.get_user_clone_linktext(user)
            page = BasePage()
            page.driver.get(link_text)
            page.login_as("admin", "password", False)
            self.assertEqual(page.get_text_of_page_header(), "Users > Configure Cloned User")
            page.driver.quit()
    
    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.check_for_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.check_for_batch_delete_checkbox())
    
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
                link_text = self._page.get_user_clone_linktext(users[-1])
                username = self._page.get_user_username(users[-1])
                username = username.split(" ")
                username[1] = str(int(username[1]) + 1)
                seperator = " "
                page = BasePage()
                page.driver.get(link_text)
                page.login_as("admin", "password", False)
                page.set_user_username_via_config_page(seperator.join((username[0], username[1])))
                page.set_user_password_via_config_page("password")
                page.set_user_password2_via_config_page("password")
                page.click_save()
                page.driver.quit()
                self._page.driver.refresh()
                