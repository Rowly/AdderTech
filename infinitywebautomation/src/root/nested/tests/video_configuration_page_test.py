'''
Created on 6 Jan 2014

@author: Mark
'''
from root.nested.tests.base_infinity_regression_test import unittest
from root.nested.tests.base_infinity_regression_test import BaseInfinityRegressionTest
from root.nested.pages.home_page import HomePage
from root.nested.services.parameters import parameter_singleton

class VideoConfigurationPageTest(BaseInfinityRegressionTest):
    
    def test_can_open_video_configuration_page(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertEqual("Video Configuration", video_page.get_logo_text())
        self.assertEqual("Video Configuration", video_page.get_main_header_text())
    
    def test_can_change_dvi_d1_background_refresh(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertEqual(video_page.get_selected_dvi_d1_background_refresh_option(), "every 32 frames")
        options = video_page.get_dvi_d1_background_refresh_options()
        counter = 0
        for counter in range(len(options)):
            video_page.set_dvi_d1_background_refresh_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d1_background_refresh_option(), options[counter])
        video_page.set_dvi_d1_background_refresh_option("every 32 frames")
        video_page.update_config_form()
          
    def test_can_change_dvi_d1_colour_depth(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            raise unittest.SkipTest("Colour Depth removed in v3.3")
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertEqual(video_page.get_selected_dvi_d1_colour_depth_option(), "24 bit")
        options = video_page.get_dvi_d1_colour_depth_options()
        counter = 0
        for counter in range(len(options)):
            options = video_page.get_dvi_d1_colour_depth_options()
            video_page.set_dvi_d1_colour_depth_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d1_colour_depth_option(), options[counter])
        video_page.set_dvi_d1_colour_depth_option("24 bit")
        video_page.update_config_form()
           
    def test_can_enable_dvi_d1_use_default_ddc(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertFalse(video_page.get_dvi_d1_use_default_ddc_state())
        video_page.set_dvi_d1_use_default_ddc_state(True)
        video_page.update_config_form()
        self.assertTrue(video_page.get_dvi_d1_use_default_ddc_state())
        video_page.set_dvi_d1_use_default_ddc_state(False)
        video_page.update_config_form()
     
    def test_can_change_dvi_d1_default_ddc(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertFalse(video_page.get_dvi_d1_default_ddc_enabled_state())
        ##
        #video_page.set_dvi_d1_hot_plug_detect_state(False)
        ##
        video_page.set_dvi_d1_use_default_ddc_state(True)
        options = video_page.get_dvi_d1_default_ddc_options()
        counter = 0
        for counter in range(len(options)):
            options = video_page.get_dvi_d1_default_ddc_options()
            video_page.set_dvi_d1_default_ddc_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d1_default_ddc_option(), options[counter])
        video_page.set_dvi_d1_default_ddc_option("GENERIC 4:3")
        video_page.set_dvi_d1_use_default_ddc_state(False)
        ##
        #video_page.set_dvi_d1_hot_plug_detect_state(True)
        ##
        video_page.update_config_form()
        
    def test_can_disable_dvi_d1_hot_plug_detect(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertTrue(video_page.get_dvi_d1_hot_plug_detect_state())
        self.assertTrue(video_page.get_dvi_d1_hot_plug_detect_period_enabled_state())  
        video_page.set_dvi_d1_hot_plug_detect_state(False)
        video_page.update_config_form()
        self.assertFalse(video_page.get_dvi_d1_hot_plug_detect_state())
        self.assertFalse(video_page.get_dvi_d1_hot_plug_detect_period_enabled_state())
        video_page.set_dvi_d1_hot_plug_detect_state(True)
        video_page.update_config_form()
        
    def test_can_change_dvi_d1_hot_plug_detect_period(self):
        self.check_device_is_transmitter()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertTrue(video_page.get_dvi_d1_hot_plug_detect_period_enabled_state())
        self.assertEqual(video_page.get_selected_dvi_d1_hot_plug_detect_period(), "Default - 100ms")
        options = video_page.get_dvi_d1_hot_plug_detect_period_options()
        counter = 0
        for counter in range(len(options)):
            options = video_page.get_dvi_d1_hot_plug_detect_period_options()
            video_page.set_dvi_d1_hot_plug_detect_period_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d1_hot_plug_detect_period(), options[counter])
        video_page.set_dvi_d1_hot_plug_detect_period_option("Default - 100ms")
        video_page.update_config_form()
               
    def test_can_change_dvi_d2_background_refresh(self):
        self.check_device_is_transmitter()
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertEqual(video_page.get_selected_dvi_d2_background_refresh_option(), "every 32 frames")
        options = video_page.get_dvi_d2_background_refresh_options()
        counter = 0
        for counter in range(len(options)):
            video_page.set_dvi_d2_background_refresh_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d2_background_refresh_option(), options[counter])
        video_page.set_dvi_d2_background_refresh_option("every 32 frames")
        video_page.update_config_form()
           
    def test_can_change_dvi_d2_colour_depth(self):
        version = parameter_singleton["version"]
        split_version = version.replace("v", "").split(".")
        if int(split_version[0]) >= 3 and int(split_version[1]) >= 3:
            raise unittest.SkipTest("Colour Depth removed in v3.3")
        self.check_device_is_transmitter()
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertEqual(video_page.get_selected_dvi_d2_colour_depth_option(), "24 bit")
        options = video_page.get_dvi_d2_colour_depth_options()
        counter = 0
        for counter in range(len(options)):
            video_page.set_dvi_d2_colour_depth_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d2_colour_depth_option(), options[counter])
        video_page.set_dvi_d2_colour_depth_option("24 bit")
        video_page.update_config_form()
            
    def test_can_enable_dvi_d2_use_default_ddc(self):
        self.check_device_is_transmitter()
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertFalse(video_page.get_dvi_d2_use_default_ddc_state())
        video_page.set_dvi_d2_use_default_ddc_state(True)
        video_page.update_config_form()
        self.assertTrue(video_page.get_dvi_d2_use_default_ddc_state())
        video_page.set_dvi_d2_use_default_ddc_state(False)
        video_page.update_config_form()
      
    def test_can_change_dvi_d2_default_ddc(self):
        self.check_device_is_transmitter()
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertFalse(video_page.get_dvi_d2_default_ddc_enabled_state())
        video_page.set_dvi_d2_use_default_ddc_state(True)
        options = video_page.get_dvi_d2_default_ddc_options()
        counter = 0
        for counter in range(len(options)):
            options = video_page.get_dvi_d2_default_ddc_options()
            video_page.set_dvi_d2_default_ddc_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d2_default_ddc_option(), options[counter])
        video_page.set_dvi_d2_default_ddc_option("GENERIC 4:3")
        video_page.set_dvi_d2_use_default_ddc_state(False)
        video_page.update_config_form()
         
    def test_can_disable_dvi_d2_hot_plug_detect(self):
        self.check_device_is_transmitter()
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertTrue(video_page.get_dvi_d2_hot_plug_detect_state())
        self.assertTrue(video_page.get_dvi_d2_hot_plug_detect_period_enabled_state())  
        video_page.set_dvi_d2_hot_plug_detect_state(False)
        video_page.update_config_form()
        self.assertFalse(video_page.get_dvi_d2_hot_plug_detect_state())
        self.assertFalse(video_page.get_dvi_d2_hot_plug_detect_period_enabled_state())
        video_page.set_dvi_d2_hot_plug_detect_state(True)
        video_page.update_config_form()
         
    def test_can_change_dvi_d2_hot_plug_detect_period(self):
        self.check_device_is_transmitter()
        self.check_device_is_dual()
        home_page = HomePage(self._driver, self._wait)
        video_page = home_page.open_video_configuration_page()
        self.assertTrue(video_page.get_dvi_d2_hot_plug_detect_period_enabled_state())
        self.assertEqual(video_page.get_selected_dvi_d2_hot_plug_detect_period(), "Default - 100ms")
        options = video_page.get_dvi_d2_hot_plug_detect_period_options()
        counter = 0
        for counter in range(len(options)):
            options = video_page.get_dvi_d2_hot_plug_detect_period_options()
            video_page.set_dvi_d2_hot_plug_detect_period_option(options[counter])
            video_page.update_config_form()
            self.assertEqual(video_page.get_selected_dvi_d2_hot_plug_detect_period(), options[counter])
        video_page.set_dvi_d2_hot_plug_detect_period_option("Default - 100ms")
        video_page.update_config_form()