'''
Created on 6 Jan 2014

@author: Mark
'''
import time

from root.nested.pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class VideoConfigurationPage(BasePage):

    def get_selected_dvi_d1_background_refresh_option(self):
        time.sleep(1)
        path = "#backgroundrefreshrate"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_dvi_d1_background_refresh_options(self):
        time.sleep(1)
        path = "#backgroundrefreshrate"
        return self.get_options_from_select_element_by_css(path)

    def set_dvi_d1_background_refresh_option(self, text):
        path = "#backgroundrefreshrate"
        self.select_text_of_select_element_by_css(path, text)

    def get_selected_dvi_d1_colour_depth_option(self):
        time.sleep(1)
        found = False
        while(found == False):
            try:
                path = "#colourdepth"
                select = Select(self.driver.find_element_by_css_selector(path))
                text = select.first_selected_option.text
                found = True
                return text
            except NoSuchElementException:
                pass

    def get_dvi_d1_colour_depth_options(self):
        time.sleep(2)
        return self.get_options_from_select_element_by_css("#colourdepth")

    def set_dvi_d1_colour_depth_option(self, text):
        self.select_text_of_select_element_by_css("#colourdepth", text)

    def get_dvi_d1_use_default_ddc_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css("#def_ddc_enable")

    def set_dvi_d1_use_default_ddc_state(self, state):
        self.set_state_of_element_via_css("#def_ddc_enable", state)

    def get_dvi_d1_default_ddc_enabled_state(self):
        return self.get_enabled_state_of_element_via_css("#ddc_list")

    def get_selected_dvi_d1_default_ddc_option(self):
        time.sleep(2)
        return self.get_selected_value_of_select_element_by_css("#ddc_list")

    def get_dvi_d1_default_ddc_options(self):
        time.sleep(1)
        return self.get_options_from_select_element_by_css("#ddc_list")

    def set_dvi_d1_default_ddc_option(self, text):
        self.select_text_of_select_element_by_css("#ddc_list", text)

    def get_dvi_d1_hot_plug_detect_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css("#hpd_enable")

    def set_dvi_d1_hot_plug_detect_state(self, state):
        self.set_state_of_element_via_css("#hpd_enable", state)

    def get_dvi_d1_hot_plug_detect_period_enabled_state(self):
        time.sleep(1)
        return self.get_enabled_state_of_element_via_css("#hpd_period")

    def get_selected_dvi_d1_hot_plug_detect_period(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css("#hpd_period")

    def get_dvi_d1_hot_plug_detect_period_options(self):
        time.sleep(1)
        return self.get_options_from_select_element_by_css("#hpd_period")

    def set_dvi_d1_hot_plug_detect_period_option(self, text):
        self.select_text_of_select_element_by_css("#hpd_period", text)

    def get_selected_dvi_d2_background_refresh_option(self):
        time.sleep(1)
        path = "#backgroundrefreshrate1"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_dvi_d2_background_refresh_options(self):
        time.sleep(1)
        path = "#backgroundrefreshrate1"
        return self.get_options_from_select_element_by_css(path)

    def set_dvi_d2_background_refresh_option(self, text):
        path = "#backgroundrefreshrate1"
        self.select_text_of_select_element_by_css(path, text)

    def get_selected_dvi_d2_colour_depth_option(self):
        time.sleep(2)
        path = "#colourdepth1"
        return self.get_selected_value_of_select_element_by_css(path)

    def get_dvi_d2_colour_depth_options(self):
        time.sleep(1)
        return self.get_options_from_select_element_by_css("#colourdepth1")

    def set_dvi_d2_colour_depth_option(self, text):
        self.select_text_of_select_element_by_css("#colourdepth1", text)

    def get_dvi_d2_use_default_ddc_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css("#def_ddc1_enable")

    def set_dvi_d2_use_default_ddc_state(self, state):
        self.set_state_of_element_via_css("#def_ddc1_enable", state)

    def get_dvi_d2_default_ddc_enabled_state(self):
        time.sleep(1)
        return self.get_enabled_state_of_element_via_css("#ddc1_list")

    def get_selected_dvi_d2_default_ddc_option(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css("#ddc1_list")

    def get_dvi_d2_default_ddc_options(self):
        time.sleep(1)
        return self.get_options_from_select_element_by_css("#ddc1_list")

    def set_dvi_d2_default_ddc_option(self, text):
        self.select_text_of_select_element_by_css("#ddc1_list", text)

    def get_dvi_d2_hot_plug_detect_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css("#hpd1_enable")

    def set_dvi_d2_hot_plug_detect_state(self, state):
        self.set_state_of_element_via_css("#hpd1_enable", state)

    def get_dvi_d2_hot_plug_detect_period_enabled_state(self):
        time.sleep(1)
        return self.get_enabled_state_of_element_via_css("#hpd1_period")

    def get_selected_dvi_d2_hot_plug_detect_period(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css("#hpd1_period")

    def get_dvi_d2_hot_plug_detect_period_options(self):
        time.sleep(1)
        return self.get_options_from_select_element_by_css("#hpd1_period")

    def set_dvi_d2_hot_plug_detect_period_option(self, text):
        self.select_text_of_select_element_by_css("#hpd1_period", text)

    def update_config_form(self):
        text = self.click_update_button("#configForm_submit")
        time.sleep(1)
        return text
