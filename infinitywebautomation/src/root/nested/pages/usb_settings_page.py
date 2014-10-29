'''
Created on 17 Dec 2013

@author: Mark
'''
from root.nested.pages.base_page import BasePage

class UsbSettingsPage(BasePage):
    
    def get_allow_human_interface_devices_only_state(self):
        return self.get_state_of_element_via_css_selector("#hid_only")

    def set_allow_human_interface_devices_only_state(self, state):
        self.set_state_of_element_via_css_selector("#hid_only", state)
    
    def get_isochronous_endpoint_osd_alerts_state(self):
        return self.get_state_of_element_via_css_selector("#isochronous_user_warning")
    
    def set_isochronous_endpoint_osd_alert_state(self, state):
        self.set_state_of_element_via_css_selector("#isochronous_user_warning", state)
    
    def get_isochronous_endpoint_attach_state(self):
        return self.get_state_of_element_via_css_selector("#isochronous_enabled")
    
    def set_isochronous_endpoint_attach_state(self, state):
        self.set_state_of_element_via_css_selector("#isochronous_enabled", state)
    
    def get_merge_top_left_state(self):
        return self.get_state_of_element_via_css_selector("#rx_port_1_merge")
    
    def set_merge_top_left_state(self, state):
        self.set_state_of_element_via_css_selector("#rx_port_1_merge", state)
    
    def get_merge_top_right_state(self):
        return self.get_state_of_element_via_css_selector("#rx_port_2_merge")
    
    def set_merge_top_right_state(self, state):
        self.set_state_of_element_via_css_selector("#rx_port_2_merge", state)
    
    def get_merge_bottom_left_state(self):
        return self.get_state_of_element_via_css_selector("#rx_port_3_merge")
    
    def set_merge_bottom_left_state(self, state):
        self.set_state_of_element_via_css_selector("#rx_port_3_merge", state)
    
    def get_merge_bottom_right_state(self):
        return self.get_state_of_element_via_css_selector("#rx_port_4_merge")
    
    def set_merge_bottom_right_state(self, state):
        self.set_state_of_element_via_css_selector("#rx_port_4_merge", state)
        
    def get_map_top_left(self):
        return self.get_selected_value_of_select_element_by_css_selector("#rx_port_1_reservation_tx_port") 

    def get_map_top_left_options(self):
        return self.get_all_option_text_values_from_select_element_by_css_selector("#rx_port_1_reservation_tx_port")

    def set_map_top_left(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#rx_port_1_reservation_tx_port", text)
    
    def get_map_top_right(self):
        return self.get_selected_value_of_select_element_by_css_selector("#rx_port_2_reservation_tx_port") 
    
    def get_map_top_right_options(self):
        return self.get_all_option_text_values_from_select_element_by_css_selector("#rx_port_2_reservation_tx_port")
    
    def set_map_top_right(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#rx_port_2_reservation_tx_port", text)
    
    def get_map_bottom_left(self):
        return self.get_selected_value_of_select_element_by_css_selector("#rx_port_3_reservation_tx_port") 

    def get_map_bottom_left_options(self):
        return self.get_all_option_text_values_from_select_element_by_css_selector("#rx_port_3_reservation_tx_port")
    
    def set_map_bottom_left(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#rx_port_3_reservation_tx_port", text)
    
    def get_map_bottom_right(self):
        return self.get_selected_value_of_select_element_by_css_selector("#rx_port_4_reservation_tx_port") 
    
    def get_map_bottom_right_options(self):
        return self.get_all_option_text_values_from_select_element_by_css_selector("#rx_port_4_reservation_tx_port")

    def set_map_bottom_right(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#rx_port_4_reservation_tx_port", text)
    
    def get_enabled_advanced_features_state(self):
        return self.get_state_of_element_via_css_selector("#rx_q_config_enable")

    def set_enabled_advanced_features_state(self, state):
        self.set_state_of_element_via_css_selector("#rx_q_config_enable", state)
    
    def get_top_left_kernel_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_1_k")
        
    def get_top_left_kernel_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_1_k", "value")
    
    def set_top_left_kernel_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_1_k", text)
    
    def get_top_left_user_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_1_u")
    
    def get_top_left_user_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_1_u", "value")

    def set_top_left_user_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_1_u", text)
    
    def get_top_right_kernel_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_2_k")
        
    def get_top_right_kernel_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_2_k", "value")
    
    def set_top_right_kernel_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_2_k", text)
    
    def get_top_right_user_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_2_u")
    
    def get_top_right_user_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_2_u", "value")

    def set_top_right_user_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_2_u", text)

    def get_bottom_left_kernel_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_3_k")
        
    def get_bottom_left_kernel_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_3_k", "value")
    
    def set_bottom_left_kernel_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_3_k", text)
    
    def get_bottom_left_user_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_3_u")
    
    def get_bottom_left_user_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_3_u", "value")

    def set_bottom_left_user_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_3_u", text)
    
    def get_bottom_right_kernel_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_4_k")
    
    def get_bottom_right_kernel_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_4_k", "value")
    
    def set_bottom_right_kernel_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_4_k", text)
    
    def get_bottom_right_user_enabled(self):
        return self.get_enabled_state_of_element_via_css_selector("#rx_port_4_u")
    
    def get_bottom_right_user_value(self):
        return self.get_attribute_of_element_via_css_selector("#rx_port_4_u", "value")

    def set_bottom_right_user_value(self, text):
        self.set_text_of_element_via_css_selector("#rx_port_4_u", text)
    
    def get_enable_dummy_boot_keyboard_state(self):
        return self.get_state_of_element_via_css_selector("#fk_enable")
    
    def set_enable_dummy_boot_keyboard_state(self, state):
        self.set_state_of_element_via_css_selector("#fk_enable", state)
    
    def get_disable_hi_speed_state(self):
        return self.get_state_of_element_via_css_selector("#dis_hispeed")
    
    def set_disable_hi_speed_state(self, state):
        self.set_state_of_element_via_css_selector("#dis_hispeed", state)
    
    def get_selected_hub_size_option(self):
        return self.get_selected_value_of_select_element_by_css_selector("#hub_size")
    
    def get_hub_size_options(self):
        return self.get_all_option_text_values_from_select_element_by_css_selector("#hub_size")
    
    def set_hub_size_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#hub_size", text)
    
    def get_selected_reserved_port_range_option(self):
        return self.get_selected_value_of_select_element_by_css_selector("#reserved_port_range_tx")
    
    def get_reserved_port_range_options(self):
        return self.get_all_option_text_values_from_select_element_by_css_selector("#reserved_port_range_tx")
    
    def set_reserved_port_range_option(self, text):
        self.select_visible_text_value_of_select_element_by_css_selector("#reserved_port_range_tx", text)
    
    def update_config_form(self):
        return self.click_update_button("#configForm_submit")
