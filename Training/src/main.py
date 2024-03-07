import os
from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from ShowerEnv import ShowerEnv

# Setup environment
env = ShowerEnv()

# Define paths
logPath = os.path.join("../logs")
modelPath = os.path.join("../models")

# Load previous of create new
if input("Load?: [y/n]").lower() == 'y':
	model = PPO.load(modelPath, env)
else:
	model = PPO("MlpPolicy", env, verbose=1, tensorboard_log=logPath)

# Train and save
model.learn(100000)
model.save(modelPath)

# Print final AI score
print(evaluate_policy(model, env, render=True))
