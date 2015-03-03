'''
Created on 4 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimChannelGroupsViewPageFunctionsTest(BaseAimRegressionTest):

    search_term = "0"

    def test_can_open_add_channel_group_via_button(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_add_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups > Add Channel Group")

    def test_name_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_name_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_name()
        groups = self._page.get_list_of_channel_groups()
        for group in groups:
            grp_name = self._page.get_channel_group_name(group).lower()
            self.assertNotEqual(grp_name.find(self.search_term), -1)

    def test_name_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_name_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_name()
        filtered_groups = self._page.get_list_of_channel_groups()
        for group in filtered_groups:
            grp_name = self._page.get_channel_group_name(group).lower()
            self.assertNotEqual(grp_name.find(self.search_term), -1)
        self._page.click_on_remove_channel_groups_name_filter()
        non_filtered_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_name_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_name_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_name()
        filtered_groups = self._page.get_list_of_channel_groups()
        for group in filtered_groups:
            grp_name = self._page.get_channel_group_name(group).lower()
            self.assertNotEqual(grp_name.find(self.search_term), -1)
        self._page.clear_channel_names_filter()
        self._page.click_on_filter_channel_groups_by_name()
        non_filtered_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_description_filter_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_desc_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_description()
        groups = self._page.get_list_of_channel_groups()
        for group in groups:
            grp_desc = self._page.get_channel_group_desc(group).lower()
            self.assertNotEqual(grp_desc.find(self.search_term), -1)

    def test_description_filter_can_be_disabled(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_desc_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_description()
        filtered_groups = self._page.get_list_of_channel_groups()
        for group in filtered_groups:
            grp_desc = self._page.get_channel_group_desc(group).lower()
            self.assertNotEqual(grp_desc.find(self.search_term), -1)
        self._page.click_on_remove_channel_groups_description_filter()
        non_filtered_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_description_filter_can_be_cleared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_desc_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_description()
        filtered_groups = self._page.get_list_of_channel_groups()
        for group in filtered_groups:
            grp_desc = self._page.get_channel_group_desc(group).lower()
            self.assertNotEqual(grp_desc.find(self.search_term), -1)
        self._page.clear_channel_group_names_filter()
        self._page.click_on_filter_channel_groups_by_description()
        non_filtered_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(filtered_groups) <= len(non_filtered_groups))

    def test_remove_filters_button_operates_as_expected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.send_search_to_c_group_name_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_name()
        filtered_groups = self._page.get_list_of_channel_groups()
        self._page.click_on_remove_filters()
        no_filter_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(filtered_groups) <= len(no_filter_groups))
        self._page.send_search_to_c_group_desc_field(self.search_term)
        self._page.click_on_filter_channel_groups_by_description()
        filtered_groups = self._page.get_list_of_channel_groups()
        self._page.click_on_remove_filters()
        no_filter_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(filtered_groups) <= len(no_filter_groups))

    def test_can_sort_names_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_on_ascend_channel_group_names()
        sorted_groups = self._page.get_list_of_channel_groups()
        group_names = []
        if len(sorted_groups) > 1:
            for group in sorted_groups:
                group_names.append(self._page.get_channel_group_name(group))
            for counter in range(0, (len(group_names) - 1)):
                prior = group_names[counter]
                latter = group_names[counter + 1]
                self.assertTrue(prior < latter)

    def test_can_sort_names_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_on_decend_channel_group_names()
        sorted_groups = self._page.get_list_of_channel_groups()
        group_names = []
        if len(sorted_groups) > 1:
            for channel in sorted_groups:
                group_names.append(self._page.get_channel_group_name(channel))
            for counter in range(0, (len(group_names) - 1)):
                prior = group_names[counter]
                latter = group_names[counter + 1]
                self.assertTrue(prior > latter)

    def test_can_sort_descriptions_ascending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_on_ascend_channel_group_descriptions()
        sorted_groups = self._page.get_list_of_channel_groups()
        if len(sorted_groups) > 1:
            g_descs = [self._page.get_channel_group_desc(group)
                       for group in sorted_groups]
            for counter in range(0, (len(g_descs) - 1)):
                prior = g_descs[counter]
                latter = g_descs[counter + 1]
                self.assertTrue(prior < latter)

    def test_can_sort_descriptions_decending(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_on_decend_channel_group_descriptions()
        sorted_groups = self._page.get_list_of_channel_groups()
        if len(sorted_groups) > 1:
            g_descs = [self._page.get_channel_group_desc(group)
                       for group in sorted_groups]
            for counter in range(0, (len(g_descs) - 1)):
                prior = g_descs[counter]
                patter = g_descs[counter + 1]
                self.assertTrue(prior > patter)

    def test_can_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        groups = self._page.get_list_of_channel_groups()
        for counter in range(0, len(groups)):
            groups = self._page.get_list_of_channel_groups()
            self._page.click_configure_channel_group(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Channel Group")
            self._driver.back()

    def test_can_open_clone_channel_group_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        groups = self._page.get_list_of_channel_groups()
        for counter in range(0, len(groups)):
            groups = self._page.get_list_of_channel_groups()
            self._page.click_channel_group_clone(groups[counter])
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Channel Groups > Configure Cloned Channel Group")
            self._driver.back()

    def test_can_open_and_cancel_delete_channel_group_dialogue(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        groups = self._page.get_list_of_channel_groups()
        for group in groups:
            self._page.click_channel_group_delete(group)
            text = self._page.get_delete_chnl_grp_txt_from_lightbox()
            self.assertTrue("Delete channel group" in text)
            self._page.click_lightbox_cancel_button()
            self.assertFalse(self._page.check_lightbox_visibility())

    def test_can_delete_channel_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self.reset_number_of_channel_groups()
        groups = self._page.get_list_of_channel_groups()
        self._page.click_channel_group_delete(groups[-1])
        text = self._page.get_delete_chnl_grp_txt_from_lightbox()
        self.assertTrue("Delete channel group" in text)
        self._page.click_lightbox_delete_button()
        self.assertFalse(self._page.check_lightbox_visibility())
        new_groupss = self._page.get_list_of_channel_groups()
        self.assertTrue(len(groups) > len(new_groupss))
        self.reset_number_of_channel_groups()

    def test_can_toggle_batch_delete_mode(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self.assertFalse(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertTrue(self._page.verify_batch_delete_checkbox())
        self._page.click_batch_delete_mode()
        self.assertFalse(self._page.verify_batch_delete_checkbox())

    def test_can_cancel_batch_delete(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self._page.click_batch_delete_mode()
        groups = self._page.get_list_of_channel_groups()
        for group in groups:
            visible = self._page.verify_batch_delete_channel_group(group)
            self.assertTrue(visible)
        self._page.click_batch_delete_mode()
        for groups in groups:
            visible = self._page.verify_batch_delete_channel_group(group)
            self.assertFalse(visible)
        groups = self._page.get_list_of_channel_groups()
        self._page.click_batch_delete_mode()
        self._page.click_batch_delete_for_channel_group(groups[-1])
        self._page.click_batch_delete_for_channel_group(groups[-2])
        self._page.click_batch_delete_channel_groups()
        self._page.click_lightbox_cancel_button()
        new_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(groups) == len(new_groups))

    def test_can_batch_delete_channel_groups(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_channels_tab()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channels")
        self._page.click_view_channel_group_button()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Channel Groups")
        self.reset_number_of_channel_groups()
        groups = self._page.get_list_of_channel_groups()
        self._page.click_batch_delete_mode()
        self._page.click_batch_delete_for_channel_group(groups[-1])
        self._page.click_batch_delete_for_channel_group(groups[-2])
        self._page.click_batch_delete_channel_groups()
        self._page.click_lightbox_delete_button()
        new_groups = self._page.get_list_of_channel_groups()
        self.assertTrue(len(groups) >= len(new_groups))
        self.reset_number_of_channel_groups()

    def reset_number_of_channel_groups(self):
        groups = self._page.get_list_of_channel_groups()
        if len(groups) < 5:
            counter = 5 - len(groups)
            for counter in range(0, counter):
                groups = self._page.get_list_of_channel_groups()
                name = self._page.get_channel_group_name(groups[-1])
                desc = self._page.get_channel_group_desc(groups[-1])
                name = name.split(" ")
                desc = desc.split(" ")
                name[1] = str(int(name[1]) + 1)
                desc[1] = str(int(desc[1]) + 1)
                self._page.click_channel_group_clone(groups[-1])
                name = " ".join((name[0], name[1]))
                desc = " ".join((desc[0], desc[1]))
                self._page.set_channel_group_name_via_config_page(name)
                self._page.set_channel_group_desc_via_config_page(desc)
                self._page.click_save()
