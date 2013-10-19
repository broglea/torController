'''
	torController.py
	Author: broglea

	A very simple and basic torController that uses telnet to the localhost to authenticate
	and get new identities

	PREREQUISITE TO USING THIS:
	1) You must edit your /etc/tor/torrc file to turn on ControlPort (default is 9051) 
	2) You must edit your /etc/tor/torrc with your HashedControlPassword you want to use,
       this can be obtained via the command 'tor --hash-password passwordGoesHere'

    usage:
    	from torController import torController
    	tor = torController(9051, "passwordGoesHere")
    	tor.connect()
    	tor.newIdentity()
'''

import telnetlib
import time

class torController(object):

	def __init__(self, PORT, PASS):
		self.port = PORT
		self.password = PASS
		self.tn = telnetlib.Telnet("127.0.0.1", self.port)		

	def connect(self):
		self.tn.write("authenticate " + '"' + self.password + '"\n')
		time.sleep(.5)
		status = self.tn.read_very_eager()
		if(status=="250 OK\r\n"):
			print("Authenticated to Tor Controller")
		else:
			raise Exception("Could not authenticate to Tor Controller: " + status)

	def newIdentity(self):
		self.tn.write("SIGNAL NEWNYM\n")
		status = self.tn.read_very_eager()
		if(status=="250 OK\r\n"):
			print("Successfully got a New Identity")
		else:
			raise Exception("Error while getting a New Identity: " + status)