import random
import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Box


class ShowerEnv(Env):
	def __init__(self):
		self.action_space = Discrete(4)  # Down, Nothing, Up, End
		self.observation_space = Box(low=0, high=100, shape=(1,))  # Shower temperature, between 0 and 100
		self.state = random.randint(35, 41)  # Starting temperature
		self.timeLimit = 200  # Amount of actions

	def step(self, action):
		# End
		if action == 3:
			if 37 <= self.state <= 39:
				reward = self.timeLimit + 10
				# print(f"reward: {reward}")
			else:
				reward = self.timeLimit * -1
				# print(f"Pain: {self.state}")
			return self.state, reward, True, {}, {}

		self.state += action - 1
		self.timeLimit -= 1

		# Calculate reward
		if 37 <= self.state <= 39:
			reward = 0
		else:
			reward = -1

		# Check if no actions left
		if self.timeLimit <= 0:
			done = True
			reward -= 10
		else:
			done = False

		return self.state, reward, done, {}, {}

	def render(self):
		# No need for rendering
		pass

	def reset(self, **kwargs):

		# Reset environment
		super().reset(seed=kwargs.get('seed'))
		self.state = np.array([random.randint(35, 41)]).astype(float)
		self.timeLimit = 200
		return self.state, {}
