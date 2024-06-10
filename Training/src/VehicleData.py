import re
from Raycasting import Raycasting
import numpy as np


class VehicleData:
	def __init__(
			self,
			TIME_LIMIT: int = 0,
			speed: float = 0,
			acceleration: float = 0,
			inputLeft: float = 0,
			inputRight: float = 0,
			inputForward: float = 0,
			inputBackwards: float = 0,
			gear: int = 0,
			rpm: float = 0,
			location: str = "<0, 0, 0>",
			direction: str = "<0, 0, 0>",
			raycaster: Raycasting = Raycasting(r"C:\Users\thijn\Downloads\Showcase.obj")
		):
		self.TIME_LIMIT = TIME_LIMIT
		self.speed: float = speed
		self.acceleration: float = acceleration
		self.inputLeft: float = inputLeft
		self.inputRight: float = inputRight
		self.inputForward: float = inputForward
		self.inputBackwards: float = inputBackwards
		self.gear: int = gear
		self.rpm: float = rpm
		self.location: list[float] = [float(s) for s in re.findall(r'-?\d+\.?\d*', location)]
		self.direction: list[float] = [float(s) for s in re.findall(r'-?\d+\.?\d*', direction)]
		self.raycaster: Raycasting = raycaster
		self.rays = [999] * 180

	def to_state(self):
		front_location = [
			self.location[0] + (self.direction[0] * 15),
			10.457,  # Y doesn't change for now
			self.location[2] + (self.direction[2] * 15),
		]

		# self.raycaster.get_image(self.location, front_location)
		self.rays = self.raycaster.get_distance(self.location, front_location)
		return np.concatenate((
			[
				self.speed,
				self.acceleration,
				self.inputLeft,
				self.inputRight,
				self.inputForward,
				self.inputBackwards,
				float(self.gear),
				self.rpm
			],
			self.rays
		))

	def calculate_reward(self) -> float:
		speed_rew = self.speed ** 2
		accel_rew = self.acceleration
		gear_rew = self.gear
		crash_pen = False
		for i, distance in enumerate(self.rays):
			if distance <= 3:
				crash_pen = True
		return ((speed_rew + accel_rew) * gear_rew) * (0 if crash_pen else 1) / 1000
