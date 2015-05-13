'''
Created on 2 Sep 2014

@author: Mark
'''
import subprocess


version = "v3.3.30326"

devices = {"RX2": "192.168.1.31",
           "TX2": "169.254.1.33",
           "TX2b": "192.168.1.21",
           "TX2v": "192.168.1.22",
           "RX2s": "192.168.1.30",
           "TX2s": "192.168.1.20"}

if __name__ == '__main__':
    for device in devices:
        subprocess.call("regression_suite.py %s %s %s"
                        % (device, version, devices[device]), shell=True)
