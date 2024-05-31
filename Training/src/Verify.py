import os

from stable_baselines3 import PPO

from TrackmaniaEnv import TrackmaniaEnv

env = TrackmaniaEnv()

# Define paths
logPath = os.path.join("../logs")
modelPath = os.path.join("../models")

model = PPO.load(modelPath, env)

obs, _ = env.reset()
done = False
score = 0

while not done:
	# model.env.render()
	action, _ = model.predict(obs)
	obs, reward, done, info, _ = env.step(action)
	score += reward
	print(obs)

print(f"Score: {score}")
