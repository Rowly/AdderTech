'''
Created on 12 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimReceiverGroupConfigFunctionsTest(BaseAimRegressionTest):

    def test_change_receiver_group_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        name = self._page.get_receiver_group_name_from_config_page()
        self._page.set_receiver_group_name("%s edit" % name)
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        new_name = self._page.get_receiver_group_name(groups[0])
        self.assertEqual(new_name, "%s edit" % name)
        self._page.click_receiver_group_config(groups[0])
        self._page.set_receiver_group_name(name)
        self._page.click_save()

    def test_can_change_receiver_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        desc = self._page.get_receiver_group_desc_from_config_page()
        self._page.set_receiver_group_description("%s edit" % desc)
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        new_description = self._page.get_receiver_group_description(groups[0])
        self.assertEqual(new_description, "%s edit" % desc)
        self._page.click_receiver_group_config(groups[0])
        self._page.set_receiver_group_description(desc)
        self._page.click_save()

    def test_can_change_login_required(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        state = self._page.get_state_of_rx_group_login_required("inherit")
        self.assertTrue(state)
        self._page.select_receiver_group_login_required_no()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_of_rx_group_login_required("no")
        self.assertTrue(state)
        self._page.select_receiver_group_login_required_yes()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_of_rx_group_login_required("yes")
        self.assertTrue(state)
        self._page.select_receiver_group_login_required()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_of_rx_group_login_required("inherit")
        self.assertTrue(state)

    def test_can_change_enable_receiver_osd_alerts(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        state = self._page.get_state_receiver_group_osd_alerts("inherit")
        self.assertTrue(state)
        self._page.select_receiver_group_osd_alerts_no()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_receiver_group_osd_alerts("no")
        self.assertTrue(state)
        self._page.select_receiver_group_osd_alerts_yes()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_receiver_group_osd_alerts("yes")
        self.assertTrue(state)
        self._page.select_receiver_group_osd_alerts_global()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_receiver_group_osd_alerts("inherit")
        self.assertTrue(state)

    def test_can_change_enable_video_compatibility_check(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        state = self._page.get_state_rx_group_video_compatibility("inherit")
        self.assertTrue(state)
        self._page.select_receiver_group_video_compatibility_no()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_rx_group_video_compatibility("no")
        self.assertTrue(state)
        self._page.select_receiver_group_video_compatibility_yes()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_rx_group_video_compatibility("yes")
        self.assertTrue(state)
        self._page.select_receiver_group_video_compatibility()
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        state = self._page.get_state_rx_group_video_compatibility("inherit")
        self.assertTrue(state)

    def test_can_change_which_receivers_are_member_of_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        self.assertTrue(len(self._page.get_all_rxs_in_receiver_group()) == 0)
        recevier_name = self._page.get_all_rxs_not_in_receiver_group()[0]
        self._page.add_member_receiver_to_receiver_group(recevier_name)
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertTrue(recevier_name
                        in self._page.get_all_rxs_in_receiver_group())
        self._page.remove_all_member_receivers_from_receiver_group()
        self._page.click_save()

    def test_can_change_receiver_group_users(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        self._page.show_user_permissions()
        self.assertTrue(len(self._page.get_all_users_of_receiver_group()) == 0)
        name = self._page.get_all_not_permitted_users_of_receiver_group()[0]
        self._page.add_user_to_receiver_group(name)
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self._page.show_user_permissions()
        self.assertTrue(name in self._page.get_all_users_of_receiver_group())
        self._page.remove_all_users_from_receiver_group()
        self._page.click_save()

    def test_can_change_receiver_group_user_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        self._page.show_user_permissions()
        groups = self._page.get_selected_user_groups_of_rx_group()
        self.assertTrue(len(groups) == 0)
        name = self._page.get_all_not_permitted_user_groups_for_rx_group()[0]
        self._page.add_user_group_to_receiver_group(name)
        self._page.click_save()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self._page.show_user_permissions()
        groups = self._page.get_selected_user_groups_of_rx_group()
        self.assertTrue(name in groups)
        self._page.remove_all_user_groups_from_receiver_group()
        self._page.click_save()

    """
    USB Settings Tests
    """
    def test_can_change_hid_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        self._page.open_receiver_usb_settings()
        state = self._page.get_state_receiver_group_hid_only("inherit")
        self.assertTrue(state)
        self._page.select_receiver_group_HID_connection_no()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        state = self._page.get_state_receiver_group_hid_only("no")
        self.assertTrue(state)
        self._page.select_receiver_group_HID_connection_yes()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        state = self._page.get_state_receiver_group_hid_only("yes")
        self.assertTrue(state)
        self._page.select_receiver_group_HID_connection_global()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        state = self._page.get_state_receiver_group_hid_only("inherit")
        self.assertTrue(state)

    def test_can_change_disable_isochronous_endpoint_osd_alerts(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_disable_iso_endpoint_alert("inherit")
        self.assertTrue(st)
        self._page.select_receiver_grp_disable_iso_endpoint_alerts_no()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_disable_iso_endpoint_alert("no")
        self.assertTrue(st)
        self._page.select_receiver_grp_disable_iso_endpoint_alerts_yes()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_disable_iso_endpoint_alert("yes")
        self.assertTrue(st)
        self._page.select_receiver_grp_disable_iso_endpoint_alerts_global()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_disable_iso_endpoint_alert("inherit")
        self.assertTrue(st)

    def test_can_change_enable_isochronous_endpoint_attach(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        groups = self._page.get_list_of_receiver_groups()
        self._page.click_receiver_group_config(groups[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receiver Groups > Configure Receiver Group")
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_enable_iso_endpoint_attach("inherit")
        self.assertTrue(st)
        self._page.select_rx_grp_enable_iso_endpoint_attach_no()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_enable_iso_endpoint_attach("no")
        self.assertTrue(st)
        self._page.select_rx_grp_enable_iso_endpoint_attach_yes()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_enable_iso_endpoint_attach("yes")
        self.assertTrue(st)
        self._page.select_rx_grp_enable_iso_endpoint_attach_global()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        st = self._page.get_state_rx_grp_enable_iso_endpoint_attach("inherit")
        self.assertTrue(st)

    def test_can_change_port_reservation_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        setting = self._page.get_global_reserved_usb_port_setting()
        current_setting = setting
        self.assertEqual(current_setting, "None")
        labels = self._page.get_global_reserved_usb_port_options()
        labels.remove("None")
        for label  in labels:
            self._page.select_global_reserved_usb_port_by_text(label)
            self._page.click_save()
            self.assertEqual(self._page.get_global_reserved_usb_port_setting(),
                             label)
            converted_label = str(int(label) + 3)
            self._page.open_receivers_tab()
            receiver = self._page.get_list_of_receivers()[0]
            self._page.click_receiver_configure(receiver)
            self._page.open_receiver_usb_settings()
            for menu in self._page.get_list_of_port_reservation_dropdowns():
                selected = self._page.get_selected_rx_reserved_usb_port(menu)
                self.assertEqual(selected, "Inherited")
                self._page.select_port_reservation(menu, converted_label)
            self._page.click_save_usb_settings()
            self._page.open_receiver_usb_settings()
            for menu in self._page.get_list_of_port_reservation_dropdowns():
                selected = self._page.get_selected_rx_reserved_usb_port(menu)
                self.assertEqual(selected, converted_label)
                self._page.select_port_reservation(menu, "Inherited")
            self._page.click_save_usb_settings()
            self._page.open_dashboard_tab()
            self._page.click_dashboard_settings_link()
            self._page.click_transmitters_settings_button()
        self._page.select_global_reserved_usb_port_by_text("None")
        self._page.click_save()

    def test_can_change_port_reservation_device(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        menus = self._page.get_port_reservation_device_dropdowns()
        m = menus[0]
        labels = self._page.get_list_of_reserved_devices(m)
        labels.remove("Not Set")
        labels.remove("Inherited")
        for label in labels:
            for counter in range(0, len(menus)):
                menus = self._page.get_port_reservation_device_dropdowns()
                m = menus[counter]
                self._page.select_port_reservation_device(m, label)
                self._page.click_save_usb_settings()
                self._page.open_receiver_usb_settings()
                menus = self._page.get_port_reservation_device_dropdowns()
                m = menus[counter]
                slctd = self._page.get_selected_rx_reserved_usb_port_device(m)
                self.assertEqual(slctd, label)
        for menu in self._page.get_port_reservation_device_dropdowns():
            self._page.select_port_reservation_device(menu, "Inherited")
        for menu in self._page.get_list_of_port_reservation_dropdowns():
            self._page.select_port_reservation(menu, "Inherited")
        self._page.click_save_usb_settings()

    def test_can_change_displayed_port_reservation_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        for counter in range(0, len(devices)):
            devices = self._page.get_list_usb_devices()
            devices.pop()
            menus = self._page.get_port_reservation_device_dropdowns()
            original_labels = self._page.get_list_of_reserved_devices(menus[0])
            self._page.toggle_hide_usb_device(devices[counter])
            self._page.click_save_features()
            self._page.open_receiver_usb_settings()
            menus = self._page.get_port_reservation_device_dropdowns()
            new_labels = self._page.get_list_of_reserved_devices(menus[0])
            self.assertNotEqual(original_labels, new_labels)
            self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        for device in devices:
            self._page.toggle_hide_usb_device(device)
        self._page.click_save_features()

    def test_change_displayed_port_reservation_devices_via_global(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        menus = self._page.get_port_reservation_device_dropdowns()
        original_labels = self._page.get_list_of_reserved_devices(menus[0])
        self._page.set_status_hide_usb_device_global()
        self._page.set_status_hide_usb_device_global()
        #twice as needed to deselect all
        for device in devices:
            self.assertFalse(self._page.get_show_status_of_usb_device(device))
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertNotEqual(original_labels, new_labels)
        self._page.show_advanced_usb_features()
        self._page.set_status_hide_usb_device_global()
        self._page.click_save_features()

    def test_add_test_device_displayed_port_reservation_devices(self):
        test_name = "XX TEST name"
        test_desc = "XX TEST desc"
        test_kernel = "1234"
        test_user = "1234"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        menus = self._page.get_port_reservation_device_dropdowns()
        original_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertFalse(test_name in original_labels)
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device(test_name,
                                       test_desc,
                                       test_kernel,
                                       test_user)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertNotEqual(original_labels, new_labels)
        self.assertTrue(test_name in new_labels)
        self._page.show_advanced_usb_features()
        self._page.delete_test_usb_device()
        self._page.click_save_features()

    def test_incomplete_form_displayed_port_reservation_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device("", "", "", "")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("No changes made",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("", "XX TEST", "", "")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("No changes made",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("", "", "XX TEST", "")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("No changes made",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("", "", "", "XX TEST")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("No changes made",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "", "", "")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("Please ensure the form is completed correctly",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "", "")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("Please ensure the form is completed correctly",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "XX TEST", "")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("Please ensure the form is completed correctly",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST", "XX TEST", "", "XX TEST")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("Please ensure the form is completed correctly",
                         self._page.get_quirk_ajax_message_text())
        self._page.add_test_usb_device("XX TEST",
                                       "XX TEST",
                                       "XX TEST",
                                       "XX TEST")
        self._page.click_save_features_ignore_warnings()
        self.assertEqual("Please ensure the form is completed correctly",
                         self._page.get_quirk_ajax_message_text())

    def test_deleting_test_device_displayed_port_reservation_devices(self):
        test_name = "XX TEST test_name"
        test_desc = "XX TEST desc"
        test_kernel = "1234"
        test_user = "1234"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self._page.open_view_receiver_groups_page()
        group = self._page.get_list_of_receiver_groups()[0]
        self._page.click_receiver_group_config(group)
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device(test_name,
                                       test_desc,
                                       test_kernel,
                                       test_user)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_port_reservation_device_dropdowns()
        labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertTrue(test_name in labels)
        self._page.show_advanced_usb_features()
        self._page.delete_test_usb_device()
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        menus = self._page.get_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertFalse(test_name in new_labels)
