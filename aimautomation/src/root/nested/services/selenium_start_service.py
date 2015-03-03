'''
Created on 29 Apr 2013

@author: Mark.rowlands
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumStartService():

    firefox = DesiredCapabilities.FIREFOX.copy()

    options = webdriver.ChromeOptions()
    switches = ["ignore-certificate-errors"]
    options.add_experimental_option("excludeSwitches", switches)
    chrome = options.to_capabilities()

    phantomjs = DesiredCapabilities.PHANTOMJS.copy()
    path = "C:\phantomjs-1.9.7-windows\phantomjs.exe"
    phantomjs["phantomjs.binary.path"] = path

    def start_driver(self):
        hub = 'http://127.0.0.1:4444/wd/hub'
        return webdriver.Remote(command_executor=hub,
                                desired_capabilities=self.chrome)
