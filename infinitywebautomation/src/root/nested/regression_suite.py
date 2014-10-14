'''
Created on 9 May 2013

@author: Mark.rowlands
'''
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

import datetime
import argparse
from unittest import TestLoader, TestSuite
from root.nested.tests.system_configuration_test import SystemConfigurationTest
from root.nested.tests.video_configuration_page_test import VideoConfigurationPageTest
from root.nested.tests.usb_settings_page_test import UsbSettingsPageTest
from root.nested.tests.security_page_test import SecurityPageTest
from root.nested.tests.aim_manager_page_test import AimManagerPageTest
from root.nested.tests.system_messages_page_test import SystemMessagesPageTest
from root.nested.tests.statistics_page_test import StatisticsPageTest
from root.nested.tests.firmware_upgrade_page_test import FirmwareUpgradePageTest
from root.nested.tests.reboot_page_test import RebootPageTest
from root.nested.tests.about_page_test import AboutPageTest
from root.nested.services.HTMLTestRunner import HTMLTestRunner
from root.nested.services.parameters import parameter_singleton

class InfinityRegressionSuite():
    RXS = ["RX", "RX2", "RX2s"]
    TXS = ["TX", "TX2", "TX2b", "TX2v", "TX2s"]

    if __name__ == "__main__":
    
        parser = argparse.ArgumentParser(description="Web UI testing of Infinity Devices.")
        parser.add_argument("unit_type", type=str, help="Unit type under test", choices=RXS+TXS)
        parser.add_argument("version", type=str, help="Version under test")
        parser.add_argument("ip", type=str, help="IP of device under test")
        args = parser.parse_args()
        
        unit = args.unit_type
        version = args.version
        ip = args.ip
        
        parameter_singleton["device"] = unit
        parameter_singleton["version"] = version
        parameter_singleton["ip"] = ip
        
        file_name = "%s_%s_%s" %(unit, 
                                 version.replace(".", "-"), 
                                 datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html"))
        output = open(file_name, "wb")
    
        loader = TestLoader()
        suite = TestSuite((
            loader.loadTestsFromTestCase(SystemConfigurationTest),
            loader.loadTestsFromTestCase(VideoConfigurationPageTest),
            loader.loadTestsFromTestCase(UsbSettingsPageTest),
            loader.loadTestsFromTestCase(SecurityPageTest),
            loader.loadTestsFromTestCase(AimManagerPageTest),
            loader.loadTestsFromTestCase(SystemMessagesPageTest),
            loader.loadTestsFromTestCase(StatisticsPageTest),
            loader.loadTestsFromTestCase(FirmwareUpgradePageTest),
            loader.loadTestsFromTestCase(RebootPageTest),
            loader.loadTestsFromTestCase(AboutPageTest)
            ))
        
        runner = HTMLTestRunner(stream = output, 
                                verbosity = 1, 
                                title = "Infinity Regression Suite. Device: %s Version: %s" %(unit, version))
        runner.run(suite)