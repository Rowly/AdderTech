'''
Created on 14 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimAddReceiverGroupPageFunctionsTest(BaseAimRegressionTest):
    
    def test_cannot_create_receiver_group_without_a_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self.assertFalse(self._page.is_ajax_error_message_displayed_for_receiver_group())
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.is_ajax_error_message_displayed_for_receiver_group())
    
    def test_can_create_receiver_group_with_login_required(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_login_required_for_receiver_group_no()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Login Required", "rg_login_required_0"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_login_required_for_receiver_group_yes()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Login Required", "rg_login_required_1"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_login_required_for_receiver_group_global()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Login Required", "rg_login_required_-1"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()

    def test_can_create_receiver_group_with_enable_osd_alerts(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_enable_osd_alerts_for_receiver_group_no()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_0"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_enable_osd_alerts_for_receiver_group_yes()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_1"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_enable_osd_alerts_for_receiver_group_global()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable receiver OSD Alerts", "rg_osd_alerts_-1"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()


    def test_can_create_receiver_group_with_video_compatibility_check(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_enable_video_compatibility_for_receiver_group_no()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_0"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_enable_video_compatibility_for_receiver_group_yes()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_1"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.select_enable_video_compatibility_for_receiver_group_global()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.is_option_selected_by_div_text_and_id("Enable Video Compatibility Check", "rg_video_compatibility_check_-1"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        
    def test_can_create_receiver_group_with_one_receiver(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        before_added_receivers = self._page.get_list_of_non_member_receivers_for_group()
        before_added_receiver_names = []
        for receiver in before_added_receivers:
            before_added_receiver_names.append(receiver.text)
        self._page.add_member_receiver_to_receiver_group(before_added_receiver_names[0])
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        added_receivers = self._page.get_list_of_member_receivers_in_group()
        added_receiver_names = []
        for added_receiver in added_receivers:
            added_receiver_names.append(added_receiver.text)
#         self._page.click_cancel() #cancel button is missing from config group page!
        for counter in range(0, len(added_receiver_names)):
            self.assertTrue(added_receiver_names[counter] in before_added_receiver_names)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()

    def test_can_create_receiver_group_with_all_receivers(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        before_added_receivers = self._page.get_list_of_non_member_receivers_for_group()
        before_added_receiver_names = []
        for receiver in before_added_receivers:
            before_added_receiver_names.append(receiver.text)
        self._page.add_all_receivers_to_receiver_group()
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        added_receivers = self._page.get_list_of_member_receivers_in_group()
        added_receiver_names = []
        for added_receiver in added_receivers:
            added_receiver_names.append(added_receiver.text)
#         self._page.click_cancel() #cancel button is missing from config group page!
        for counter in range(0, len(added_receiver_names)):
            self.assertTrue(added_receiver_names[counter] in before_added_receiver_names)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        
    def test_can_change_user_permissions_of_receiver_group(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.show_user_permissions()
        user_name = self._page.get_first_user_name_from_add_select()
        self._page.add_user_to_receiver_group(user_name)
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self._page.show_user_permissions()
        self.assertTrue(self._page.check_user_has_receiver_group_permission(user_name))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
        
    def test_can_create_receiver_group_with_user_group(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(), "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name_via_config_page(name)
        self._page.set_receiver_group_description_via_config_page(desc)
        self._page.show_user_permissions()
        user_group_name = self._page.get_first_user_group_name_from_add_select()
        self._page.add_user_group_to_receiver_group(user_group_name)
        self._page.click_save()
        self._page.check_for_error_message("configure_receiver_group_ajax_message")
        self._page.confirm_no_longer_on_receiver_group_add_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self._page.show_user_permissions()
        self.assertTrue(self._page.check_user_group_has_receiver_group_permission(user_group_name))
#         self._page.click_cancel() #cancel button is missing from config group page!
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receivers()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()