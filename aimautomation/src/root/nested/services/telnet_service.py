'''
Created on 30 Apr 2013

@author: Mark.rowlands
'''
import telnetlib


class TelnetService():

    def __init__(self, host, port):
        self.host = host.replace("http://", "")
        self.port = port
        self.telnet = telnetlib.Telnet(self.host, self.port)

    def login_to_unit(self):
        self.telnet.read_until(b"login: ")
        self.telnet.write(b"root\n")
        self.telnet.read_until(b"Password: ")
        self.telnet.write(b"dvix\n")

    def get_response_from_command(self, command):
        self.login_to_unit()
        self.telnet.read_until(b"$")
        self.telnet.write(command)
        return str(self.telnet.read_all())

if __name__ == '__main__':
    host = input("Enter Host address: ")
    test = TelnetService(host, 23)
    output = test.get_response_from_command(b"ifconfig; exit\n")
    print(output)
    assert(host in output)
