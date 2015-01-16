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
from root.nested.tests.aim_login_page_defaults_test import AimLoginPageDefaultsTest
from root.nested.tests.aim_transmitter_config_page_functions_test import AimTransmitterConfigPageFunctions
from root.nested.tests.aim_add_user_group_page_functions_test import AimAddUserGroupPageFunctionsTest
from root.nested.tests.aim_login_page_functions_test import AimLoginPageFunctionsTest
from root.nested.tests.aim_transmitters_page_defaults_test import AimTransmittersPageDefaultTest
from root.nested.tests.aim_transmitters_page_functions_test import AimTransmittersPageFunctionsTest
from root.nested.tests.aim_transmitter_config_page_default_test import AimTransmitterConfigPageDefaultsTest
from root.nested.tests.aim_dashboard_page_defaults_test import AimDashboardDefaultsTest
from root.nested.tests.aim_channel_page_functions_test import AimChannelPageFunctionsTest
from root.nested.tests.aim_channel_config_page_functions_test import AimChannelConfigPageFunctionsTest
from root.nested.tests.aim_channel_clone_page_functions_test import AimChannelClonePageFunctionsTest
from root.nested.tests.aim_channel_groups_view_page_functions_test import AimChannelGroupsViewPageFunctionsTest
from root.nested.tests.aim_channel_group_config_functions_test import AimChannelGroupConfigFunctionsTest
from root.nested.tests.aim_channel_group_clone_page_functions_test import AimChannelGroupClonePageFunctionsTest
from root.nested.tests.aim_add_channel_group_page_functions_test import AimAddChannelGroupPageFunctionsTest
from root.nested.tests.aim_add_channel_page_functions_test import AimAddChannelPageFunctionsTest
from root.nested.tests.aim_receiver_view_group_functions_test import AimReceiverViewGroupFunctionsTest
from root.nested.tests.aim_receiver_config_page_functions_test import AimReceiverConfigPageFunctionsTest
from root.nested.tests.aim_receivers_page_functions_test import AimReceiversPageFunctionsTest
from root.nested.tests.aim_receiver_group_config_functions_test import AimReceiverGroupConfigFunctionsTest
from root.nested.tests.aim_receiver_group_clone_page_functions_test import AimReceiverGroupClonePageFunctionsTest
from root.nested.tests.aim_add_receiver_group_page_functions_test import AimAddReceiverGroupPageFunctionsTest
from root.nested.tests.aim_presets_page_functions_test import AimPresetsPageFunctionsTest
from root.nested.tests.aim_presets_config_page_functions_test import AimPresetsConfigPageFunctionsTest
from root.nested.tests.aim_presets_clone_page_functions_test import AimPresetsClonePageFunctionsTest
from root.nested.tests.aim_users_view_page_functions_test import AimUsersViewPageFunctionsTest
from root.nested.tests.aim_user_config_page_functions_test import AimUserConfigPageFunctionsTest
from root.nested.tests.aim_user_clone_page_functions_test import AimUserClonePageFunctionsTest
from root.nested.tests.aim_user_group_view_page_functions_test import AimUserGroupViewPageFunctionsTest
from root.nested.tests.aim_user_group_config_page_functions_test import AimUserGroupConfigPageFunctionsTest
from root.nested.tests.aim_user_group_clone_page_functions_test import AimUserGroupClonePageFunctionsTest
from root.nested.tests.aim_dashboard_home_page_functions_test import AimDashbordHomePageFunctionsTest
from root.nested.tests.aim_dashboard_settings_general_page_functions_test import AimDashboardSettingsGeneralPageFunctionsTest
from root.nested.tests.aim_dashboard_settings_transmitters_page_functions_test import AimDashboardSettingsTransmittersPageFunctionsTest
from root.nested.tests.aim_dashboard_settings_receivers_page_functions_test import AimDashboardSettingsReceiversPageFunctionsTest
from root.nested.tests.aim_dashboard_settings_time_page_functions_test import AimDashboardSettingsTimePageFunctionsTest
from root.nested.tests.aim_dashboard_settings_network_page_functions_test import AimDashboardSettingsNetworkPageFunctionsTest
from root.nested.tests.aim_dashboard_settings_mail_page_functions_test import AimDashboardSettingsMailPageFunctionsTest
from root.nested.tests.aim_dashboard_settings_active_directory_page_functions_test import AimDashboardSettingsActiveDirectoryPageFunctionsTest
from root.nested.tests.aim_dashboard_backups_page_functions_test import AimDashboardBackupsPageFunctionsTest
from root.nested.tests.aim_statistics_page_functions_test import AimStatisticsPageFunctionsTest
from root.nested.tests.aim_statistics_v32_page_functions_test import AimStatisticsV32PageFunctionsTest
from root.nested.tests.aim_servers_page_functions_test import AimServersPageFunctionsTest
from root.nested.services.HTMLTestRunner import HTMLTestRunner
from root.nested.services.parameters import parameter_singleton

