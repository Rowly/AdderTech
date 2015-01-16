'''
Created on 7 May 2014

@author: Mark
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimStatisticsV32PageFunctionsTest(BaseAimRegressionTest):
    
    def test_can_set_device_filter_to_rx_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self._page.click_show_receivers()
        devices = self._page.get_list_of_devices()
        for device in devices:
            self.assertTrue("monitor_green.png" in self._page.get_device_type_img(device))

    def test_can_set_device_filter_to_tx_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self._page.click_show_transmitters()
        devices = self._page.get_list_of_devices()
        for device in devices:
            self.assertTrue("computer_purple.png" in self._page.get_device_type_img(device))
    
    def test_can_activate_statistics_for_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self._page.click_disable_all_device_statistics()
        devices = self._page.get_list_of_devices()
        counter = 0
        for counter in range(counter, len(devices)):
            devices = self._page.get_list_of_devices()
            self._page.click_activate_statistics(devices[counter])
            self._page.click_device_name(devices[counter])
            self.assertTrue(self._page.get_graph_title(), "Statistics")
            self._page.driver.back()
        self._page.click_disable_all_device_statistics()
    
    def test_can_disable_statistics_for_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self._page.click_disable_all_device_statistics()
        devices = self._page.get_list_of_devices()
        for device in devices:
            self._page.click_activate_statistics(device)
            self.assertEqual(1, self._page.get_number_device_name_links(device))
        for device in devices:
            self._page.click_activate_statistics(device)
            self.assertEqual(0, self._page.get_number_device_name_links(device))
        for device in devices:
            self._page.click_activate_statistics(device)
        self._page.click_disable_all_device_statistics()
        for device in devices:
            self.assertEqual(0, self._page.get_number_device_name_links(device))
        
    def test_filters_work(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        devices = self._page.get_list_of_devices()
        search_term = self._page.get_device_name(devices[-1])
        self._page.send_search_term_to_name(search_term)
        self._page.click_filter_by_name()
        devices = self._page.get_list_of_devices()
        self.assertTrue(search_term in self._page.get_device_name(devices[-1]))
        self._page.click_remove_filters()
        self._page.send_search_term_to_description(search_term)
        self._page.click_filter_by_description()
        devices = self._page.get_list_of_devices()
        self.assertTrue(search_term in self._page.get_device_description(devices[-1]))
        self._page.click_remove_filters()
        self._page.send_search_term_to_location(search_term)
        self._page.click_filter_by_location()
        devices = self._page.get_list_of_devices()
        self.assertTrue(search_term in self._page.get_device_location(devices[-1]))
        self._page.click_remove_filters()