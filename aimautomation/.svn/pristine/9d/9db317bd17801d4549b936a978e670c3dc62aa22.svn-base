'''
Created on 8 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimDashbordHomePageFunctionsTest(BaseAimRegressionTest):
    
    def test_all_sublinks_operate_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Settings")
        self._page.click_dashboard_backups_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Backup")
        self._page.click_dashboard_updates_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Upgrade AIM Software")
        self._page.click_dashboard_active_connections_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Connection Log")
        self._page.click_dashboard_connection_log_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Connection Log")
        self._page.click_dashboard_event_log_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Event Log")
        self._page.click_dashboard_home_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Dashboard")
     
    def test_view_all_active_connections_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_active_connects_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Connection Log")
     
    def test_view_all_events_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_events_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Event Log")
     
    def test_view_all_channels_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_channels_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Channels")
 
    def test_view_all_channel_changes_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_channel_changes_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Connection Log")
 
    def test_view_all_user_logins_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_OSD_logins_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Event Log")
 
    def test_view_all_users_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_users_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Users")
 
    def test_view_all_receivers_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_receivers_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Receivers")
 
    def test_view_all_transmitters_link_operates_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_view_all_transmitters_link()
        self.assertEqual(self._page.get_text_of_page_header(), "Transmitters")
     
    def test_all_latest_active_connect_user_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_active_connection_user_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_active_connection_user_names_from_dashboard_page()
                links = self._page.get_active_connection_user_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure User")
                self.assertEqual(self._page.get_user_username_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_latest_active_connect_receiver_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_active_connection_receiver_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_active_connection_receiver_names_from_dashboard_page()
                links = self._page.get_active_connection_receiver_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Receivers > Configure Receiver")
                self.assertEqual(self._page.get_receiver_name_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_latest_active_connect_preset_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_active_connection_preset_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_active_connection_preset_names_from_dashboard_page()
                links = self._page.get_active_connection_preset_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Presets > Configure Preset")
                self.assertEqual(self._page.get_preset_name_from_config_page(), names[counter])
                self._driver.back()
     
    def test_all_event_log_user_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_event_log_user_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_event_log_user_names_from_dashboard_page()
                links = self._page.get_event_log_user_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure User")
                config_name = self._page.get_user_username_from_config_page()
                self.assertEqual(config_name, names[counter])
                self._driver.back()
 
    def test_all_event_log_transmitter_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_event_log_transmitter_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_event_log_transmitter_names_from_dashboard_page()
                links = self._page.get_event_log_transmitter_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                self.assertEqual(self._page.get_transmitter_name_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_event_log_receiver_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_event_log_receiver_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_event_log_receiver_names_from_dashboard_page()
                links = self._page.get_event_log_receiver_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Receivers > Configure Receiver")
                self.assertEqual(self._page.get_receiver_name_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_event_log_channel_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_event_log_channel_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_event_log_channel_names_from_dashboard_page()
                links = self._page.get_event_log_channel_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter])
                self._driver.back()
     
    def test_all_latest_active_connect_channel_name_open_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_active_connection_channel_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_active_connection_channel_names_from_dashboard_page()
                links = self._page.get_active_connection_channel_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter])
                self._driver.back()
     
    def test_all_latest_channel_names_open_corresponding_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_channel_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_channel_names_from_dashboard_page()
                links = self._page.get_channel_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter])
                self._driver.back()
                 
    def test_all_latest_channel_names_corresponding_pencil_icon_opens_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_channel_configure_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_channel_names_from_dashboard_page()
                links = self._page.get_channel_configure_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_latest_channel_names_corresponding_clone_icon_opens_correct_clone_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_channel_clone_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_channel_names_from_dashboard_page()
                links = self._page.get_channel_clone_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Cloned Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter] + " (Copy)")
                self._driver.back()
 
    def test_all_user_logins_open_corresponding_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_user_login_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_user_login_names_from_dashboard_page()
                links = self._page.get_user_login_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter])
                self._driver.back()
                 
    def test_all_user_logins_corresponding_pencil_icon_opens_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_user_login_configure_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_user_login_names_from_dashboard_page()
                links = self._page.get_user_login_configure_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure User")
                self.assertEqual(self._page.get_user_username_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_user_registration_links_open_corresponding_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_user_registration_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_user_registration_names_from_dashboard_page()
                links = self._page.get_user_registration_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure User")
                self.assertEqual(self._page.get_user_username_from_config_page(), names[counter])
                self._driver.back()
                 
    def test_all_user_registration_links_corresponding_pencil_icon_opens_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_user_registration_configure_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_user_registration_names_from_dashboard_page()
                links = self._page.get_user_registration_configure_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure User")
                self.assertEqual(self._page.get_user_username_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_user_registration_links_corresponding_icon_opens_correct_clone_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_user_registration_clone_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_user_registration_names_from_dashboard_page()
                links = self._page.get_user_registration_clone_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure Cloned User")
                self.assertEqual(self._page.get_user_username_from_config_page(), names[counter]+"_copy")
                self._driver.back()
 
    def test_all_receiver_links_open_corresponding_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_receiver_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_receiver_names_from_dashboard_page()
                links = self._page.get_receiver_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Receivers > Configure Receiver")
                self.assertEqual(self._page.get_receiver_name_from_config_page(), names[counter])
                self._driver.back()
                 
    def test_all_receiver_links_corresponding_pencil_icon_opens_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_receiver_configure_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_receiver_names_from_dashboard_page()
                links = self._page.get_receiver_configure_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Receivers > Configure Receiver")
                self.assertEqual(self._page.get_receiver_name_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_receiver_links_corresponding_connect_icon_opens_connect_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_receiver_connect_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_receiver_names_from_dashboard_page()
                links = self._page.get_receiver_connect_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Receivers > Change channel on " + names[counter])
                self._driver.back()
     
    def test_receivers_shown_in_widget_can_connect_to_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        if self._page.get_visibility_of_dashboard_disconnect_all():
            self._page.click_dashboard_disconnect_all()
        receivers = self._page.get_receivers_from_dashboard_widget()
        counter = 0
        for counter in range(counter, len(receivers)):
            receivers = self._page.get_receivers_from_dashboard_widget()
            self._page.click_receiver_connect_via_dashboard_widget(receivers[counter])
            channels = self._page.get_list_of_channels()
            self._page.click_on_connect_receiver_to_channel_view_only(channels[0])
            self._page.open_dashboard_tab()
        receivers = self._page.get_receivers_from_dashboard_widget()
        for receiver in receivers:
            self.assertTrue(self._page.get_visibility_of_receiver_disconnect_button(receiver))
     
    def test_receivers_shown_in_widget_can_disconnect_from_channel(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        receivers = self._page.get_receivers_from_dashboard_widget()
        counter = 0
        for counter in range(counter, len(receivers)):
            receivers = self._page.get_receivers_from_dashboard_widget()
            self._page.click_receiver_connect_via_dashboard_widget(receivers[counter])
            channels = self._page.get_list_of_channels()
            self._page.click_on_connect_receiver_to_channel_view_only(channels[0])
            self._page.open_dashboard_tab()
        receivers = self._page.get_receivers_from_dashboard_widget()
        counter = 0
        for counter in range(counter, len(receivers)):
            self._page.click_receiver_disconnect_via_dashboard_widget(receivers[counter])
            self._page.open_dashboard_tab()
            receivers = self._page.get_receivers_from_dashboard_widget()
            self.assertFalse(self._page.get_visibility_of_receiver_disconnect_button(receivers[counter]))
             
    def test_all_transmitter_links_open_corresponding_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_transmitter_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_transmitter_names_from_dashboard_page()
                links = self._page.get_transmitter_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                self.assertEqual(self._page.get_transmitter_name_from_config_page(), names[counter])
                self._driver.back()
                 
    def test_all_transmitter_links_corresponding_pencil_icon_opens_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_transmitter_confifgure_links_from_icon_on_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_transmitter_names_from_dashboard_page()
                links = self._page.get_transmitter_confifgure_links_from_icon_on_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Transmitters > Configure Transmitter")
                self.assertEqual(self._page.get_transmitter_name_from_config_page(), names[counter])
                self._driver.back()
     
    def test_all_channel_change_user_links_open_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_channel_change_user_name_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_channel_change_user_name_from_dashboard_page()
                links = self._page.get_channel_change_user_name_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Users > Configure User")
                self.assertEqual(self._page.get_user_username_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_channel_change_receiver_links_open_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_channel_change_receiver_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_channel_change_receiver_name_from_dashboard_page()
                links = self._page.get_channel_change_receiver_links_from_dashboard_page()  
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Receivers > Configure Receiver")
                self.assertEqual(self._page.get_receiver_name_from_config_page(), names[counter])
                self._driver.back()
 
    def test_all_channel_change_channel_links_open_correct_config_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        links = self._page.get_channel_change_channel_links_from_dashboard_page()
        if links is not None:
            counter = 0
            for counter in range(counter, len(links)):
                names = self._page.get_channel_change_channel_name_from_dashboard_page()
                links = self._page.get_channel_change_channel_links_from_dashboard_page()
                self._driver.get(links[counter])
                self.assertEqual(self._page.get_text_of_page_header(), "Channels > Configure Channel")
                self.assertEqual(self._page.get_channel_name_from_config_page(), names[counter])
                self._driver.back()
     
    def test_is_a_confirmation_given_when_restart_attempted(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_restart()
        self.assertTrue("Restart AIM Server?" in self._page.get_restart_aim_unit_text_from_lightbox())
     
    def test_can_cancel_restart(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_restart()
        self._page.click_lightbox_cancel_button()
        self.assertFalse(self._page.check_lightbox_visibility())
     
    def test_is_a_confirmation_given_when_shutdown_attempted(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_shutdown()
        title = self._page.get_shutdown_aim_unit_text_from_lightbox()
        self.assertTrue("Shutdown AIM Server?" in title)
     
    def test_can_cancel_shutdown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_shutdown()
        self._page.click_lightbox_cancel_button()
        self.assertFalse(self._page.check_lightbox_visibility())
     
    def test_disconnect_all_button_functions_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        if not self._page.get_visibility_of_dashboard_disconnect_all():
            self.make_connection()
        self._page.click_dashboard_disconnect_all()
        self._page.click_lightbox_disconnect_button()
        self._page.open_dashboard_tab()
        self.assertEqual(self._page.get_text_of_active_connections_widget(), "No Active Connections")
 
    def make_connection(self):
        self._page.open_receivers_tab()
        receivers = self._page.get_list_of_receivers()
        self._page.click_receiver_connect_to_channel(receivers[0])
        channels = self._page.get_list_of_channels()
        self._page.click_on_connect_receiver_to_channel_view_only(channels[0])
        self._page.open_dashboard_tab()