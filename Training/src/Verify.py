import os
import subprocess

from stable_baselines3 import PPO

from TrackmaniaEnv import TrackmaniaEnv

env = TrackmaniaEnv()

# Define paths
logPath = os.path.join("../logs")
modelPath = os.path.join("C:\\Users\\thijn\\Documents\\school\\sem 4\\individual\\Training\\src\\models\\2024-06-13.4.zip")

model = PPO.load(modelPath, env)

subprocess.Popen(r"C:\Users\thijn\Documents\school\sem 4\individual\Server\Server\bin\Debug\net7.0\Server.exe")

while True:
	obs, _ = env.reset()
	done = False
	score = 0

	while not done:
		# model.env.render()
		action, _ = model.predict(obs)
		obs, reward, done, info, _ = env.step(action)
		score += reward
		print(reward)

	print(score)
