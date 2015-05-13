'''
Created on 19 Dec 2013

@author: Mark
'''
from root.nested.pages.home_page import HomePage
from root.nested.tests.base_infinity_regression_test import \
    BaseInfinityRegressionTest


class SystemMessagesPageTest(BaseInfinityRegressionTest):
    
    def test_can_open_system_messages_page(self):
        home_page = HomePage(self._driver, self._wait)
        system_messages_page = home_page.open_system_messages_page()
        self.assertEqual("System Messages", system_messages_page.get_logo_text())
        self.assertEqual("System Messages", system_messages_page.get_main_header_text())
        
    def test_can_disable_system_messages(self):
        home_page = HomePage(self._driver, self._wait)
        system_messages_page = home_page.open_system_messages_page()
        self.assertTrue(system_messages_page.get_enable_system_messages_state())
        system_messages_page.set_enable_system_messages_state(False)
        system_messages_page.update_config_form()
        self.assertFalse(system_messages_page.get_enable_system_messages_state())
        system_messages_page.set_enable_system_messages_state(True)
        system_messages_page.set_store_system_mesages_in_unit(True)
        system_messages_page.update_config_form()
    
    def test_can_view_system_messages(self):
        home_page = HomePage(self._driver, self._wait)
        system_messages_page = home_page.open_system_messages_page()
        main_window = system_messages_page.get_main_window_handle()
        system_messages_page.click_view_messages()
        messages = system_messages_page.get_system_messages_from_new_window(main_window)
        self.assertTrue(system_messages_page.messages_start_header_is_correct(messages))