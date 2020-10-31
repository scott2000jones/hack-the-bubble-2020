from tkinter import *

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Horrors of Practical Submission")
        master.geometry("600x500")

        textframe = Frame(master)
        textframe.place(anchor = "n", relx = 0.5, rely = 0.2)

        optionframe = Frame(master)
        optionframe.place(anchor = "s", relx = 0.5, rely = 0.8)

        choices = [["choice 1", "this is where it goes"], ["this is a choice", "it goes here"], ["whoo another choice", "and it goes here"], ["ouioui baguette", "yummy"]]
        self.makeOptions(choices, optionframe)


        close_button = Button(master, text="Close", command=master.quit)
        close_button.place(anchor = "s", relx =  0.5, rely = 1)
        

    def greet(self):
        print("Greetings!")

    def makeOptions(self, choices, optionframe):
        var = StringVar()

        for choice in choices:
            option = Radiobutton(optionframe, text=choice[0], variable=var, value=choice[1])
            option.pack()


root = Tk()
gui = GUI(root)
root.mainloop()
