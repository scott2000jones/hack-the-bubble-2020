import json
from types import SimpleNamespace

# Get JSON and put it in an object
f = open("data.json", "r")
datastring = f.read()
x = json.loads(datastring)

# Set up state for the initial scene
time = '8:30pm'
currentScene = 'bedroom'
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



print("showing the title now oooooooo")
print("-----------------------------------------")
print("SILENCE OF THE LABS")
print("-----------------------------------------")
print("wow so cool (says everyone)\n\n")

print("ok time to play the game")

while(True):
    print("\n\n\nnew option")
    print(x['scene'][currentScene]['prompt'])
    for option in x['scene'][currentScene]:
        if(option != "prompt"):
            print(option)
    parsecmd(input("Which option do you choose? (Enter the number) "))
