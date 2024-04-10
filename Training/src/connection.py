import os
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
	message = socket.recv()

	print(f'Received message: {message}')

	socket.send_string('')
