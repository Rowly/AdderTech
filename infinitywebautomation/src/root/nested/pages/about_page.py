'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.base_page import BasePage

class AboutPage(BasePage):
        
    def get_macs(self):
        macs = []
        for element in self.driver.find_elements_by_xpath("//p[contains(text(), 'Unit MAC ')]"):
            macs.append(element.text[-17:])
        return macs
    
    def find_build_numbers(self):
        builds = []
        for element in self.driver.find_elements_by_xpath("//p[contains(text(), 'Build number ')]"):
            builds.append(element.text.replace("Build number ", ""))
        return builds

    def get_main_system_version_number(self):
        return self.find_build_numbers()[0]

    def get_backup_system_version_number(self):
        return self.find_build_numbers()[1]
    
    def get_boot_system_version_number(self):
        return self.find_build_numbers()[2]
    
    def get_option_switch_1_text(self):
        return self.get_text_of_element_via_xpath("//p[contains(text(), 'Option Switch 1')]")

    def get_option_switch_2_text(self):
        return self.get_text_of_element_via_xpath("//p[contains(text(), 'Option Switch 2')]")

    def get_board_revision(self):
        return self.get_text_of_element_via_xpath("//p[contains(text(), 'Board Revision')]")
    
    def get_system_type(self):
        return self.get_text_of_element_via_xpath("//p[contains(text(), 'System Type is ')]").replace("System Type is ", "")
    