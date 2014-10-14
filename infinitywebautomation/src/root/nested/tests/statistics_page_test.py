'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.tests.base_infinity_regression_test import BaseInfinityRegressionTest
from root.nested.pages.home_page import HomePage

class StatisticsPageTest(BaseInfinityRegressionTest):
    
    def test_can_open_statistics_page(self):
        home_page = HomePage(self._driver, self._wait)
        statistics_page = home_page.open_statistics_page()
        self.assertEqual("Statistics", statistics_page.get_logo_text())
        self.assertEqual("Statistics", statistics_page.get_main_header_text())
    
    def test_can_enable_statistics_for_unit(self):
        home_page = HomePage(self._driver, self._wait)
        statistics_page = home_page.open_statistics_page()
        self.assertFalse(statistics_page.get_enable_statistics_state())
        statistics_page.set_enable_statistics_state(True)
        statistics_page.click_submit()
        self.assertTrue(statistics_page.get_appearance_of_graph())
        statistics_page.set_enable_statistics_state(False)
        statistics_page.click_submit()
        