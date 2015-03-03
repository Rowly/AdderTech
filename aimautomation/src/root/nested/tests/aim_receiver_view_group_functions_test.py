'''
Created on 12 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimReceiverViewGroupFunctionsTest(BaseAimRegressionTest):

    def test_add_receiver_group_button_opens_correct_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self._page.click_add_receiver_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Add Receiver Group")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        search_term = self._page.get_receiver_group_name(groups[0])
        self._page.send_search_term_to_receiver_group_name_field(search_term)
        self._page.click_on_filter_receiver_groups_by_name()
        groups = self._page.get_list_of_receiver_groups()
        for group in groups:
            name = self._page.get_receiver_group_name(group).lower()
            self.assertNotEqual(name.find(search_term), -1)

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        search_term = self._page.get_receiver_group_name(groups[0])
        self._page.send_search_term_to_receiver_group_name_field(search_term)
        self._page.click_on_filter_receiver_groups_by_name()
        filtered_groups = self._page.get_list_of_receiver_groups()
        for group in filtered_groups:
            name = self._page.get_receiver_group_name(group).lower()
            self.assertNotEqual(name.find(search_term), -1)
        self._page.click_on_remove_receiver_groups_name_filter()
        non_filtered_groups = self._page.get_list_of_receiver_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        search_term = self._page.get_receiver_group_name(groups[0])
        self._page.send_search_term_to_receiver_group_name_field(search_term)
        self._page.click_on_filter_receiver_groups_by_name()
        filtered_groups = self._page.get_list_of_receiver_groups()
        for group in filtered_groups:
            name = self._page.get_receiver_group_name(group).lower()
            self.assertNotEqual(name.find(search_term), -1)
        self._page.clear_receiver_groups_names_filter()
        self._page.click_on_filter_receiver_groups_by_name()
        non_filtered_groups = self._page.get_list_of_receiver_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        search_term = self._page.get_receiver_group_description(groups[0])
        self._page.send_search_to_receiver_group_desc_field(search_term)
        self._page.click_on_filter_receiver_groups_by_description()
        groups = self._page.get_list_of_receiver_groups()
        for group in groups:
            desc = self._page.get_receiver_group_description(group).lower()
            self.assertNotEqual(desc.find(search_term), -1)

    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        search_term = self._page.get_receiver_group_description(groups[0])
        self._page.send_search_to_receiver_group_desc_field(search_term)
        self._page.click_on_filter_receiver_groups_by_description()
        filtered_groups = self._page.get_list_of_receiver_groups()
        for group in filtered_groups:
            desc = self._page.get_receiver_group_description(group).lower()
            self.assertNotEqual(desc.find(search_term), -1)
        self._page.click_on_remove_receiver_groups_description_filter()
        non_filtered_groups = self._page.get_list_of_receiver_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        search_term = self._page.get_receiver_group_description(groups[0])
        self._page.send_search_to_receiver_group_desc_field(search_term)
        self._page.click_on_filter_receiver_groups_by_description()
        filtered_groups = self._page.get_list_of_receiver_groups()
        for group in filtered_groups:
            desc = self._page.get_receiver_group_description(group).lower()
            self.assertNotEqual(desc.find(search_term), -1)
        self._page.clear_remove_receiver_group_descriptions_filter()
        self._page.click_on_filter_receiver_groups_by_description()
        non_filtered_groups = self._page.get_list_of_receiver_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        name = self._page.get_receiver_group_name(groups[0])
        desc = self._page.get_receiver_group_description(groups[0])

        self._page.send_search_term_to_receiver_group_name_field(name)
        self._page.click_on_filter_receiver_groups_by_name()
        filtered_name = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_name) <= len(no_filter))

        self._page.send_search_to_receiver_group_desc_field(desc)
        self._page.click_on_filter_receiver_groups_by_description()
        filtered_desc = self._page.get_list_of_receivers()
        self._page.click_on_remove_filters()
        no_filter = self._page.get_list_of_receivers()
        self.assertTrue(len(filtered_desc) <= len(no_filter))

    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self._page.click_on_ascend_receiver_group_names()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            rx_names = [self._page.get_receiver_group_name(receiver)
                        for receiver in sorted_receivers]
            counter = 0
            for counter in range((len(rx_names) - 1)):
                prior = rx_names[counter].lower()
                latter = rx_names[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self._page.click_on_decend_receiver_group_names()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            rx_names = [self._page.get_receiver_group_name(receiver)
                        for receiver in sorted_receivers]
            counter = 0
            for counter in range((len(rx_names) - 1)):
                prior = rx_names[counter].lower()
                latter = rx_names[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self._page.click_on_ascend_receiver_group_descriptions()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            rx_descs = [self._page.get_receiver_group_description(receiver)
                       for receiver in sorted_receivers]
            for counter in range(0, (len(rx_descs) - 1)):
                prior = rx_descs[counter].lower()
                latter = rx_descs[counter + 1].lower()
                self.assertTrue(prior <= latter)

    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self._page.click_on_decend_receiver_group_descriptions()
        sorted_receivers = self._page.get_list_of_receivers()
        if len(sorted_receivers) > 1:
            rx_descs = [self._page.get_receiver_group_description(receiver)
                        for receiver in sorted_receivers]
            for counter in range(0, (len(rx_descs) - 1)):
                prior = rx_descs[counter].lower()
                latter = rx_descs[counter + 1].lower()
                self.assertTrue(prior >= latter)

    def test_can_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        receivers = self._page.get_list_of_receivers()
        for counter in range(0, len(receivers)):
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_group_config(receivers[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Receiver Groups > Configure Receiver Group")
            self._driver.back()

    def test_can_open_clone_receiver_group_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        receivers = self._page.get_list_of_receivers()
        for counter in range(0, len(receivers)):
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_group_clone(receivers[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Receiver Groups > " +
                             "Configure Cloned Receiver Group")
            self._driver.back()

    def test_can_open_and_cancel_delete_receiver_group_dialogue(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        receivers = self._page.get_list_of_receivers()
        for receiver in receivers:
            self._page.click_receiver_group_delete(receiver)
            text = self._page.get_delete_receiver_text_from_lightbox()
            self.assertTrue("Delete Receiver Group" in text)
            self._page.click_lightbox_cancel_button()
            self.assertFalse(self._page.check_lightbox_visibility())

    def test_can_delete_receiver_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self.reset_number_of_receiver_groups()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_group_delete(receivers[-1])
        text = self._page.get_delete_receiver_text_from_lightbox()
        self.assertTrue("Delete Receiver Group" in text)
        self._page.click_lightbox_delete_button()
        self.assertFalse(self._page.check_lightbox_visibility())
        new_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(receivers) > len(new_receivers))
        self.reset_number_of_receiver_groups()

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self.assertFalse(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.verify_batch_delete_checkbox())

    def test_can_cancel_batch_delete(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self._page.click_batch_delete_mode()
        groups = self._page.get_list_of_receiver_groups()
        for group in groups:
            visible = self._page.verify_batch_delete_for_receiver_group(group)
            self.assertTrue(visible)
        self._page.click_batch_delete_mode()
        for groups in groups:
            visible = self._page.verify_batch_delete_for_receiver_group(group)
            self.assertFalse(visible)
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_batch_delete_mode()
        self._page.click_batch_delete_receiver_group(groups[-1])
        self._page.click_batch_delete_receiver_group(groups[-2])
        self._page.click_batch_delete_receiver_groups()
        self._page.click_lightbox_cancel_button()
        new_groups = self._page.get_list_of_receiver_groups()
        self.assertTrue(len(groups) == len(new_groups))

    def test_can_batch_delete_receivers(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        self.reset_number_of_receiver_groups()
        receivers = self._page.get_list_of_receivers()
        self._page.click_batch_delete_mode()
        self._page.click_batch_delete_receiver_group(receivers[-1])
        self._page.click_batch_delete_receiver_group(receivers[-2])
        self._page.click_batch_delete_receiver_groups()
        self._page.click_lightbox_delete_button()
        new_receivers = self._page.get_list_of_receivers()
        self.assertTrue(len(receivers) >= len(new_receivers))
        self.reset_number_of_receiver_groups()

    def reset_number_of_receiver_groups(self):
        receivers = self._page.get_list_of_receivers()
        if len(receivers) < 5:
            counter = 5 - len(receivers)
            for counter in range(0, counter):
                receivers = self._page.get_list_of_receivers()
                name = self._page.get_receiver_group_name(receivers[-1])
                desc = self._page.get_receiver_group_description(receivers[-1])
                name = name.split(" ")
                desc = desc.split(" ")
                name[1] = str(int(name[1]) + 1)
                desc[1] = str(int(desc[1]) + 1)
                self._page.click_receiver_group_clone(receivers[-1])
                name = " ".join((name[0], name[1]))
                desc = " ".join((desc[0], desc[1]))
                self._page.set_receiver_group_name(name)
                self._page.set_receiver_group_description(desc)
                self._page.click_save()
