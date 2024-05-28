import json
import random
import time
import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Box, Dict
from Connection import Connection
from pyvjoystick import vigem as vg


class TrackmaniaEnv(Env):
	def __init__(self):
		self.action_space = Box(low=-1, high=1, shape=(3,))
		self.observation_space = Box(low=-999, high=999, shape=(1,))  # Speed
		self.state = Box(low=-999, high=999, shape=(1,))
		self.finished = False  # has AI crossed finish line
		self.connection = Connection()  # ZMQ connection
		self.controller = vg.VDS4Gamepad()
		self.timeSteps = 0
		self.timeLimit = 100

		# Respawn car
		self.controller.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()
		self.controller.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()

	def step(self, action):
		data = self.connection.socket.recv().decode()
		self.timeSteps += 1

		# Calculate reward
		reward = self.calculate_reward(json.loads(data))

		# Emulate DualShock 4 controller
		self.emulate_input(action)

		# Perform action
		self.connection.socket.send_string('')

		time.sleep(0.05)
		print(reward)

		# Check if no actions left
		done = self.timeSteps > self.timeLimit
		return self.state, reward, done, {}, {}

	def calculate_reward(self, data):
		speedReward = data['FrontSpeed']
		return speedReward

	def emulate_input(self, action):
		self.controller.right_trigger_float(action[0])
		self.controller.left_trigger_float(action[1])
		self.controller.left_joystick(int(action[2] * 255), 0)
		self.controller.update()

		print(f"gas: {action[0]}, brake: {action[1]}, steering: {action[2]}")

	def render(self):
		# No need for rendering
		pass

	def reset(self, **kwargs):
		# Reset environment
		super().reset(seed=kwargs.get('seed'))
		self.state = np.array([0]).astype(np.float32)
		self.finished = False
		self.timeSteps = 0

		# Reset car
		self.controller.press_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()
		self.controller.release_button(vg.DS4_BUTTONS.DS4_BUTTON_CIRCLE)
		self.controller.update()
		return self.state, {}
