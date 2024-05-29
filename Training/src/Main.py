import datetime
import os
import time

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from src.TrackmaniaEnv import TrackmaniaEnv
import numpy as np

env = TrackmaniaEnv()
logPath = os.path.join("./logs")

iterations_per_gen = 10
generations = 100

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logPath)


generation = 0
while generation <= generations:
    generation += 1
    modelPath = os.path.join("./models", f"{datetime.date.today()}.{generation}.zip")
    model.learn(6144, progress_bar=True)
    model.save(modelPath)
