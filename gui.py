from tkinter import *
from PIL import Image
from PIL import ImageTk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Horrors of Practical Submission")
        master.geometry("600x500")

        choices = 3
        var = IntVar()
        optionText = "haha"

        for f in range(0, choices):
            option = Radiobutton(master, text=optionText + str(f), variable=var, value = f)
            option.place(anchor = "n", relx = 0.5, y= 20 * f + 100)


        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(anchor = "n", relx =  0.5, rely = 0.95)
        

    def greet(self):
        print("Greetings!")






root = Tk()
gui = GUI(root)
root.mainloop()