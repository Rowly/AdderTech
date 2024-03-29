'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.home_page import HomePage
from root.nested.tests.base_infinity_regression_test import \
    BaseInfinityRegressionTest


class AimManagerPageTest(BaseInfinityRegressionTest):

    def test_can_open_aim_manager_page(self):
        home_page = HomePage(self._driver, self._wait)
        aim_manager_page = home_page.open_aim_manager_page()
        logo = aim_manager_page.get_logo_text()
        header = aim_manager_page.get_main_header_text()
        self.assertEqual("AIM Manager", logo)
        self.assertEqual("AIM Manager", header)
