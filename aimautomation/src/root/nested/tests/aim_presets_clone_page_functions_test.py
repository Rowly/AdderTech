'''
Created on 25 Jun 2013

@author: Mark.rowlands
'''
from root.nested.tests.base_aim_regression_test import BaseAimRegressionTest


class AimPresetsClonePageFunctionsTest(BaseAimRegressionTest):

    def test_can_clone_existing_preset(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        self.assertEqual(self._page.get_preset_name(presets[-1])[-6:],
                         "(Copy)")
        self._page.click_preset_delete(presets[-1])
        self._page.click_lightbox_delete_button()

    def test_can_cancel_clone_existing_preset(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.click_cancel()
        new_presets = self._page.get_list_of_presets()
        self.assertEqual(len(presets), len(new_presets))

    def test_can_change_name_of_cloned_preset(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.set_preset_name_via_config_page("preset clone")
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        self.assertEqual(self._page.get_preset_name(presets[-1]),
                         "preset clone")
        self._page.click_preset_delete(presets[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_description_of_cloned_preset(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.set_preset_description_via_config_page("preset clone")
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        self.assertEqual(self._page.get_preset_description(presets[-1]),
                         "preset clone")
        self._page.click_preset_delete(presets[-1])
        self._page.click_lightbox_delete_button()

    def test_can_change_allowed_connections_preset_to_view_only(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.select_preset_connection_view_only()
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        p = presets[-1]
        srcs = self._page.get_preset_connection_image_srcs(p)
        self.assertTrue(self._silk_dir + "eye.png" in srcs)
        self.assertFalse(self._page.get_preset_conx_shared_visibility(p))
        self.assertFalse(self._page.get_preset_conx_exclusive_visibility(p))
        self._page.click_preset_delete(p)
        self._page.click_lightbox_delete_button()

    def test_can_change_allowed_connections_to_shared(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.select_preset_connection_shared()
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        p = presets[-1]
        srcs = self._page.get_preset_connection_image_srcs(p)
        self.assertTrue(self._silk_dir + "eye.png" in srcs)
        self.assertTrue(self._silk_dir + "multicast.png" in srcs)
        self.assertTrue(self._page.get_preset_conx_view_only_visibility(p))
        self.assertTrue(self._page.get_preset_conx_shared_visibility(p))
        self.assertFalse(self._page.get_preset_conx_exclusive_visibility(p))
        self._page.click_preset_delete(p)
        self._page.click_lightbox_delete_button()

    def test_can_change_allowed_connections_to_exclusive(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.select_preset_connection_exclusive()
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        p = presets[-1]
        srcs = self._page.get_preset_connection_image_srcs(p)
        self.assertTrue(self._silk_dir + "lock.png" in srcs)
        self.assertFalse(self._page.get_preset_conx_view_only_visibility(p))
        self.assertFalse(self._page.get_preset_conx_shared_visibility(p))
        self.assertTrue(self._page.get_preset_conx_exclusive_visibility(p))
        self._page.click_preset_delete(p)
        self._page.click_lightbox_delete_button()

    def test_can_change_allowed_connections_to_all(self):
        self._page.open_AIM_homepage_on_base_url()
        self._page.login_as("admin", "password", False)
        self._page.open_presets_tab()
        presets = self._page.get_list_of_presets()
        self._page.click_preset_clone(presets[-1])
        self._page.select_preset_connection_all()
        self._page.click_save()
        presets = self._page.get_list_of_presets()
        p = presets[-1]
        srcs = self._page.get_preset_connection_image_srcs(p)
        self.assertTrue(self._silk_dir + "eye.png" in srcs)
        self.assertTrue(self._silk_dir + "multicast.png" in srcs)
        self.assertTrue(self._silk_dir + "lock.png" in srcs)
        self.assertTrue(self._page.get_preset_conx_view_only_visibility(p))
        self.assertTrue(self._page.get_preset_conx_shared_visibility(p))
        self.assertTrue(self._page.get_preset_conx_exclusive_visibility(p))
        self._page.click_preset_delete(p)
        self._page.click_lightbox_delete_button()
