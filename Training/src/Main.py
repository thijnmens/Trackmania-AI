import os
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from src.TrackmaniaEnv import TrackmaniaEnv
import numpy as np

env = TrackmaniaEnv()
env.reward_range = (-np.inf, 10)
logPath = os.path.join("../logs")
modelPath = os.path.join("../models")

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logPath)
model.learn(10000)
model.save(modelPath)

print(evaluate_policy(model, env, render=True, n_eval_episodes=5))