class AimRegressionSuite():
    
    lengths_allowed = ["long", "short"]
        
    if __name__ == "__main__":
        
        parser = argparse.ArgumentParser(description="Web UI testing of AIM.")
        parser.add_argument("version", type=str, help="Version under test")
        parser.add_argument("suite", type=str, help="Suite length to run", choices=lengths_allowed)
        parser.add_argument("ip", type=str, help="IP of AIM unit under test")
        args = parser.parse_args()
        
        version = args.version
        suite_length = args.suite
        url = "http://" + args.ip
        parameter_singleton["version"] = version #for local tests edit value in base_test
        parameter_singleton["suite"] = suite_length #for local tests edit value in base_test
        parameter_singleton["url"] = url #for local tests edit value in base_test
        
        file_name = "%s_%s"%(version.replace(".", "-"), datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html"))
    
        output = open(file_name, "wb")
    
        loader = TestLoader()
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 2:
            suite = TestSuite((
                loader.loadTestsFromTestCase(AimLoginPageDefaultsTest),
                loader.loadTestsFromTestCase(AimLoginPageFunctionsTest),
                loader.loadTestsFromTestCase(AimTransmittersPageDefaultTest),
                loader.loadTestsFromTestCase(AimTransmittersPageFunctionsTest),
                loader.loadTestsFromTestCase(AimTransmitterConfigPageDefaultsTest),
                loader.loadTestsFromTestCase(AimTransmitterConfigPageFunctions),
                loader.loadTestsFromTestCase(AimChannelPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddChannelPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelGroupsViewPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelGroupConfigFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelGroupClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddChannelGroupPageFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiversPageFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiverConfigPageFunctionsTest),
                #loader.loadTestsFromTestCase(AimReceiverViewGroupFunctionsTest),
                #loader.loadTestsFromTestCase(AimReceiverGroupConfigFunctionsTest),
                #loader.loadTestsFromTestCase(AimReceiverGroupClonePageFunctionsTest),
                #loader.loadTestsFromTestCase(AimAddReceiverGroupPageFunctionsTest),
                loader.loadTestsFromTestCase(AimPresetsPageFunctionsTest),
                loader.loadTestsFromTestCase(AimPresetsConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimPresetsClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimUsersViewPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserGroupViewPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserGroupConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserGroupClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddUserGroupPageFunctionsTest),
                loader.loadTestsFromTestCase(AimServersPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardDefaultsTest),
                loader.loadTestsFromTestCase(AimDashbordHomePageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsGeneralPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsTransmittersPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsReceiversPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsNetworkPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsTimePageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsMailPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsActiveDirectoryPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardBackupsPageFunctionsTest),
                loader.loadTestsFromTestCase(AimStatisticsV32PageFunctionsTest)
                ))
        else:
            suite = TestSuite((
                loader.loadTestsFromTestCase(AimLoginPageDefaultsTest),
                loader.loadTestsFromTestCase(AimLoginPageFunctionsTest),
                loader.loadTestsFromTestCase(AimTransmittersPageDefaultTest),
                loader.loadTestsFromTestCase(AimTransmittersPageFunctionsTest),
                loader.loadTestsFromTestCase(AimTransmitterConfigPageDefaultsTest),
                loader.loadTestsFromTestCase(AimTransmitterConfigPageFunctions),
                loader.loadTestsFromTestCase(AimChannelPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddChannelPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelGroupsViewPageFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelGroupConfigFunctionsTest),
                loader.loadTestsFromTestCase(AimChannelGroupClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddChannelGroupPageFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiversPageFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiverConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiverViewGroupFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiverGroupConfigFunctionsTest),
                loader.loadTestsFromTestCase(AimReceiverGroupClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddReceiverGroupPageFunctionsTest),
                loader.loadTestsFromTestCase(AimPresetsPageFunctionsTest),
                loader.loadTestsFromTestCase(AimPresetsConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimPresetsClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimUsersViewPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserGroupViewPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserGroupConfigPageFunctionsTest),
                loader.loadTestsFromTestCase(AimUserGroupClonePageFunctionsTest),
                loader.loadTestsFromTestCase(AimAddUserGroupPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardDefaultsTest),
                loader.loadTestsFromTestCase(AimDashbordHomePageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsGeneralPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsTransmittersPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsReceiversPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsNetworkPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsTimePageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsMailPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardSettingsActiveDirectoryPageFunctionsTest),
                loader.loadTestsFromTestCase(AimDashboardBackupsPageFunctionsTest),
                loader.loadTestsFromTestCase(AimStatisticsPageFunctionsTest)
                ))
    
        runner = HTMLTestRunner(stream = output, verbosity = 1, title = "Aim UI Regression Suite "  + version)
        runner.run(suite)