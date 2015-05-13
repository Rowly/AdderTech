'''
Created on 12 Nov 2013

@author: Mark.rowlands
'''
import unittest
from root.nested.services.parameters import parameter_singleton
from root.nested.services.selenium_start_service import SeleniumStartService
from selenium.webdriver.support.wait import WebDriverWait


class BaseInfinityRegressionTest(unittest.TestCase):

    def setUp(self):

        parameter_singleton["device"] = "RX2"
        parameter_singleton["version"] = "v3.3.30326"
        parameter_singleton["ip"] = "192.168.1.31"

        self._device = parameter_singleton["device"]
        self._version = parameter_singleton["version"]
        self._ip = parameter_singleton["ip"]
        self._base_url = "http://" + self._ip

        self._driver = SeleniumStartService().start_driver()
        self._wait = WebDriverWait(self._driver, 15)
        self._driver.get(self._base_url)

        #Global Test Variables
        self._invalid_ips = ["1.1.123123123.1",
                             "abc.ade.ade.adf",
                             "1.2",
                             "192.168.16.255",
                             " "]
        self._invalid_netmasks = ["255.255.123123123.1",
                                  "abc.ade.ade.adf",
                                  "1.2",
                                  " "]
        #255.255.255.255 appears to work when it shouldn't?

    def tearDown(self):
        try:
            self._driver.quit()
        except Exception:
            pass

    def check_device_is_dual(self):
        if (self._device == "RX"
            or self._device == "TX"
            or self._device == "RX2s"
            or self._device == "TX2s"):
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_rx2_rx2s_tx2_tx2b_tx2v(self):
        if self._device == "RX" or self._device == "TX":
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_receiver(self):
        if "RX" not in self._device:
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_rx2(self):
        if self._device != "RX2":
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_rx2_or_rx2s(self):
        if self._device != "RX2" and self._device != "RX2s":
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_transmitter(self):
        if "TX" not in self._device:
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_tx2_or_tx2b(self):
        if self._device != "TX2" and self._device != "TX2b":
            raise unittest.SkipTest("Incompatible device")

    def check_device_is_tx2v(self):
        if self._device != "TX2v":
            raise unittest.SkipTest("Incompatible device")

    def check_for_phantomjs(self):
        if self._driver.name == "phantomjs":
            raise unittest.SkipTest("Does not work with Phantomjs")
