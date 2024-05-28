import os
import subprocess
import zmq


class Connection:
	"""
	ZMQ server for receiving trackmania data
	"""

	def __init__(self):
		self.context = zmq.Context()
		self.socket = self.context.socket(zmq.REP)
		self.socket.bind("tcp://*:5555")
		subprocess.Popen(r"C:\Users\thijn\Documents\school\sem 4\individual\Server\Server\bin\Debug\net7.0\Server.exe")
