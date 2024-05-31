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
			location: list[float] = [0, 0, 0]
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
		self.location: list[float] = location

	def to_state(self) -> [float]:
		return [self.speed, self.acceleration, self.inputLeft, self.inputRight, self.inputForward, self.inputBackwards, float(self.gear), self.rpm]

	def calculate_reward(self) -> float:
		speed_rew = self.speed
		accel_rew = self.acceleration * self.speed
		return (speed_rew + accel_rew) / self.TIME_LIMIT
