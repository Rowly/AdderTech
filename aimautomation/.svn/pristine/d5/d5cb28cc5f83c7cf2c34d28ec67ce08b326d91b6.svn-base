'''
Created on 12 Jul 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import unittest
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest
from root.nested.services.parameters import parameter_singleton

class AimDashboardSettingsNetworkPageFunctionsTest(BaseAimRegressionTest):
    
    def test_cannot_change_syslog_ip_address_to_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.set_syslog_ip("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_syslog_ip_validation_icon_appearance())
        
    def test_can_syslog_ip_address_to_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_syslog_enabled(True)
        old_ip = self._page.get_syslog_ip()
        self._page.set_syslog_ip("169.254.1.2")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_syslog_ip_validation_icon_appearance())
        self._page.click_save()
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_syslog_ip_validation_icon_appearance())
        self._page.set_syslog_ip(old_ip)
        self._page.click_save()

    def test_cannot_change_multicast_ip_base_address_to_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.set_multicast_ip_base("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_multicast_ip_base_validation_icon_appearance())

    def test_can_change_multicast_ip_base_address_to_valid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        old_ip = self._page.get_multicast_ip_base()
        self._page.set_multicast_ip_base("237.1.1.2")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_multicast_ip_base_validation_icon_appearance())
        self._page.click_save()
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/accept.png" in self._page.get_multicast_ip_base_validation_icon_appearance())
        self._page.set_multicast_ip_base(old_ip)

    def test_cannot_change_aim_ip_address_to_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.set_aim_ip("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_aim_ip_validation_icon_appearance())

    def test_cannot_change_gateway_ip_address_to_invalid(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            raise unittest.SkipTest("Gateway removed in v3.2")
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.set_gateway_ip("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_gateway_ip_validation_icon_appearance())

    def test_cannot_change_netmask_address_to_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.set_netmask("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_netmask_validation_icon_appearance())

    def test_cannot_change_dns_server_ip_address_to_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.set_netmask("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_netmask_validation_icon_appearance())
    
    def test_changing_ethernet_port_2_to_dhcp_reveals_mac_and_ip(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_dhcp_ethernet_2()
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_label("dhcp"))
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_value("dhcp"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_label("dhcp"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_value("dhcp"))
        self._page.click_save()
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_label("dhcp"))
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_value("dhcp"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_label("dhcp"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_value("dhcp"))
        self._page.select_no_ethernet_2()
        self._page.click_save()
        
    def test_selecting_ethernet_port_2_to_static_reveals_all(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_static_ethernet_2()
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_label("static"))
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_value("static"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_label("static"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_value("static"))
        self.assertTrue(self._page.get_visibility_of_gateway_ip_address_label("static"))
        self.assertTrue(self._page.get_visibility_of_gateway_ip_address_value("static"))
        self.assertTrue(self._page.get_visibility_of_netmask_label("static"))
        self.assertTrue(self._page.get_visibility_of_netmask_value("static"))
        self.assertTrue(self._page.get_visibility_of_dns_server_ip_address_label("static"))
        self.assertTrue(self._page.get_visibility_of_dns_server_ip_address_value("static"))

    def test_selecting_ethernet_port_2_to_static_provide_no_details_gives_warning(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_static_ethernet_2()
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_label("static"))
        self.assertTrue(self._page.get_visibility_of_aim_mac_address_2_value("static"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_label("static"))
        self.assertTrue(self._page.get_visibility_of_aim_ip_address_2_value("static"))
        self.assertTrue(self._page.get_visibility_of_gateway_ip_address_label("static"))
        self.assertTrue(self._page.get_visibility_of_gateway_ip_address_value("static"))
        self.assertTrue(self._page.get_visibility_of_netmask_label("static"))
        self.assertTrue(self._page.get_visibility_of_netmask_value("static"))
        self.assertTrue(self._page.get_visibility_of_dns_server_ip_address_label("static"))
        self.assertTrue(self._page.get_visibility_of_dns_server_ip_address_value("static"))
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.get_visibility_of_settings_warning())

    def test_warning_given_for_aim_ip_address_2_if_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_static_ethernet_2()
        self._page.set_aim_ip_2("invalid")
        self._page.set_gateway_ip_2("10.10.20.1")
        self._page.set_netmask_2("255.255.255.0")
        self._page.set_dns_server_ip_2("10.10.20.1")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_aim_ip_2_validation_icon_appearance())
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.get_visibility_of_settings_warning())

    def test_warning_given_for_gateway_ip_address_2_if_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_static_ethernet_2()
        self._page.set_aim_ip_2(self.create_new_ip_from_baseurl())
        self._page.set_gateway_ip_2("invalid")
        self._page.set_netmask_2("255.255.255.0")
        self._page.set_dns_server_ip_2("10.10.20.1")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_gateway_ip_2_validation_icon_appearance())
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.get_visibility_of_settings_warning())

    def test_warning_given_for_netmask_2_if_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_static_ethernet_2()
        self._page.set_aim_ip_2(self.create_new_ip_from_baseurl())
        self._page.set_gateway_ip_2("10.10.20.1")
        self._page.set_netmask_2("invalid")
        self._page.set_dns_server_ip_2("10.10.20.1")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_netmask_2_validation_icon_appearance())
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.get_visibility_of_settings_warning())

    def test_warning_given_for_dns_server_ip_address_2_if_invalid(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self._page.select_static_ethernet_2()
        self._page.set_aim_ip_2(self.create_new_ip_from_baseurl())
        self._page.set_gateway_ip_2("10.10.20.1")
        self._page.set_netmask_2("255.255.255.0")
        self._page.set_dns_server_ip_2("invalid")
        self.assertTrue(self._baseurl + "/admin/images/silk_icons/exclamation.png" in self._page.get_dns_server_ip_2_validation_icon_appearance())
        self._page.click_save_ignore_warnings()
        self.assertTrue(self._page.get_visibility_of_settings_warning())
    
    def test_snmp_options_available_once_snmp_enabled(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) <= 3 and int(split_version[1]) < 2:
            raise unittest.SkipTest("SNMP added in v3.2")
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.click_dashboard_settings_link()
        self._page.click_network_settings_button()
        self.assertFalse(self._page.get_display_state_snmp_username())
        self._page.set_snmp_enabled("yes")
        self.assertTrue(self._page.get_display_state_snmp_username())
        self._page.set_snmp_enabled("no")
        self._page.click_save_ignore_warnings()
        
    def create_new_ip_from_baseurl(self):
        url = self._baseurl.replace("http://", "")
        url = url.split(".")
        url[2] = "20"
        url[3] = str(int(url[3]) + 1)
        return ".".join((url[0], url[1], url[2], url[3]))