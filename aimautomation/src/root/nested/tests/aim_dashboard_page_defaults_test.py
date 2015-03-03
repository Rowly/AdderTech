'''
Created on 2 May 2013

@author: Mark.rowlands
'''
import datetime
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimDashboardDefaultsTest(BaseAimRegressionTest):

    def test_adder_branding_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.assertEqual(self._page.get_page_logo(), "Adder")

    def test_adder_infinty_management_suite_is_shown(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.assertEqual(self._page.get_page_name(),
                         "AdderLink Infinity Management Suite")

    def test_aim_is_shown_in_page_footer(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.assertTrue("AIM" in self._page.get_footer_text())

    def test_time_and_date_shown_and_correct(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        aim_time = self._page.get_displayed_time_and_date()
        system_time = datetime.datetime.now().strftime("%H:%M, %a %d %b %Y")
        self.assertTrue(self._page.get_year_comparison(aim_time, system_time))
        self.assertTrue(self._page.get_month_comparison(aim_time, system_time))
        self.assertTrue(self._page.get_date_comparison(aim_time, system_time))
        self.assertTrue(self._page.get_day_comparison(aim_time, system_time))
        self.assertTrue(self._page.get_hour_comparison(aim_time, system_time))
        self.assertTrue(self._page.get_min_comparison(aim_time, system_time))

    def test_logout_button_is_present_and_displayed_correctly(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self.assertTrue(self._page.get_located_logout_button())
        self.assertEqual(self._page.get_logout_button_colour_property(),
                         "rgba(62, 107, 195, 1)")

    def test_footer_is_showing_correct_firmware_version(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        text = self._page.get_footer_text()
        self.assertEqual(text, "AIM %s" % self._version)
