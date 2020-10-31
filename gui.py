from tkinter import *
import json

master = Tk()


f = open("data.json", "r")
datastring = f.read()
x = json.loads(datastring)
# print(x)

time = '8:30pm'
tkOldCurrentScene = StringVar(master, "bedroom")
tkCurrentScene = StringVar(master, "bedroom")
tkOldCurrentScene.set("bedroom")
tkCurrentScene.set("bedroom")
print("currentscene starts as " + tkCurrentScene.get())
hasMatric = False

master.title("Silence of the Labs")
master.geometry("600x500")
textframe = Frame(master)
textframe.place(anchor = "n", relx = 0.5, rely = 0.4)
optionframe = Frame(master)
optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)

def makePrompt(prompt):
    textframe = Frame(master)
    textframe.place(anchor = "n", relx = 0.5, rely = 0.4)

    text = Label(textframe, text=prompt)
    text.pack()

def selectOption(varget):
    # print("_------------------------------")
    # print("previous value of currentScene " + tkCurrentScene.get())
    # print("previous value of OLDcurrentScene \n" + tkOldCurrentScene.get())
    # print("changing value of currentScene to ")
    # print(x[tkCurrentScene.get()][varget]['newscene'])
    # print("changing value of OLDcurrentScene to\n" + tkCurrentScene.get())
    # print("_------------------------------\n\n\n\n\n")

    tkCurrentScene.set(x[tkOldCurrentScene.get()][varget]['newscene'])

def makeOptions(choices):
    optionframe = Frame(master)
    optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)
    var = StringVar()
    for choice in choices:
        print(choice)
        if (choice != "prompt"):
            # option = Radiobutton(optionframe, text=choice, variable=var, value=choice, command=(lambda : tkCurrentScene.set(x[tkCurrentScene.get()][var.get()]['newscene'])))
            option = Radiobutton(optionframe, text=choice, variable=var, value=choice, command=(lambda : selectOption(var.get())))
            option.pack()

def changeScene():
    tkOldCurrentScene.set(tkCurrentScene.get())
    makeOptions(x[tkCurrentScene.get()])
    print("now in " + tkCurrentScene.get() + ", previously was in " + tkOldCurrentScene.get())

makeOptions(x[tkCurrentScene.get()])

close_button = Button(master, text="Close", command=master.quit)
close_button.place(anchor = "s", relx =  0.5, rely = 1)

submit_button = Button(master, text="Submit", command=changeScene)
submit_button.place(anchor = "s", relx =  0.5, rely = 0.9)

makePrompt("Hello")



mainloop()
