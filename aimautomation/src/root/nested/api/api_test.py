'''
Created on 24 Oct 2014

@author: Mark
'''
import requests
import unittest
from xml.etree import ElementTree
import time


class ApiTest(unittest.TestCase):

    base_ip = "10.10.10.10"
    version = "2"
    token = ""
    d_dict = {}
    channels_list = []
    presets_list = []

    def setUp(self):
        payload = {"v": self.version,
                   "method": "login",
                   "username": "admin",
                   "password": "password"}
        response = self.send_get_request(payload)
        data = ElementTree.fromstring(response.content)
        self.assertEqual(data.find("success").text, "1")
        self.token = data.find("token").text

    def tearDown(self):
        payload = {"v": self.version,
                   "method": "logout",
                   "token": self.token}
        response = self.send_get_request(payload)
        self.confirm_success(response.content)

    def test_can_get_devices(self):
        payload = {"v": self.version,
                   "token": self.token,
                   "method": "get_devices",
                   "show_all": "1"}
        response = self.send_get_request(payload)
        self.confirm_success(response.content)
        tree = self.get_element_tree(response.content)
        devices = tree.findall(".//device")
        for device in devices:
            self.d_dict[device.find("d_id").text] = device.find("d_type").text
        self.assertTrue(len(self.d_dict) > 0)

    def test_can_get_channels(self):
        payload = {"v": self.version,
                   "token": self.token,
                   "method": "get_channels"}
        response = self.send_get_request(payload)
        self.confirm_success(response.content)
        tree = self.get_element_tree(response.content)
        channels = tree.findall(".//channel")
        for channel in channels:
            self.channels_list.append(channel.find("c_id").text)
        self.assertTrue(len(self.channels_list) > 0)

    def test_can_get_presets(self):
        if self.presets_list:
            self.presets_list.clear()
        payload = {"v": self.version,
                   "token": self.token,
                   "method": "get_presets"}
        response = self.send_get_request(payload)
        self.confirm_success(response.content)
        tree = self.get_element_tree(response.content)
        presets = tree.findall(".//connection_preset")
        self.presets_list = [preset.find("cp_id").text
                             for preset in presets]
        self.assertTrue(len(self.presets_list) > 0)

    def test_connect_and_disconnect_channel(self):
        if not self.channels_list:
            self.test_get_channels()
        if not self.d_dict:
            self.test_get_devices()
        receivers = [device
                     for device in self.d_dict
                     if self.d_dict[device] == "rx"]
        for receiver in receivers:
            for channel in self.channels_list:
                payload = {"v": self.version,
                           "method": "connect_channel",
                           "token": self.token,
                           "c_id": channel,
                           "rx_id": receiver,
                           "exclusive": "1"}
                response = self.send_get_request(payload)
                self.confirm_success(response.content)
                time.sleep(3)
                payload = {"v": self.version,
                           "method": "disconnect_channel",
                           "token": self.token,
                           "rx_id": receiver}
                response = self.send_get_request(payload)
                self.confirm_success(response.content)
                time.sleep(3)

    def test_connect_and_disconnect_preset(self):
        if not self.presets_list:
            self.test_can_get_presets()
        if not self.d_dict:
            self.test_get_devices()
        for preset in self.presets_list:
            payload = {"v": self.version,
                       "method": "connect_preset",
                       "token": self.token,
                       "id": preset,
                       "force": "1"}
            response = self.send_get_request(payload)
            self.confirm_success(response.content)
            time.sleep(3)
            payload = {"v": self.version,
                       "method": "disconnect_preset",
                       "token": self.token,
                       "id": preset}
            response = self.send_get_request(payload)
            self.confirm_success(response.content)
            time.sleep(3)

    def test_create_and_delete_preset(self):
        if not self.channels_list:
            self.test_get_channels()
        if not self.d_dict:
            self.test_get_devices()
        if not self.presets_list:
            self.test_can_get_presets()
        presets_before = self.presets_list.copy()
        receivers = [device for device
                     in self.d_dict
                     if self.d_dict[device] == "rx"]
        payload = {"v": str(int(self.version) + 1),
                   "method": "create_preset",
                   "token": self.token,
                   "name": "test_preset",
                   "pairs": self.channels_list[-1] + "-" + receivers[0],
                   "allowed": "vse"}
        response = self.send_get_request(payload)
        self.confirm_success(response.content)
        self.test_can_get_presets()
        presets_after = self.presets_list
        self.assertTrue(len(presets_after) > len(presets_before))
        pid = list(set(presets_after) - set(presets_before))
        pid = pid[0]
        payload = {"v": str(int(self.version) + 1),
                   "method": "delete_preset",
                   "token": self.token,
                   "id": pid}
        response = self.send_get_request(payload)
        self.confirm_success(response.content)
        self.test_can_get_presets()
        final_presets = self.presets_list
        self.assertEqual(final_presets, presets_before)

    def send_get_request(self, payload):
        r = requests.get("http://%s/api" % self.base_ip, params=payload)
        self.assertEqual(r.status_code, 200)
        return r

    def get_element_tree(self, content):
        return ElementTree.fromstring(content)

    def confirm_success(self, content):
        tree = ElementTree.fromstring(content)
        self.assertEqual(tree.find("success").text, "1")
