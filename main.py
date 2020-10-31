import json
from types import SimpleNamespace

# Get JSON and put it in an object
f = open("data.json", "r")
datastring = f.read()
x = json.loads(datastring)

# Set up state for the initial scene
time = '8:30pm'
currentScene = 'dra'
hasMatric = False

# Parse a user's choice and update the state
def parsecmd(cmd):
    try:
        cmd = int(cmd)
    except ValueError:
        return False

    # Replace this with stuff to update the state
    print(cmd)
    print(x['scene'][currentScene][str(cmd)])

print("spooky time")
parsecmd(1)
