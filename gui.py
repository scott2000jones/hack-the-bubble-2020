from tkinter import *
import json
from tkinter.ttk import *
from PIL import Image, ImageTk


master = Tk()
master.title("Silence of the Labs")

frame = Frame(master, height=500, width=600)
frame.pack()

background = Image.open("imgs/bg.png")
background = background.resize((600,500))
background = ImageTk.PhotoImage(background)

background_label = Label(frame, image=background)
background_label.place(x=0,y=0,relwidth=1, relheight=1)

style = Style()
style.configure('TButton', font=('courier',14), foreground='black')
style.configure('TRadiobutton', font=('courier'), foreground='black')


f = open("data.json", "r")
datastring = f.read()
x = json.loads(datastring)
# print(x)

time = '8:30pm'
tkOldCurrentScene = StringVar(frame, "bedroom")
tkCurrentScene = StringVar(frame, "bedroom")
tkOldCurrentScene.set("bedroom")
tkCurrentScene.set("bedroom")
tkVarget = StringVar(frame, "")
print("currentscene starts as " + tkCurrentScene.get())
earnedItems = []


textframe = Frame(frame)
textframe.place(anchor = "n", relx = 0.5, rely = 0.4)
# optionframe = Frame(master)
# optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)

text = Text(textframe, wrap=WORD, width=80, height=10, bg='black', fg='#4FB346')
text.pack()


def selectOption(varget):
    tkVarget.set(varget)
    tkCurrentScene.set(x[tkOldCurrentScene.get()][varget]['newscene'])

def makeOptions(choices):

    optionframe = Frame(frame)
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

button = Image.open("imgs/button.png")
button = button.resize((100,20))
button = ImageTk.PhotoImage(button)

close_button = Button(frame, image=button, text="Close", compound=CENTER, command=master.quit)
close_button.place(anchor = "s", relx =  0.5, rely = 1, y = -10)

submit_button = Button(frame, image=button, text="Submit", compound=CENTER, command=changeScene)
submit_button.place(anchor = "s", relx =  0.5, rely = 0.9)

mainloop()
