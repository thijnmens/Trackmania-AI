import random

import numpy as np
from gymnasium import Env
from gymnasium.spaces import Discrete, Box, Dict


class TrackmaniaEnv(Env):
	def __init__(self):
		self.action_space = Dict({
			'steering': Box(low=-100, high=100, shape=(1,)),
			'throttle': Box(low=-100, high=100, shape=(1,)),
			'brake': Discrete(1)
		});
		self.observation_space = Dict({
			'AirBrakeNormed': Box(low=-1, high=1, shape=(1,)),
			'BulletTimeNormed': Box(low=-1, high=1, shape=(1,)),
			'CurGear': Box(low=-1, high=1, shape=(1,)),
			'Dir': Box(low=-1, high=1, shape=(1,)),
			'DiscontinuityCount': Box(low=-1, high=1, shape=(1,)),
			'EngineOn': Box(low=-1, high=1, shape=(1,)),
			'FLBreakNormedCoef': Box(low=-1, high=1, shape=(1,)),
			'FLDamperLen': Box(low=-1, high=1, shape=(1,)),
			'FLIcing01': Box(low=-1, high=1, shape=(1,)),
			'FLSlipCoef': Box(low=-1, high=1, shape=(1,)),
			'FLSteerAngle': Box(low=-1, high=1, shape=(1,)),
			'FLTireWear01': Box(low=-1, high=1, shape=(1,)),
			'FLWheelRot': Box(low=-1, high=1, shape=(1,)),
			'FLWheelRotSpeed': Box(low=-1, high=1, shape=(1,)),
			'FRBreakNormedCoef': Box(low=-1, high=1, shape=(1,)),
			'FRDamperLen': Box(low=-1, high=1, shape=(1,)),
			'FRIcing01': Box(low=-1, high=1, shape=(1,)),
			'FRSlipCoef': Box(low=-1, high=1, shape=(1,)),
			'FRSteerAngle': Box(low=-1, high=1, shape=(1,)),
			'FRTireWear01': Box(low=-1, high=1, shape=(1,)),
			'FRWheelRot': Box(low=-1, high=1, shape=(1,)),
			'FRWheelRotSpeed': Box(low=-1, high=1, shape=(1,)),
			'FrontSpeed': Box(low=-1, high=1, shape=(1,)),
			'GroundDist': Box(low=-1, high=1, shape=(1,)),
			'InputBrakePedal': Box(low=-1, high=1, shape=(1,)),
			'InputGasPedal': Box(low=-1, high=1, shape=(1,)),
			'InputIsBraking': Box(low=-1, high=1, shape=(1,)),
			'InputSteer': Box(low=-1, high=1, shape=(1,)),
			'InputVertical': Box(low=-1, high=1, shape=(1,)),
			'IsGroundContact': Box(low=-1, high=1, shape=(1,)),
			'IsReactorGroundMode': Box(low=-1, high=1, shape=(1,)),
			'IsTopContact': Box(low=-1, high=1, shape=(1,)),
			'IsTurbo': Box(low=-1, high=1, shape=(1,)),
			'IsWheelsBurning': Box(low=-1, high=1, shape=(1,)),
			'Left': Box(low=-1, high=1, shape=(1,)),
			'Position': Box(low=-1, high=1, shape=(1,)),
			'RLBreakNormedCoef': Box(low=-1, high=1, shape=(1,)),
			'RLDamperLen': Box(low=-1, high=1, shape=(1,)),
			'RLIcing01': Box(low=-1, high=1, shape=(1,)),
			'RLSlipCoef': Box(low=-1, high=1, shape=(1,)),
			'RLSteerAngle': Box(low=-1, high=1, shape=(1,)),
			'RLTireWear01': Box(low=-1, high=1, shape=(1,)),
			'RLWheelRot': Box(low=-1, high=1, shape=(1,)),
			'RLWheelRotSpeed': Box(low=-1, high=1, shape=(1,)),
			'RRBreakNormedCoef': Box(low=-1, high=1, shape=(1,)),
			'RRDamperLen': Box(low=-1, high=1, shape=(1,)),
			'RRIcing01': Box(low=-1, high=1, shape=(1,)),
			'RRSlipCoef': Box(low=-1, high=1, shape=(1,)),
			'RRSteerAngle': Box(low=-1, high=1, shape=(1,)),
			'RRTireWear01': Box(low=-1, high=1, shape=(1,)),
			'RRWheelRot': Box(low=-1, high=1, shape=(1,)),
			'RRWheelRotSpeed': Box(low=-1, high=1, shape=(1,)),
			'RaceStartTime': Box(low=-1, high=1, shape=(1,)),
			'ReactorAirControl': Box(low=-1, high=1, shape=(1,)),
			'ReactorInputsX': Box(low=-1, high=1, shape=(1,)),
			'SimulationTimeCoef': Box(low=-1, high=1, shape=(1,)),
			'SpoilerOpenNormed': Box(low=-1, high=1, shape=(1,)),
			'TurboTime': Box(low=-1, high=1, shape=(1,)),
			'Up': Box(low=-1, high=1, shape=(1,)),
			'WaterImmersionCoef': Box(low=-1, high=1, shape=(1,)),
			'WaterOverDistNormed': Box(low=-1, high=1, shape=(1,)),
			'WaterOverSurfacePos': Box(low=-1, high=1, shape=(1,)),
			'WetnessValue01': Box(low=-1, high=1, shape=(1,)),
			'WingsOpenNormed': Box(low=-1, high=1, shape=(1,)),
			'WorldCarUp': Box(low=-1, high=1, shape=(1,)),
			'WorldVel': Box(low=-1, high=1, shape=(1,))
		})
		self.state = {}

	def step(self, action):

		reward = 0
		done = False

		return self.state, reward, done, {}, {}

	def render(self):
		# No need for rendering
		pass

	def reset(self, **kwargs):

		# Reset environment
		super().reset(seed=kwargs.get('seed'))
		self.state = {}
		return self.state, {}
