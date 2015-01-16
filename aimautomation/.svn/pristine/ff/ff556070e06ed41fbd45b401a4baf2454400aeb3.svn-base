'''
Created on 17 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimBlackBoxTests(BaseAimRegressionTest):
    
    def test_blackbox_favicon_is_present(self):
        self._macros.open_AIM_homepage_on_base_url()
        self.assertEqual(self._macros.get_favicon_href(), self._baseurl + "/admin/images/ipath/favicon.ico")
        
    def test_ipath_branding_is_shown(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertEqual(self._macros.get_page_logo(), "Black Box")
        
    def test_ipath_serv_switch_is_shown(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertEqual(self._macros.get_page_name(), "ServSwitch iPATH - Black Box IP Access Manager")
        
    def test_ipath_is_shown_in_page_footer(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertTrue("iPATH" in self._macros.get_footer_text())
    
    def test_remote_is_shown_on_tab_links(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertEqual(self._macros.get_text_for_remote_tab(), "REMOTES")

    def test_local_is_shown_on_tab_links(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertEqual(self._macros.get_text_for_local_tab(), "LOCALS")
    
    def test_remote_is_shown_in_receivers_widget_title(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertEqual(self._macros.get_receiver_widget_header(), "View all Remotes\nLatest Remotes Added")

    def test_local_is_shown_in_transmitters_widget_title(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self.assertEqual(self._macros.get_transmitter_widget_header(), "View all Locals\nLatest Locals Added")
        
    def test_remotes_page_has_correct_subtab_links(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self._macros.open_remotes_tab()
        self.assertEqual(self._macros.get_text_of_remote_subtab_link("1"), "View Remotes")
        self.assertEqual(self._macros.get_text_of_remote_subtab_link("2"), "View Remote Groups")
        self.assertEqual(self._macros.get_text_of_remote_subtab_link("3"), "Add Remote Group")

    def test_locals_page_has_correct_subtab_links(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self._macros.open_locals_tab()
        self.assertEqual(self._macros.get_text_of_local_subtab_link("1"), "View Locals")
    
    def test_remotes_page_links_operate_correctly(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self._macros.open_remotes_tab()
        self._macros.open_view_remotes_page()
        self.assertEquals(self._macros.get_text_of_page_header(), "Remotes")
        self._macros.open_view_remote_groups_page()
        self.assertEquals(self._macros.get_text_of_page_header(), "Remote Groups")
        self._macros.open_add_remote_groups_page()
        self.assertEquals(self._macros.get_text_of_page_header(), "Remote Groups > Add Remote Group")
        self._macros.open_update_remote_firmware_page()
        self.assertTrue(self._macros.get_text_of_page_header(), "Upgrade iPATH Software")
    
    def test_locals_page_links_operate_correctly(self):
        self._macros.open_AIM_homepage_on_base_url()
        self._macros.login_as("admin", "password", False)
        self._macros.open_locals_tab()
        self._macros.open_update_local_firmware_page()
        self.assertEquals(self._macros.get_text_of_page_header(), "Upgrade iPATH Software")
        self._macros.open_view_locals_page()
        self.assertEquals(self._macros.get_text_of_page_header(), "Locals")