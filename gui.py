from tkinter import *
from PIL import Image
from PIL import ImageTk

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("The Horrors of Practical Submission")
        master.geometry("600x500")
        
        '''
        background = Image.open("imgs/bg.jpg")
        background = background.resize((20,20))
        background = ImageTk.PhotoImage(background)

        self.background_label = Label(master, image=background)
        self.background_label.pack()
        '''

        
        
        self.frame = Frame(master, bg="Red")
        self.frame.pack()

        self.label = Label(self.frame, text="This is a GUI!")
        self.label.pack()

        self.entry = Entry(self.frame, fg="yellow", bg="blue", width="50")
        self.entry.pack()

        self.greet_button = Button(self.frame, text="Greet", bg="yellow", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(self.frame, text="Close", command=master.quit)
        self.close_button.pack()
        

    def greet(self):
        print("Greetings!")






root = Tk()
gui = GUI(root)
root.mainloop()