import datetime
import os
import subprocess
from tersel import Tersel
from stable_baselines3 import PPO
from TrackmaniaEnv import TrackmaniaEnv

env = TrackmaniaEnv()
logPath = os.path.join("./logs")

iterations_per_gen = 10
generations = 100

load = True if Tersel("Do you wish to load a model?", [
    "Yes please!",
    "No thanks"
]).show()[0] == 0 else False
if load:
    options = os.listdir(os.path.join("./models"))
    model_path = options[Tersel("Choose which model to load", options).show()[0]]
    model = PPO.load(os.path.join("./models", model_path), env, verbose=0, tensorboard_log=logPath)
else:
    model = PPO('MlpPolicy', env, verbose=0, tensorboard_log=logPath)

subprocess.Popen(r"C:\Users\thijn\Documents\school\sem 4\individual\Server\Server\bin\Debug\net7.0\Server.exe")

generation = 0
while generation <= generations:
    generation += 1
    modelPath = os.path.join("./models", f"{datetime.date.today()}.{generation}.zip")
    model.learn(iterations_per_gen * TrackmaniaEnv.TIME_LIMIT, progress_bar=True)
    model.save(modelPath)
