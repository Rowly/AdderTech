'''
Created on 2 Sep 2014

@author: Mark
'''
import subprocess
from collections import OrderedDict

version = "v3.3.30326"
rx2  = {"d_ip":"192.168.1.31"}
rx2s = {"d_ip":"192.168.1.30"}
tx2  = {"d_ip":"169.254.1.33"}
tx2b = {"d_ip":"192.168.1.21"}
tx2v = {"d_ip":"192.168.1.22"}
tx2s = {"d_ip":"192.168.1.20"}

# devices = OrderedDict((("RX2",rx2), 
#                        ("TX2",tx2), 
#                        ("TX2b",tx2b), 
#                        ("TX2v",tx2v), 
#                        ("RX2s",rx2s), 
#                        ("TX2s",tx2s)))
devices = OrderedDict((("RX2",rx2),
                       ("RX2s",rx2s),
                       ("TX2b",tx2b),
                       ("TX2s",tx2s)))

if __name__ == '__main__':
    for device in devices:
        subprocess.call("regression_suite.py %s %s %s" %(device, version, devices[device].get("d_ip")), shell=True)