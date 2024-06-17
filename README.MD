# Trackmania AI

### How to use

#### Installing the plugin
- Install [OpenPlanet](https://openplanet.dev)
- Set OpenPlanet to Development mode (!!!YOU NEED A TRACKMANIA SUBSCRIPTION FOR THIS!!!)
- Enable the plugin

You will know the plugin is properly working if the game starts to freeze and run at around 0.3fps

#### Installing the AI
- Install [Python 3.10](https://www.python.org/downloads/release/python-31014/)
- Enable the venv by running the `activate` file using `./Training/venv/Scripts/activate`
- Install all dependencies using `pip install -r requirements.txt`
- run the program openings the `/Scripts/teach.bat` file

### How to teach the AI
The AI will automatically start learning when you run the program. You can resume a learning session by loading the previous model.

### How to run the AI without training
You can follow the same installation steps, but you should open the `/Scripts/run.bat` file instead