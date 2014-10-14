'''
Created on 20 Nov 2013

@author: Mark
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest

class AimServersPageFunctionsTest(BaseAimRegressionTest):

    def test_can_change_primary_server_name(self):
        primary = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "primary":
                primary = server
                index = servers.index(server)
                break
        if primary is not None:
            original = self._page.get_server_name(primary)
            self._page.click_server_config(primary)
            self._page.set_server_name(original + " edit")
            self._page.click_save()
            primary = self._page.get_list_of_servers()[index]
            new = self._page.get_server_name(primary)
            self.assertNotEqual(original, new)
            self._page.click_server_config(primary)
            self._page.set_server_name(original)
            self._page.click_save()
        else: raise RuntimeError("No Primary server in cluster")


    def test_can_change_primary_server_description(self):
        primary = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "primary":
                primary = server
                index = servers.index(server)
                break
        if primary is not None:
            original = self._page.get_server_description(primary)
            self._page.click_server_config(primary)
            self._page.set_server_description(original + " edit")
            self._page.click_save()
            primary = self._page.get_list_of_servers()[index]
            new = self._page.get_server_description(primary)
            self.assertNotEqual(original, new)
            self._page.click_server_config(primary)
            self._page.set_server_description(original)
            self._page.click_save()
        else: raise RuntimeError("No Primary server in cluster")

    def test_can_change_primary_server_location(self):
        primary = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "primary":
                primary = server
                index = servers.index(server)
                break
        if primary is not None:
            original = self._page.get_server_location(primary)
            self._page.click_server_config(primary)
            self._page.set_server_location(original + " edit")
            self._page.click_save()
            primary = self._page.get_list_of_servers()[index]
            new = self._page.get_server_location(primary)
            self.assertNotEqual(original, new)
            self._page.click_server_config(primary)
            self._page.set_server_location(original)
            self._page.click_save()
        else: raise RuntimeError("No Primary server in cluster")

    def test_can_change_backup_server_name(self):
        backup = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "backup":
                backup = server
                index = servers.index(server)
                break
        if backup is not None:
            original = self._page.get_server_name(backup)
            self._page.click_server_config(backup)
            self._page.set_server_name(original + " edit")
            self._page.click_save()
            backup = self._page.get_list_of_servers()[index]
            new = self._page.get_server_name(backup)
            self.assertNotEqual(original, new)
            self._page.click_server_config(backup)
            self._page.set_server_name(original)
            self._page.click_save()
        else: raise RuntimeError("No Backup server in cluster")

    def test_can_change_backup_server_description(self):
        backup = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "backup":
                backup = server
                index = servers.index(server)
                break
        if backup is not None:
            original = self._page.get_server_description(backup)
            self._page.click_server_config(backup)
            self._page.set_server_description(original + " edit")
            self._page.click_save()
            backup = self._page.get_list_of_servers()[index]
            new = self._page.get_server_description(backup)
            self.assertNotEqual(original, new)
            self._page.click_server_config(backup)
            self._page.set_server_description(original)
            self._page.click_save()
        else: raise RuntimeError("No Backup server in cluster")

    def test_can_change_backup_server_location(self):
        backup = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "backup":
                backup = server
                index = servers.index(server)
                break
        if backup is not None:
            original = self._page.get_server_location(backup)
            self._page.click_server_config(backup)
            self._page.set_server_location(original + " edit")
            self._page.click_save()
            backup = self._page.get_list_of_servers()[index]
            new = self._page.get_server_location(backup)
            self.assertNotEqual(original, new)
            self._page.click_server_config(backup)
            self._page.set_server_location(original)
            self._page.click_save()
        else: raise RuntimeError("No Backup server in cluster")

    def test_can_open_backup_server_local_config(self):
        backup = None
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_servers_tab()
        servers = self._page.get_list_of_servers()
        for server in servers:
            if self._page.get_server_role(server) == "backup":
                backup = server
                break
        if backup is not None:
            name = self._page.get_server_name(backup)
            first_window = self._page.get_current_window_handle()
            self._page.click_non_primary_server_local_config(backup)
            self._page.switch_to_other_window_from(first_window)
            self.assertTrue(self._backup_url in self._page.get_current_url())
            self.assertEqual(name, self._page.get_server_name_from_backup_local_config())
        else: raise RuntimeError("No Backup server in cluster")