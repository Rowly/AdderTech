'''
Created on 19 Nov 2013

@author: Mark
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimStatisticsPageFunctionsTest(BaseAimRegressionTest):

    def test_cannot_display_statistics_if_no_devices_selected(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self.assertEqual("No devices enabled", self._page.get_no_enabled_devices_text_from_lightbox())
    
    def test_can_display_statistics_from_device_selected_from_all_devices_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self._page.click_open_device_list_within_lightbox()
        self.assertEqual("Devices", self._page.get_text_of_page_header())
        device = self._page.get_list_of_devices()[0]
        device_name = self._page.get_device_name(device)
        self._page.click_device_statistics_icon(device)
        self._page.open_statistics_tab()
        self._page.click_lightbox_submit_button()
        self.assertTrue(device_name in self._page.get_device_name_from_statistics_graph())
        self._page.open_device_list_directly()
        device = self._page.get_list_of_devices()[0]
        self._page.click_device_statistics_icon(device)
    
    def test_can_display_statistics_from_receiver_showing_rxbandwidth_and_rxdata(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertEqual("Receivers", self._page.get_text_of_page_header())
        receiver = self._page.get_list_of_receivers()[0]
        receiver_name = self._page.get_receiver_name(receiver)
        self._page.click_receiver_statistics(receiver)
        self._page.open_statistics_tab()
        self._page.select_rx_bandwidth(True)
        self._page.select_rx_throughput(True)
        self._page.select_tx_throughput(False)
        self._page.select_tx_bandwidth(False)
        self._page.click_lightbox_submit_button()
        self.assertTrue(receiver_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Rx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_statistics(receiver)

    def test_can_display_statistics_from_receiver_showing_txbandwidth_and_txdata(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertEqual("Receivers", self._page.get_text_of_page_header())
        receiver = self._page.get_list_of_receivers()[0]
        receiver_name = self._page.get_receiver_name(receiver)
        self._page.click_receiver_statistics(receiver)
        self._page.open_statistics_tab()
        self._page.select_rx_throughput(False)
        self._page.select_rx_bandwidth(False)
        self._page.select_tx_bandwidth(True)
        self._page.select_tx_throughput(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(receiver_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Tx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_statistics(receiver)

    def test_can_display_statistics_from_receiver_showing_framecount(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertEqual("Receivers", self._page.get_text_of_page_header())
        receiver = self._page.get_list_of_receivers()[0]
        receiver_name = self._page.get_receiver_name(receiver)
        self._page.click_receiver_statistics(receiver)
        self._page.open_statistics_tab()
        self._page.select_rx_throughput(False)
        self._page.select_rx_bandwidth(False)
        self._page.select_tx_throughput(False)
        self._page.select_tx_bandwidth(False)
        self._page.select_framecount(True)
        self._page.select_head0_frame_rate(True)
        self._page.select_head1_frame_rate(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(receiver_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("frame count" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_statistics(receiver)

    def test_can_display_statistics_from_receiver_showing_framecount_and_rxbandwith(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertEqual("Receivers", self._page.get_text_of_page_header())
        receiver = self._page.get_list_of_receivers()[0]
        receiver_name = self._page.get_receiver_name(receiver)
        self._page.click_receiver_statistics(receiver)
        self._page.open_statistics_tab()
        self._page.select_rx_bandwidth(True)
        self._page.select_rx_throughput(True)
        self._page.select_tx_throughput(False)
        self._page.select_tx_bandwidth(False)
        self._page.select_framecount(True)
        self._page.select_head0_frame_rate(True)
        self._page.select_head1_frame_rate(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(receiver_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Rx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self.assertTrue("frame count" in self._page.get_graph_type_from_statistics_graph_right_axis())
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_statistics(receiver)

    def test_can_display_statistics_from_receiver_showing_framecount_and_txbandwith(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_receivers_tab()
        self.assertEqual("Receivers", self._page.get_text_of_page_header())
        receiver = self._page.get_list_of_receivers()[0]
        receiver_name = self._page.get_receiver_name(receiver)
        self._page.click_receiver_statistics(receiver)
        self._page.open_statistics_tab()
        self._page.select_rx_throughput(False)
        self._page.select_rx_bandwidth(False)
        self._page.select_tx_bandwidth(True)
        self._page.select_tx_throughput(True)
        self._page.select_framecount(True)
        self._page.select_head0_frame_rate(True)
        self._page.select_head1_frame_rate(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(receiver_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Tx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self.assertTrue("frame count" in self._page.get_graph_type_from_statistics_graph_right_axis())
        self._page.open_receivers_tab()
        receiver = self._page.get_list_of_receivers()[0]
        self._page.click_receiver_statistics(receiver)

    def test_can_display_statistics_from_transmitter_showing_rxbandwidth_and_rxdata(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertEqual("Transmitters", self._page.get_text_of_page_header())
        transmitter = self._page.get_list_of_transmitters()[0]
        transmitter_name = self._page.get_transmitter_name(transmitter)
        self._page.click_transmitter_statistics(transmitter)
        self._page.open_statistics_tab()
        self._page.select_rx_bandwidth(True)
        self._page.select_rx_throughput(True)
        self._page.select_tx_throughput(False)
        self._page.select_tx_bandwidth(False)
        self._page.click_lightbox_submit_button()
        self.assertTrue(transmitter_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Rx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        self._page.click_transmitter_statistics(transmitter)

    def test_can_display_statistics_from_transmitter_showing_txbandwidth_and_txdata(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertEqual("Transmitters", self._page.get_text_of_page_header())
        transmitter = self._page.get_list_of_transmitters()[0]
        transmitter_name = self._page.get_transmitter_name(transmitter)
        self._page.click_transmitter_statistics(transmitter)
        self._page.open_statistics_tab()
        self._page.select_rx_throughput(False)
        self._page.select_rx_bandwidth(False)
        self._page.select_tx_bandwidth(True)
        self._page.select_tx_throughput(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(transmitter_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Tx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        self._page.click_transmitter_statistics(transmitter)

    def test_can_display_statistics_from_transmitter_showing_framecount(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertEqual("Transmitters", self._page.get_text_of_page_header())
        transmitter = self._page.get_list_of_transmitters()[0]
        transmitter_name = self._page.get_transmitter_name(transmitter)
        self._page.click_transmitter_statistics(transmitter)
        self._page.open_statistics_tab()
        self._page.select_rx_throughput(False)
        self._page.select_rx_bandwidth(False)
        self._page.select_tx_throughput(False)
        self._page.select_tx_bandwidth(False)
        self._page.select_framecount(True)
        self._page.select_head0_frame_rate(True)
        self._page.select_head1_frame_rate(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(transmitter_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("frame count" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        self._page.click_transmitter_statistics(transmitter)
    
    def test_can_display_statistics_from_transmitter_showing_framecount_and_rxbandwith(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertEqual("Transmitters", self._page.get_text_of_page_header())
        transmitter = self._page.get_list_of_transmitters()[0]
        transmitter_name = self._page.get_transmitter_name(transmitter)
        self._page.click_transmitter_statistics(transmitter)
        self._page.open_statistics_tab()
        self._page.select_rx_bandwidth(True)
        self._page.select_rx_throughput(True)
        self._page.select_tx_throughput(False)
        self._page.select_tx_bandwidth(False)
        self._page.select_framecount(True)
        self._page.select_head0_frame_rate(True)
        self._page.select_head1_frame_rate(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(transmitter_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Rx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self.assertTrue("frame count" in self._page.get_graph_type_from_statistics_graph_right_axis())
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        self._page.click_transmitter_statistics(transmitter)

    def test_can_display_statistics_from_transmitter_showing_framecount_and_txbandwith(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_transmitters_tab()
        self.assertEqual("Transmitters", self._page.get_text_of_page_header())
        transmitter = self._page.get_list_of_transmitters()[0]
        transmitter_name = self._page.get_transmitter_name(transmitter)
        self._page.click_transmitter_statistics(transmitter)
        self._page.open_statistics_tab()
        self._page.select_rx_throughput(False)
        self._page.select_rx_bandwidth(False)
        self._page.select_tx_bandwidth(True)
        self._page.select_tx_throughput(True)
        self._page.select_framecount(True)
        self._page.select_head0_frame_rate(True)
        self._page.select_head1_frame_rate(True)
        self._page.click_lightbox_submit_button()
        self.assertTrue(transmitter_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue("Tx bandwidth (Mbit/s)" in self._page.get_graph_type_from_statistics_graph_left_axis())
        self.assertTrue("frame count" in self._page.get_graph_type_from_statistics_graph_right_axis())
        self._page.open_transmitters_tab()
        transmitter = self._page.get_list_of_transmitters()[0]
        self._page.click_transmitter_statistics(transmitter)
    
    def test_can_display_statistics_from_two_different_devices(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_statistics_tab()
        self._page.click_open_device_list_within_lightbox()
        self.assertEqual("Devices", self._page.get_text_of_page_header())
        device_one = self._page.get_list_of_devices()[0]
        device_one_name = self._page.get_device_name(device_one)
        self._page.click_device_statistics_icon(device_one)
        device_two = self._page.get_list_of_devices()[-1]
        device_two_name = self._page.get_device_name(device_two)
        self._page.click_device_statistics_icon(device_two)
        self._page.open_statistics_tab()
        self._page.click_lightbox_submit_button()
        self.assertTrue(device_one_name in self._page.get_device_name_from_statistics_graph())
        self.assertTrue(device_two_name in self._page.get_device_name_from_statistics_graph())
        self._page.open_device_list_directly()
        device_one = self._page.get_list_of_devices()[0]
        device_two = self._page.get_list_of_devices()[-1]
        self._page.click_device_statistics_icon(device_one)
        self._page.click_device_statistics_icon(device_two)