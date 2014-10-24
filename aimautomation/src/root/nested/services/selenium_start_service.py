'''
Created on 29 Apr 2013

@author: Mark.rowlands
'''

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class SeleniumStartService():
    
    firefox = DesiredCapabilities.FIREFOX.copy()
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    chrome = options.to_capabilities()
    
    phantomjs = DesiredCapabilities.PHANTOMJS.copy()
    phantomjs["phantomjs.binary.path"] = "C:\phantomjs-1.9.7-windows\phantomjs.exe"

    def start_driver(self):
        return webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', 
                                        desired_capabilities=self.chrome)