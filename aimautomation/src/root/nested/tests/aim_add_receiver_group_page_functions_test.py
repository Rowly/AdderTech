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
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.click_save_ignore_warnings()
        displayed = self._page.is_error_message_displayed_for_rx_group()
        self.assertTrue(displayed)

    def test_can_create_receiver_group_with_login_required(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_login_required_for_receiver_group_no()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self.assertTrue(self._page.get_login_required_for_receiver_group("no"))
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

        self._page.open_add_receiver_groups_page()
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_login_required_for_receiver_group_yes()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        state = self._page.get_login_required_for_receiver_group("yes")
        self.assertTrue(state)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

        self._page.open_add_receiver_groups_page()
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_login_required_for_receiver_group_global()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        state = self._page.get_login_required_for_receiver_group("global")
        self.assertTrue(state)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_receiver_group_with_enable_osd_alerts(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_enable_osd_alerts_for_receiver_group_no()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        state = self._page.get_enabled_osd_alerts_for_receiver_group("no")
        self.assertTrue(state)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

        self._page.open_add_receiver_groups_page()
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_enable_osd_alerts_for_receiver_group_yes()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        state = self._page.get_enabled_osd_alerts_for_receiver_group("yes")
        self.assertTrue(state)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

        self._page.open_add_receiver_groups_page()
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_enable_osd_alerts_for_receiver_group_global()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        state = self._page.get_enabled_osd_alerts_for_receiver_group("global")
        self.assertTrue(state)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_receiver_group_with_video_compatibility_check(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_enable_video_compatibility_for_receiver_group_no()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        s = self._page.get_enable_video_compatibility_for_rx_group("no")
        self.assertTrue(s)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

        self._page.open_add_receiver_groups_page()
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_enable_video_compatibility_for_receiver_group_yes()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        s = self._page.get_enable_video_compatibility_for_rx_group("yes")
        self.assertTrue(s)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

        self._page.open_add_receiver_groups_page()
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.select_enable_video_compatibility_for_receiver_group()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        s = self._page.get_enable_video_compatibility_for_rx_group("global")
        self.assertTrue(s)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_receiver_group_with_one_receiver(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        before = self._page.get_list_of_non_member_receivers_for_group()
        self._page.add_member_receiver_to_receiver_group(before[0])
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        added_receivers = self._page.get_list_of_member_receivers_in_group()
        for counter in range(0, len(added_receivers)):
            self.assertTrue(added_receivers[counter] in before)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

    def test_can_create_receiver_group_with_all_receivers(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        before = self._page.get_list_of_non_member_receivers_for_group()
        self._page.add_all_receivers_to_receiver_group()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        added_receivers = self._page.get_list_of_member_receivers_in_group()
        for counter in range(0, len(added_receivers)):
            self.assertTrue(added_receivers[counter] in before)
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_user_permissions_of_receiver_group(self):
        name = "new group"
        desc = "new desc"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_add_receiver_groups_page()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.show_user_permissions()
        self._page.add_user_to_receiver_group("user 0")
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self._page.show_user_permissions()
        self.assertTrue("user 0"
                        in self._page.get_all_users_for_receiver_group())
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
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")
        self._page.set_receiver_group_name(name)
        self._page.set_receiver_group_description(desc)
        self._page.show_user_permissions()
        self._page.add_user_group_to_receiver_group("group 0")
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[-1])
        self._page.show_user_permissions()
        self.assertTrue("group 0"
                        in self._page.get_selected_user_groups_of_rx_group())
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receivers()
        self._page.click_receiver_group_delete(groups[-1])
        self._page.click_lightbox_delete_button()
        self._page.check_lightbox_visibility()
