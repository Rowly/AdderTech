'''
Created on 12 Dec 2013

@author: Mark
'''
from root.nested.pages.about_page import AboutPage
from root.nested.pages.aim_manager_page import AimManagerPage
from root.nested.pages.base_page import BasePage
from root.nested.pages.firmware_upgrade_page import FirmwareUpgradePage
from root.nested.pages.reboot_page import RebootPage
from root.nested.pages.security_page import SecurityPage
from root.nested.pages.statistics_page import StatisticsPage
from root.nested.pages.system_configuration_page import SystemConfigurationPage
from root.nested.pages.system_messages_page import SystemMessagesPage
from root.nested.pages.usb_settings_page import UsbSettingsPage
from root.nested.pages.video_configuration_page import VideoConfigurationPage


class HomePage(BasePage):

    def open_system_configuration_page(self):
        self.click_menu_link("System Configuration")
        return SystemConfigurationPage(self.driver, self.wait)

    def open_video_configuration_page(self):
        self.click_menu_link("Video Configuration")
        return VideoConfigurationPage(self.driver, self.wait)

    def open_usb_settings_page(self):
        self.click_menu_link("USB Settings")
        return UsbSettingsPage(self.driver, self.wait)

    def open_security_page(self):
        self.click_menu_link("Security")
        return SecurityPage(self.driver, self.wait)

    def open_aim_manager_page(self):
        self.click_menu_link("AIM Manager")
        return AimManagerPage(self.driver, self.wait)

    def open_system_messages_page(self):
        self.click_menu_link("System Messages")
        return SystemMessagesPage(self.driver, self.wait)

    def open_statistics_page(self):
        self.click_menu_link("Statistics")
        return StatisticsPage(self.driver, self.wait)

    def open_firmware_upgrade_page(self):
        self.click_menu_link("Firmware Upgrade")
        return FirmwareUpgradePage(self.driver, self.wait)

    def open_reboot_page(self):
        self.click_menu_link("Reboot")
        return RebootPage(self.driver, self.wait)

    def open_about_page(self):
        self.click_menu_link("About")
        return AboutPage(self.driver, self.wait)
