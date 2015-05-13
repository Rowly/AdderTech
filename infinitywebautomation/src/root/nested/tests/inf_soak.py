'''
Created on 19 Mar 2015

@author: Mark
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import requests
from requests.auth import HTTPDigestAuth
import logging


IPS = ["192.168.100.101", "192.168.100.102",
       "192.168.100.103", "192.168.100.104",
       "192.168.100.105", "192.168.100.106"]


def on():
    payload = ""
    for counter in range(0, len(IPS)):
        payload += "M0:O%s=on&" % str(counter + 1)
        if counter == len(IPS) - 1:
            payload = payload[0:-1]
    r = requests.get("http://192.168.100.200/hidden.htm?" +
                     payload,
                     auth=HTTPDigestAuth("api", "api"))
    assert(r.status_code == 200)


def off():
    payload = ""
    for counter in range(0, len(IPS)):
        payload += "M0:O%s=off&" % str(counter + 1)
        if counter == len(IPS) - 1:
            payload = payload[0:-1]
    r = requests.get("http://192.168.100.200/hidden.htm?" +
                     payload,
             auth=HTTPDigestAuth("api", "api"))
    assert(r.status_code == 200)

if __name__ == '__main__':
    logging.basicConfig(filename="result.log",
                    format="%(asctime)s:%(levelname)s:%(message)s",
                    level=logging.DEBUG)
    logging.debug("TEST ==== Started Logging ====")
    runs = 0
    passes = 0
    fails = 0
    try:
        driver = webdriver.Firefox()
        wait = WebDriverWait(driver, 30)
        on()
        while True:
            pass_count = 0
            fail_count = 0
            runs += 1
            time.sleep(60 * 60 * 3)
            off()
            time.sleep(60 * 20)
            on()
            time.sleep(60)
            for ip in IPS:
                driver.get("http://" + ip)
                logo = By.CSS_SELECTOR, ".logotext2"
                text = wait.until(EC.presence_of_element_located(logo)).text
                assert(text == "System Configuration")
                head = By.CSS_SELECTOR, "#right > h1"
                h_text = wait.until(EC.presence_of_element_located(head)).text
                assert(h_text == "System Configuration")
                if (text == "System Configuration"
                    and h_text == "System Configuration"):
                    pass_count += 1
                else:
                    fail_count += 1
            if pass_count == len(IPS):
                passes += 1
            else:
                fails += 1
            logging.debug("TEST Execution: %d Passes: %d Fails: %d"
                        % (runs, passes, fails))
    finally:
        driver.quit()
