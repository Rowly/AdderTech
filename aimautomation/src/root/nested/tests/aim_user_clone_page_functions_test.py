'''
Created on 2 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimUserClonePageFunctionsTest(BaseAimRegressionTest):
    
    def test_can_clone_existing_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_username(users[-1])[-5:], "_copy")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_username_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        username = self._page.get_user_username(users[-1])
        self._page.click_user_clone(users[-1])
        self._page.set_user_username_via_config_page(username + " edit")
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_username(users[-1]), username + " edit")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
        
    def test_can_change_first_name_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        firstname = self._page.get_user_firstname(users[-1])
        self._page.click_user_clone(users[-1])
        self._page.set_user_firstname_via_config_page(firstname + " edit")
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_firstname(users[-1]), firstname + " edit")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_last_name_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        lastname = self._page.get_user_lastname(users[-1])
        self._page.click_user_clone(users[-1])
        self._page.set_user_lastname_via_config_page(lastname + " edit")
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_lastname(users[-1]), lastname + " edit")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_email_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.set_user_email_via_config_page("new@email.com")
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self.assertEqual(self._page.get_user_email_from_config_page(), "new@email.com")
        self._page.driver.back()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_cannot_change_email_to_invalid_address(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.set_user_email_via_config_page("not valid")
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.is_ajax_error_message_displayed_for_user())
    
    def test_can_change_cloned_user_to_no_password_required(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.select_aim_admin_yes()
        self._page.select_user_no_password()
        username = self._page.get_user_username_from_config_page()
        self._page.click_save()
        self._page.ensure_logged_out()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as(username, "", False)
        self.assertTrue(self._page.get_located_dashboard_link())
        self._page.ensure_logged_out()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_cloned_user_password(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        username = self._page.get_user_username_from_config_page()
        password = "password"
        self._page.select_aim_admin_yes()
        self._page.set_user_password_via_config_page(password)
        self._page.set_user_password2_via_config_page(password)        
        self._page.click_save()
        self._page.ensure_logged_out()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as(username, password, False)
        self.assertTrue(self._page.get_located_dashboard_link())
        self._page.ensure_logged_out()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_cloned_user_to_suspended(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        username = self._page.get_user_username_from_config_page()
        password = "password"
        self._page.select_user_suspended_yes()
        self._page.select_aim_admin_yes()
        self._page.set_user_password_via_config_page(password)
        self._page.set_user_password2_via_config_page(password)    
        self._page.click_save()
        self._page.ensure_logged_out()
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as(username, password, False)
        self.assertEqual(self._page.get_login_error_message_text(), "The username and password you supplied are not valid")
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_cloned_user_exclusive_connection_status_to_no(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.select_user_exclusive_no()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password") 
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_connection_image_src(users[-1]), self._baseurl + "/admin/images/silk_icons/cross.png")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_cloned_user_exclusive_connection_status_to_global(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.select_user_exclusive_global()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password") 
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_connection_image_src(users[-1]), self._baseurl + "/admin/images/silk_icons/inherit.png")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_cloned_user_exclusive_connection_status_to_yes(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.select_user_exclusive_yes()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password") 
        self._page.click_save()
        users = self._page.get_list_of_users()
        self.assertEqual(self._page.get_user_connection_image_src(users[-1]), self._baseurl + "/admin/images/silk_icons/tick.png")
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_cloned_user_group_membership_of_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.add_user_to_usergroup_via_user_config_page()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password") 
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self.assertTrue(self._page.check_user_in_user_group_via_user_config_page())
        self._page.driver.back()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_channel_permissions_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self._page.remove_all_channels_from_user()
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.add_channel_permission_to_user_via_user_config_page()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password") 
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self.assertTrue(self._page.check_channel_permission_for_user_via_user_config_page())
        self._page.driver.back()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self._page.add_all_channel_permissions_to_user_via_user_config_page()
        self._page.click_save()
    
    def test_can_change_channel_group_permissions_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.add_channel_group_permission_to_user_via_user_config_page()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self.assertTrue(self._page.check_channel_group_permission_for_user_via_user_config_page())
        self._page.driver.back()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_receiver_permissions_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self._page.show_receiver_permissions()
        self._page.remove_all_receiver_permissions_from_user()
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.show_receiver_permissions()
        self._page.add_receiver_permission_to_user_via_user_config_page()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self._page.show_receiver_permissions()
        self.assertTrue(self._page.check_receiver_permission_for_user_via_user_config_page())
        self._page.driver.back()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()
    
    def test_can_change_receiver_group_permissions_of_cloned_user(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        users = self._page.get_list_of_users()
        self._page.click_user_clone(users[-1])
        self._page.show_receiver_permissions()
        self._page.add_receiver_group_permission_to_user_via_user_config_page()
        self._page.set_user_password_via_config_page("password")
        self._page.set_user_password2_via_config_page("password")
        self._page.click_save()
        users = self._page.get_list_of_users()
        self._page.click_user_config(users[-1])
        self._page.show_receiver_permissions()
        self.assertTrue(self._page.check_receiver_group_permission_for_user_via_user_config_page())
        self._page.driver.back()
        users = self._page.get_list_of_users()
        self._page.click_user_delete(users[-1])
        self._page.click_lightbox_delete_button()