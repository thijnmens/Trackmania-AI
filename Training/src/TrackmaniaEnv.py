import json
import random
import time
import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Box, Dict
from Connection import Connection
from pyvjoystick import vigem as vg

from src.VehicleData import VehicleData


class TrackmaniaEnv(Env):
	def __init__(self):
		self.action_space = Box(low=-1, high=1, shape=(3,))
		self.observation_space = Box(low=-999, high=999, shape=(8,))
		self.state = VehicleData().to_state()
		self.finished = False  # has AI crossed finish line
		self.connection = Connection()  # ZMQ connection
		self.controller = vg.VDS4Gamepad()
		self.timeSteps = 0
		self.timeLimit = 500

		# Respawn car
		self.controller.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()
		self.controller.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()

	def step(self, action):
		data = self.connection.socket.recv().decode()
		vehicle_data = json.loads(data, object_hook=lambda p: VehicleData(**p))

		# Update state
		self.state = vehicle_data.to_state()
		self.timeSteps += 1

		# Calculate reward
		reward = vehicle_data.calculate_reward()

		# Emulate DualShock 4 controller
		self.emulate_input(action)

		# Perform action
		self.connection.socket.send_string('')

		# Check if no actions left
		done = self.timeSteps > self.timeLimit

		time.sleep(0.005)

		return self.state, reward, done, {}, {}

	def emulate_input(self, action):
		self.controller.right_trigger_float(action[0])
		self.controller.left_trigger_float(action[1])
		self.controller.left_joystick(int(action[2] * 255), 0)
		self.controller.update()

	def render(self):
		# No need for rendering
		pass

	def reset(self, **kwargs):
		# Reset environment
		super().reset(seed=kwargs.get('seed'))
		self.state = VehicleData().to_state()
		self.finished = False
		self.timeSteps = 0

		# Reset car
		self.controller.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()
		self.controller.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()
		return self.state, {}
