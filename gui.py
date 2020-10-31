from tkinter import *
import json

# class GUI:
#
#     def __init__(self, master):
#         self.master = master
#         master.title("Silence of the Labs")
#         master.geometry("600x500")
#
#         textframe = Frame(master)
#         textframe.place(anchor = "n", relx = 0.5, rely = 0.2)
#
#         optionframe = Frame(master)
#         optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)
#
#         f = open("data.json", "r")
#         datastring = f.read()
#         x = json.loads(datastring)
#         print(x)
#
#         time = '8:30pm'
#         currentScene = 'bedroom'
#         hasMatric = False
#
#         self.makeOptions(x['scene'][currentScene], optionframe)
#
#         close_button = Button(master, text="Close", command=master.quit)
#         close_button.place(anchor = "s", relx =  0.5, rely = 1)
#
#         submit_button = Button(master, text="Submit", command=self.greet)
#         submit_button.place(anchor = "s", relx =  0.5, rely = 0.9)
#
#     def greet(self, x):
#         self.makeOptions(x['scene']['Run'])
#         print("Greetings!")
#
#     def makeOptions(self, choices, optionframe):
#         var = StringVar()
#         for choice in choices:
#             if (choice != "prompt"):
#                 option = Radiobutton(optionframe, text=choice, variable=var, value=choice[1])
#                 option.pack()


f = open("data.json", "r")
datastring = f.read()
x = json.loads(datastring)
print(x)

master = Tk()
master.title("Silence of the Labs")
master.geometry("600x500")
textframe = Frame(master)
textframe.place(anchor = "n", relx = 0.5, rely = 0.2)
optionframe = Frame(master)
optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)

def makeOptions(choices):
    optionframe = Frame(master)
    optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)
    var = StringVar()
    for choice in choices:
        if (choice != "prompt"):
            option = Radiobutton(optionframe, text=choice, variable=var, value=choice[1])
            option.pack()

def greet():
    # CHANGE THIS
    makeOptions(x['run'])
    print("Greetings!")

time = '8:30pm'
currentScene = 'bedroom'
hasMatric = False

makeOptions(x[currentScene])

close_button = Button(master, text="Close", command=master.quit)
close_button.place(anchor = "s", relx =  0.5, rely = 1)

submit_button = Button(master, text="Submit", command=greet)
submit_button.place(anchor = "s", relx =  0.5, rely = 0.9)


mainloop()
