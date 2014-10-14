'''
Created on 30 Apr 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimLoginPageDefaultsTest(BaseAimRegressionTest):

    def test_can_open_login_page(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertEqual(self._page.get_page_title(), "AIM")
        
    def test_adder_branding_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertEqual(self._page.get_page_logo(), "Adder")
        
    def test_adder_infinty_management_suite_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertEqual(self._page.get_page_name(), "AdderLink Infinity Management Suite")
        
    def test_username_field_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertTrue(self._page.get_located_username_input())
        
    def test_password_field_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertTrue(self._page.get_located_password_input())

    def test_initial_username_validation_is_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertEqual(self._page.get_username_validation_tool_tip_text("warning"), "Username::This field must not be empty. ")
        
    def test_username_validation_updates_once_text_is_entered_into_the_field(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.enter_text_into_input_field("username", "test")
        self.assertEqual(self._page.get_username_validation_tool_tip_text("ok"), "Username::This field must not be empty. ")
        
    def test_background_colour_is_black(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertEqual(self._page.get_back_ground_colour(), "rgba(0, 0, 0, 1)")
        
    def test_background_image_is_present_and_set_to_repeat(self):
        self._page.open_AIM_homepage_on_base_url()
#         NOTE: different browsers are returning a different string for the image url
        if self._page.get_back_ground_image() == "url(\"" + self._baseurl + "/admin/images/background.png\")":
            found = True
        elif self._page.get_back_ground_image() == "url(" + self._baseurl + "/admin/images/background.png)":
            found = True
        else: found = False    
        self.assertTrue(found)
        self.assertEqual(self._page.get_back_ground_repeat_property(), "repeat-x")
    
    def test_adder_favicon_is_present(self):
        self._page.open_AIM_homepage_on_base_url()
        self.assertEqual(self._page.get_favicon_href(), self._baseurl + "/admin/images/adder/favicon.ico")
