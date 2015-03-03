'''
Created on 10 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimReceiverConfigPageFunctionsTest(BaseAimRegressionTest):

    def test_can_enter_valid_name(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        original_name = self._page.get_receiver_name_from_config_page()
        new_name = original_name.upper()
        self._page.set_receiver_name(new_name)
        self.assertEqual(self._page.get_receiver_name_from_config_page(),
                         original_name.upper())
        new_name = original_name + "test"
        self._page.set_receiver_name(new_name)
        self.assertEqual(self._page.get_receiver_name_from_config_page(),
                         original_name + "test")
        new_name = original_name + "%%%%%"
        self._page.set_receiver_name(new_name)
        self.assertEqual(self._page.get_receiver_name_from_config_page(),
                         original_name + "%%%%%")
        new_name = original_name.lower()
        self._page.set_receiver_name(new_name)
        self.assertEqual(self._page.get_receiver_name_from_config_page(),
                         original_name.lower())
        self._page.set_receiver_name(original_name)

    def test_can_enter_valid_description(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        original_desc = self._page.get_receiver_desc_from_config_page()
        new_desc = original_desc.upper()
        self._page.set_receiver_desc(new_desc)
        self.assertEqual(self._page.get_receiver_desc_from_config_page(),
                         original_desc.upper())
        new_desc = original_desc + "test"
        self._page.set_receiver_desc(new_desc)
        self.assertEqual(self._page.get_receiver_desc_from_config_page(),
                         original_desc + "test")
        new_desc = original_desc + "%%%%%"
        self._page.set_receiver_desc(new_desc)
        self.assertEqual(self._page.get_receiver_desc_from_config_page(),
                         original_desc + "%%%%%")
        new_desc = original_desc.lower()
        self._page.set_receiver_desc(new_desc)
        self.assertEqual(self._page.get_receiver_desc_from_config_page(),
                         original_desc.lower())
        self._page.set_receiver_desc(original_desc)

    def test_can_enter_valid_location(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        original_loc = self._page.get_receiver_location_from_config_page()
        new_loc = original_loc.upper()
        self._page.set_receiver_loc(new_loc)
        self.assertEqual(self._page.get_receiver_location_from_config_page(),
                         original_loc.upper())
        new_loc = original_loc + "test"
        self._page.set_receiver_loc(new_loc)
        self.assertEqual(self._page.get_receiver_location_from_config_page(),
                         original_loc + "test")
        new_loc = original_loc + "%%%%%"
        self._page.set_receiver_loc(new_loc)
        self.assertEqual(self._page.get_receiver_location_from_config_page(),
                         original_loc + "%%%%%")
        new_loc = original_loc.lower()
        self._page.set_receiver_loc(new_loc)
        self.assertEqual(self._page.get_receiver_location_from_config_page(),
                         original_loc.lower())
        self._page.set_receiver_loc(original_loc)

    def test_can_change_login_required(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self.assertTrue(self._page.get_login_required_option_state("inherit"))
        self._page.select_login_required_no()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_login_required_option_state("no"))
        self._page.select_login_required_yes()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_login_required_option_state("yes"))
        self._page.select_login_required_global()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_login_required_option_state("inherit"))

    def test_can_change_OSD_alerts(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self.assertTrue(self._page.get_osd_alerts_option_state("inherit"))
        self._page.select_osd_alerts_no()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_osd_alerts_option_state("no"))
        self._page.select_osd_alerts_yes()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_osd_alerts_option_state("yes"))
        self._page.select_osd_alerts_global()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_osd_alerts_option_state("inherit"))

    def test_can_change_keyboard_country(self):
        default = "USE GLOBAL SETTING (currently gb - UK)"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self.assertEqual(self._page.get_selected_keyboard_country(),
                         default)
        all_options = self._page.get_all_keyboard_country_options()
        for option in all_options:
            self._page.set_keyboard_country_to_visible_text(option)
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            self.assertEqual(self._page.get_selected_keyboard_country(),
                             option)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self._page.set_keyboard_country_to_visible_text(default)
        self._page.click_save()
        if self._driver.name == "chrome":
            receivers = self._page.get_list_of_receivers()

    def test_can_change_audio_input_type(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        cells = self._page.get_cell_elements(receivers[0])
        device_type = self._page.get_device_type(cells[0])
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self.assertTrue(self._page.get_audio_input_option_state("global"))
        if device_type == "1":
            self._page.select_audio_input_line()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            self.assertTrue(self._page.get_audio_input_option_state("line"))
        self._page.select_audio_input_mic()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_audio_input_option_state("mic"))
        self._page.select_audio_input_mic_boost()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_audio_input_option_state("mic_boost"))
        self._page.select_audio_input_global()
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertTrue(self._page.get_audio_input_option_state("global"))

    def test_can_change_video_compatibility_check(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        cells = self._page.get_cell_elements(receivers[0])
        device_type = self._page.get_device_type(cells[0])
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        if not device_type == "1":
            v1_state = self._page.get_video_one_compatibility_state("inherit")
            self.assertTrue(v1_state)
            v2_state = self._page.get_video_two_compatibility_state("inherit")
            self.assertTrue(v2_state)

            self._page.select_video_one_compatibility_no()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_one_compatibility_state("no")
            self.assertTrue(state)

            self._page.select_video_one_compatibility_yes()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_one_compatibility_state("yes")
            self.assertTrue(state)

            self._page.select_video_two_compatibility_no()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_two_compatibility_state("no")
            self.assertTrue(state)

            self._page.select_video_two_compatibility_yes()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_two_compatibility_state("yes")
            self.assertTrue(state)

            self._page.select_video_one_compatibility_global()
            self._page.select_video_two_compatibility_global()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            v1_state = self._page.get_video_one_compatibility_state("inherit")
            self.assertTrue(v1_state)
            v2_state = self._page.get_video_two_compatibility_state("inherit")
            self.assertTrue(v2_state)

        elif device_type == "1":
            state = self._page.get_video_one_compatibility_state("inherit")
            self.assertTrue(state)

            self._page.select_video_one_compatibility_no()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_one_compatibility_state("no")
            self.assertTrue(state)

            self._page.select_video_one_compatibility_yes()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_one_compatibility_state("yes")
            self.assertTrue(state)

            self._page.select_video_one_compatibility_global()
            self._page.click_save()
            receivers = self._page.get_list_of_receivers()
            self._page.click_receiver_configure(receivers[0])
            state = self._page.get_video_one_compatibility_state("inherit")
            self.assertTrue(state)

    def test_can_change_receiver_group_membership(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        groups = self._page.get_all_current_rx_groups_for_rx()
        self.assertTrue(len(groups) == 0)
        self._page.add_receiver_to_receiver_group("group 0")
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        groups = self._page.get_all_current_rx_groups_for_rx()
        self.assertTrue("group 0" in groups)
        self._page.remove_all_receivers_from_receiver_group()
        self._page.click_save()

    def test_can_change_receiver_users(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self._page.show_user_permissions()
        self._page.remove_all_users_from_receiver()
        self._page.add_user_to_receiver("admin")
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self._page.show_user_permissions()
        self.assertTrue("admin" in self._page.get_all_current_users_for_rx())
        self._page.add_all_users_to_receiver()
        self._page.click_save()

    def test_can_change_receiver_user_group(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self._page.show_user_permissions()
        groups = self._page.get_all_current_user_groups_for_rx()
        self.assertTrue("group 0" in groups)
        self._page.remove_receiver_from_user_group("group 0")
        self._page.click_save()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self._page.show_user_permissions()
        groups = self._page.get_all_current_user_groups_for_rx()
        self.assertFalse("group 0" in groups)
        self._page.add_receiver_to_user_group("group 0")
        self._page.click_save()

    """
    USB Settings
    """
    def test_can_change_HID_connection_access(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        self.assertTrue(self._page.get_HID_connection_option_state("inherit"))
        self._page.select_HID_connection_no()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        self.assertTrue(self._page.get_HID_connection_option_state("no"))
        self._page.select_HID_connection_yes()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        self.assertTrue(self._page.get_HID_connection_option_state("yes"))
        self._page.select_HID_connection_global()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        self.assertTrue(self._page.get_HID_connection_option_state("inherit"))

    def test_can_change_disable_isochronous_endpoint_osd_alerts(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_disable_iso_endpoint_alert_state("inherit")
        self.assertTrue(state)
        self._page.select_disable_isochronous_endpoint_osd_alerts_no()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_disable_iso_endpoint_alert_state("no")
        self.assertTrue(state)
        self._page.select_disable_isochronous_endpoint_osd_alerts_yes()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_disable_iso_endpoint_alert_state("yes")
        self.assertTrue(state)
        self._page.select_disable_isochronous_endpoint_osd_alerts_global()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_disable_iso_endpoint_alert_state("inherit")
        self.assertTrue(state)

    def test_can_change_enable_isochronous_endpoint_attach(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_configure(receivers[0])
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver")
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_enable_iso_endpoint_attach_state("inherit")
        self.assertTrue(state)
        self._page.select_enable_isochronous_endpoint_attach_no()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_enable_iso_endpoint_attach_state("no")
        self.assertTrue(state)
        self._page.select_enable_isochronous_endpoint_attach_yes()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_enable_iso_endpoint_attach_state("yes")
        self.assertTrue(state)
        self._page.select_enable_isochronous_endpoint_attach_global()
        self._page.click_save_usb_settings()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        state = self._page.get_enable_iso_endpoint_attach_state("inherit")
        self.assertTrue(state)

    def test_can_change_port_reservation_values(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_transmitters_settings_button()
        labels = self._page.get_global_reserved_usb_port_options()
        labels.remove("None")
        for label in labels:
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
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_configure(receiver)
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
                self.assertEqual(self._page.get_text_of_page_header(),
                                 "Receivers > Configure Receiver USB settings")
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
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_configure(receiver)
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
            self.assertEqual(self._page.get_text_of_page_header(),
                             "Receivers > Configure Receiver USB settings")
            self._page.show_advanced_usb_features()
            menus = self._page.get_port_reservation_device_dropdowns()
            new_labels = self._page.get_list_of_reserved_devices(menus[0])
            self.assertNotEqual(original_labels, new_labels)
            self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        for device in devices:
            self._page.toggle_hide_usb_device(device)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        for menu in self._page.get_port_reservation_device_dropdowns():
            self._page.select_port_reservation_device(menu, "Inherited")
        self._page.click_save_usb_settings()

    def test_global_toggle_displayed_port_reservation_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_configure(receiver)
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        devices = self._page.get_list_usb_devices()
        devices.pop()
        menus = self._page.get_port_reservation_device_dropdowns()
        original_labels = self._page.get_list_of_reserved_devices(menus[0])
        self._page.set_status_hide_usb_device_global()
        self._page.set_status_hide_usb_device_global()
        for device in devices:
            status = self._page.get_show_status_of_usb_device(device)
            self.assertFalse(status)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        menus = self._page.get_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertNotEqual(original_labels, new_labels)
        self._page.show_advanced_usb_features()
        self._page.set_status_hide_usb_device_global()
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        for menu in self._page.get_port_reservation_device_dropdowns():
            self._page.select_port_reservation_device(menu, "Inherited")
        self._page.click_save_usb_settings()

    def test_add_device_port_reservation(self):
        test_name = "XX TEST name"
        test_desc = "XX TEST desc"
        test_kernel = "1234"
        test_user = "1234"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_configure(receiver)
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
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        menus = self._page.get_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertNotEqual(original_labels, new_labels)
        self.assertTrue(test_name in new_labels)
        self._page.show_advanced_usb_features()
        self._page.delete_test_usb_device()
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        for menu in self._page.get_port_reservation_device_dropdowns():
            self._page.select_port_reservation_device(menu, "Inherited")
        self._page.click_save_usb_settings()

    def test_incomplete_form_displayed_port_reservation_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_configure(receiver)
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

    def test_delete_test_device_port_reservation_device(self):
        test_name = "XX TEST name"
        test_desc = "XX TEST desc"
        test_kernel = "1234"
        test_user = "1234"
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_configure(receiver)
        self._page.open_receiver_usb_settings()
        self._page.show_advanced_usb_features()
        self._page.add_test_usb_device(test_name,
                                       test_desc,
                                       test_kernel,
                                       test_user)
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        menus = self._page.get_port_reservation_device_dropdowns()
        labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertTrue(test_name in labels)
        self._page.show_advanced_usb_features()
        self._page.delete_test_usb_device()
        self._page.click_save_features()
        self._page.open_receiver_usb_settings()
        self.assertEqual(self._page.get_text_of_page_header(),
                         "Receivers > Configure Receiver USB settings")
        menus = self._page.get_port_reservation_device_dropdowns()
        new_labels = self._page.get_list_of_reserved_devices(menus[0])
        self.assertFalse(test_name in new_labels)
        for menu in self._page.get_port_reservation_device_dropdowns():
            self._page.select_port_reservation_device(menu, "Inherited")
        self._page.click_save_usb_settings()
