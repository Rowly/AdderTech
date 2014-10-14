'''
Created on 6 Jan 2014

@author: Mark
'''
from root.nested.pages.base_page import BasePage
import time
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

class VideoConfigurationPage(BasePage):

    def get_selected_dvi_d1_background_refresh_option(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css_selector("#backgroundrefreshrate")
    
    def get_dvi_d1_background_refresh_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#backgroundrefreshrate")
    
    def set_dvi_d1_background_refresh_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#backgroundrefreshrate", text)
    
    def get_selected_dvi_d1_colour_depth_option(self):
        time.sleep(1)
        found = False
        while(found == False):
            try:
                select = Select(self.driver.find_element_by_css_selector("#colourdepth"))
                text =  select.first_selected_option.text
                found = True
                return text
            except: NoSuchElementException 
    
    def get_dvi_d1_colour_depth_options(self):
        time.sleep(2)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#colourdepth")
    
    def set_dvi_d1_colour_depth_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#colourdepth", text)
    
    def get_dvi_d1_use_default_ddc_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css_selector("#def_ddc_enable")
    
    def set_dvi_d1_use_default_ddc_state(self, state):
        self.set_state_of_element_via_css_selector("#def_ddc_enable", state)
    
    def get_dvi_d1_default_ddc_enabled_state(self):
        return self.get_enabled_state_of_element_via_css_selector("#ddc_list")
    
    def get_selected_dvi_d1_default_ddc_option(self):
        time.sleep(2)
        return self.get_selected_value_of_select_element_by_css_selector("#ddc_list")
    
    def get_dvi_d1_default_ddc_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#ddc_list")
    
    def set_dvi_d1_default_ddc_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#ddc_list", text)
    
    def get_dvi_d1_hot_plug_detect_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css_selector("#hpd_enable")
    
    def set_dvi_d1_hot_plug_detect_state(self, state):
        self.set_state_of_element_via_css_selector("#hpd_enable", state)
    
    def get_dvi_d1_hot_plug_detect_period_enabled_state(self):
        time.sleep(1)
        return self.get_enabled_state_of_element_via_css_selector("#hpd_period")
    
    def get_selected_dvi_d1_hot_plug_detect_period(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css_selector("#hpd_period")
    
    def get_dvi_d1_hot_plug_detect_period_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#hpd_period")
    
    def set_dvi_d1_hot_plug_detect_period_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#hpd_period", text)
    
    def get_selected_dvi_d2_background_refresh_option(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css_selector("#backgroundrefreshrate1")
    
    def get_dvi_d2_background_refresh_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#backgroundrefreshrate1")
    
    def set_dvi_d2_background_refresh_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#backgroundrefreshrate1", text)
    
    def get_selected_dvi_d2_colour_depth_option(self):
        time.sleep(2)
        return self.get_selected_value_of_select_element_by_css_selector("#colourdepth1")
    
    def get_dvi_d2_colour_depth_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#colourdepth1")
    
    def set_dvi_d2_colour_depth_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#colourdepth1", text)
    
    def get_dvi_d2_use_default_ddc_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css_selector("#def_ddc1_enable")
    
    def set_dvi_d2_use_default_ddc_state(self, state):
        self.set_state_of_element_via_css_selector("#def_ddc1_enable", state)
    
    def get_dvi_d2_default_ddc_enabled_state(self):
        time.sleep(1)
        return self.get_enabled_state_of_element_via_css_selector("#ddc1_list")
    
    def get_selected_dvi_d2_default_ddc_option(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css_selector("#ddc1_list")
    
    def get_dvi_d2_default_ddc_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#ddc1_list")
    
    def set_dvi_d2_default_ddc_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#ddc1_list", text)
    
    def get_dvi_d2_hot_plug_detect_state(self):
        time.sleep(1)
        return self.get_state_of_element_via_css_selector("#hpd1_enable")
    
    def set_dvi_d2_hot_plug_detect_state(self, state):
        self.set_state_of_element_via_css_selector("#hpd1_enable", state)
    
    def get_dvi_d2_hot_plug_detect_period_enabled_state(self):
        time.sleep(1)
        return self.get_enabled_state_of_element_via_css_selector("#hpd1_period")
    
    def get_selected_dvi_d2_hot_plug_detect_period(self):
        time.sleep(1)
        return self.get_selected_value_of_select_element_by_css_selector("#hpd1_period")
    
    def get_dvi_d2_hot_plug_detect_period_options(self):
        time.sleep(1)
        return self.get_all_option_text_values_from_select_element_by_css_selector("#hpd1_period")
    
    def set_dvi_d2_hot_plug_detect_period_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#hpd1_period", text)
    
    def update_config_form(self):
        text = self.click_update_button("#configForm_submit")
        time.sleep(1)
        return text

    
    

    
    

    
    

    
    

    
    
    
    
#     def get_peak_bandwidth_percentage(self):
#         time.sleep(0.5)
#         return self.get_text_of_element_via_css_selector("div#bw_tr_value")
#     
#     def get_peak_bandwidth_slider_position(self):
#         return self.get_css_value_of_element_via_css_selector("#bw_tr_knob", "left").replace("px", "")
# 
#     def get_click_point_for_percentage(self, percent):
#         print("----------------------------")
#         print("Percent: %d" %percent)
#         percent_times_2 = percent*2
#         print("Precent times 2: %d" %percent_times_2)
#         abs_value = abs((percent*2)-2)
#         print("Absolute value after minus 2: %d" %abs_value)
#         target = abs_value+8
#         print("Target: %d" %target)
#         return target
#     
#     def set_peak_bandwidth_slider_to_percent(self, percent):
#         target = self.get_click_point_for_percentage(percent)
#         slide = ActionChains(self.driver)
#         slide.move_to_element_with_offset(self.driver.find_element_by_css_selector("#bw_tr_slider"), target, 0).click().perform()

    
    
    