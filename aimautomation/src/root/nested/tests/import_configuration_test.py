'''
Created on 19 Dec 2014

@author: Mark
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class ImportConfigurationTest(BaseAimRegressionTest):

    def test_can_import_transmitter_configurations(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        [self._page.click_transmitter_delete(tx)
         for tx in self._page.get_list_of_transmitters()
         if self._page.get_transmitter_name(tx) == "TX"]
        self._page.click_lightbox_delete_button()
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_import_configuration()
        self._page.enter_tx_import_details()
        self._page.click_submit()
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        self.assertEqual(self._page.get_transmitter_name(transmitter), "TX")
        self.reset_unit_if_possible(transmitter)
        self.reset_number_of_channels()

#     def test_can_import_recevier_configurations(self):
#         self._page.open_AIM_homepage_on_base_url()
#         self._page.login_as("admin", "password", False)
#         self._page.open_receivers_tab()
#         [self._page.click_receiver_delete(rx)
#          for rx in self._page.get_list_of_receivers()
#          if self._page.get_receiver_name(rx) == "RX"]
#         self._page.click_lightbox_delete_button()
#         self._page.open_dashboard_tab()
#         self._page.click_dashboard_backups_link()
#         self._page.click_import_configuration()
#         self._page.enter_rx_import_details()
#         self._page.click_submit()
#         self._page.open_receivers_tab()
#         receiver = self._page.get_list_of_receivers()[0]
#         self.assertEqual(self._page.get_receiver_name(receiver), "RX")
#         self.reset_unit_if_possible(receiver)

    def test_can_import_channel_configurations(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_import_configuration()
        self._page.enter_channel_import_details()
        self._page.click_submit()
        self._page.open_channels_tab()
        names = [self._page.get_channel_name(channel)
                 for channel in self._page.get_list_of_channels()]
        self.assertTrue("New Channel" in names)
        [self._page.click_channel_delete(channel)
         for channel in self._page.get_list_of_channels()
         if self._page.get_channel_name(channel) == "New Channel"]
        self._page.click_lightbox_delete_button()

    def test_can_import_users_configuration(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_users_tab()
        self._page.click_batch_delete_mode()
        for user in self._page.get_list_of_users():
            if (self._page.get_user_username(user)
                in ["admin", "anon", "api_anon"]):
                pass
            else:
                self._page.click_batch_delete_selector_for_user_element(user)
        self._page.click_batch_delete_users()
        self._page.click_lightbox_delete_button()
        self.assertEqual(len(self._page.get_list_of_users()), 3)
        self._page.open_dashboard_tab()
        self._page.click_dashboard_backups_link()
        self._page.click_import_configuration()
        self._page.enter_user_import_details()
        self._page.click_submit()
        self._page.open_users_tab()
        self.assertTrue(len(self._page.get_list_of_users()) > 3)
        names = [self._page.get_user_username(user)
                for user in self._page.get_list_of_users()]
        self.assertEqual(set(names),
                         set(["admin", "anon", "api_anon", "user 0",
                              "user 1", "user 2", "user 3", "user 4"]))

    """
    Utilities
    """
    def reset_number_of_channels(self):
        current_names = [self._page.get_channel_name(channel)
                         for channel in self._page.get_list_of_channels()]
        missing_names = list(set(self._channel_names) - set(current_names))
        if missing_names:
            for name in missing_names:
                self._page.click_add_channel_button()
                self._page.set_channel_name_via_config_page(name)
                split = name.split()
                end = split[-1]
                desc = "desc " + end
                loc = "loc " + end
                self._page.set_channel_description_via_config_page(desc)
                self._page.set_channel_location_via_config_page(loc)
                self._page.set_channel_video_source(end + " [1]")
                if (end + " [2]") in self._page.get_video2_source_options():
                    self._page.set_channel_video2_source(end + " [2]")
                self._page.set_channel_audio_source(end)
                self._page.set_channel_usb_source(end)
                self._page.add_user_to_channel_permission("admin")
                self._page.click_save()
        self._driver.refresh()

    def reset_unit_if_possible(self, device):
        try:
            cells = self._page.get_cell_elements(device)
            status = self._page.check_online_status_image_src(cells[0])
            _type = self._page.get_device_type_image_src(cells[0])
            if status == self._silk_dir + "tick_cross.png":
                if _type == self._silk_dir + "monitor_green.png":
                    self._page.click_receiver_configure(device)
                    self._page.click_save()
                    self._page.get_list_of_receivers()
                elif _type == self._silk_dir + "computer_purple.png":
                    self._page.click_transmitter_configure(device)
                    self._page.click_save()
        except Exception:
            pass
