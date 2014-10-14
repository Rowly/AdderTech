'''
Created on 30 Apr 2013

@author: Mark.rowlands
'''
import telnetlib
import time

class TelnetService():

    def __init__(self, server, port):
        self.server = server.replace("http://", "")
        self.port = port
        self.telnet = telnetlib.Telnet(self.server, self.port)

    def login_to_unit(self):
        self.telnet.read_until(b"login: ")
        self.telnet.write(b"root\n")
        self.telnet.read_until(b"Password: ")
        self.telnet.write(b"dvix\n")

    def get_response_from_command(self, command):
        self.login_to_unit()
        time.sleep(2)
        self.telnet.write(command)
        time.sleep(0.2)
        self.telnet.write(b"exit\n")
        telnet_response = str(self.telnet.read_all())
        return telnet_response