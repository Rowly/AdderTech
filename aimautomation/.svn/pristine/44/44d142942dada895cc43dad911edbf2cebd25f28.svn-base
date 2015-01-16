'''
Created on 1 May 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimLoginPageFunctionsTest(BaseAimRegressionTest):
    
    def test_can_login_with_valid_credentials(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.ensure_logged_out()
        self._page.login_as("admin", "password", False)
        self.assertTrue(self._page.get_located_dashboard_link())
        
    def test_cannot_login_with_invalid_credentials(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.ensure_logged_out()
        self._page.login_as("admin", "invalid", False)
        self.assertTrue(self._page.get_located_login_error_message())
        self.assertEqual(self._page.get_information_to_user_text(), "The username and password you supplied are not valid")
    