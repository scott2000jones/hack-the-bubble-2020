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
tkVarget = StringVar(master, "")
print("currentscene starts as " + tkCurrentScene.get())
earnedItems = []

master.title("Silence of the Labs")
master.geometry("600x500")
textframe = Frame(master)
textframe.place(anchor = "n", relx = 0.5, rely = 0.4)
# optionframe = Frame(master)
# optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)

text = Text(master, wrap=WORD, width=80, height=10)
text.pack()


def selectOption(varget):
    tkVarget.set(varget)
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
    for item in x[tkOldCurrentScene.get()][tkVarget.get()]['earned']:
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>" + item)
        earnedItems.append(item)

    tkOldCurrentScene.set(tkCurrentScene.get())

    makePrompt(x[tkCurrentScene.get()]['prompt'])
    makeOptions(x[tkCurrentScene.get()])
    print("now in " + tkCurrentScene.get() + ", previously was in " + tkOldCurrentScene.get())

def makePrompt(prompt):
    # textframe = Frame(master)
    # textframe.place(anchor = "n", relx = 0.5, rely = 0.4)
    text.config(state=NORMAL)
    text.delete('1.0', END)
    text.insert(END, prompt)
    text.config(state=DISABLED)


makePrompt(x[tkCurrentScene.get()]['prompt'])
makeOptions(x[tkCurrentScene.get()])

close_button = Button(master, text="Close", command=master.quit)
close_button.place(anchor = "s", relx =  0.5, rely = 1)

submit_button = Button(master, text="Submit", command=changeScene)
submit_button.place(anchor = "s", relx =  0.5, rely = 0.9)

mainloop()
