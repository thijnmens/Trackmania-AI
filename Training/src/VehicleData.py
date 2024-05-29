class VehicleData:
	def __init__(
			self,
			speed: float = 0,
			acceleration: float = 0,
			inputLeft: float = 0,
			inputRight: float = 0,
			inputForward: float = 0,
			inputBackwards: float = 0,
			gear: int = 0,
			rpm: float = 0
		):
		self.speed: float = speed
		self.acceleration: float = acceleration
		self.inputLeft: float = inputLeft
		self.inputRight: float = inputRight
		self.inputForward: float = inputForward
		self.inputBackwards: float = inputBackwards
		self.gear: int = gear
		self.rpm: float = rpm

	def to_state(self) -> [float]:
		return [self.speed, self.acceleration, self.inputLeft, self.inputRight, self.inputForward, self.inputBackwards, float(self.gear), self.rpm]

	def calculate_reward(self) -> float:
		speed_rew = self.speed
		accel_rew = self.acceleration * self.speed
		return (speed_rew + accel_rew) / 1000
