import re
from Raycasting import Raycasting


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

	def to_state(self) -> list[float]:
		front_location = [
			self.location[0] + self.direction[0],
			self.location[1],  # Y doesn't change for now
			self.location[2] + self.direction[2],
		]

		rays = self.raycaster.get_distance(self.location, front_location)
		length = len(rays)
		return [
			[self.speed] * length,
			[self.acceleration] * length,
			[self.inputLeft] * length,
			[self.inputRight] * length,
			[self.inputForward] * length,
			[self.inputBackwards] * length,
			[float(self.gear)] * length,
			[self.rpm] * length,
			rays
		]

	def calculate_reward(self) -> float:
		speed_rew = self.speed
		accel_rew = self.acceleration * self.speed
		return (speed_rew + accel_rew) / self.TIME_LIMIT
