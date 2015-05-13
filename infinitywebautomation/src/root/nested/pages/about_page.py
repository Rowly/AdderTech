'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.base_page import BasePage


class AboutPage(BasePage):

    def get_macs(self):
        xpath = "//p[contains(text(), 'Unit MAC ')]"
        els = self.driver.find_elements_by_xpath(xpath)
        macs = [element.text[-17:]
                for element in els]
        return macs

    def find_build_numbers(self):
        xpath = "//p[contains(text(), 'Build number ')]"
        els = self.driver.find_elements_by_xpath(xpath)
        builds = [element.text.replace("Build number ", "")
                  for element in els]
        return builds

    def get_main_system_version_number(self):
        return self.find_build_numbers()[0]

    def get_backup_system_version_number(self):
        return self.find_build_numbers()[1]

    def get_boot_system_version_number(self):
        return self.find_build_numbers()[2]

    def get_option_switch_1_text(self):
        xpath = "//p[contains(text(), 'Option Switch 1')]"
        return self.get_text_of_element_via_xpath(xpath)

    def get_option_switch_2_text(self):
        xpath = "//p[contains(text(), 'Option Switch 2')]"
        return self.get_text_of_element_via_xpath(xpath)

    def get_board_revision(self):
        xpath = "//p[contains(text(), 'Board Revision')]"
        return self.get_text_of_element_via_xpath(xpath)

    def get_system_type(self):
        xpath = "//p[contains(text(), 'System Type is ')]"
        _type = self.get_text_of_element_via_xpath(xpath)
        return _type.replace("System Type is ", "")
