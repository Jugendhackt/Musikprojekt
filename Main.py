
from tkinter import *
from QuintenChoice import *
from math import sin, cos
from ColorSchema import *
from RectangleFunction import *

if __name__ == "__main__":
    master = Tk()

    def start():
        master.destroy()
        configureSong()

    def blueText(x, y, size, content):
        w.create_text(x, y, text=content, fill=secondaryColor, font=('Arial '+str(size)+' bold'))

    welcomeContent0 = "Welcome!"
    welcomeContent1 = "With this system, you can easily create your own songs without any experience!"
    welcomeContent2 = "It is simple and easy to use - and you still have a variety of options to choose from."
    welcomeContent3 = "Click on the button below to get started!"

    w = Canvas(master, width=1500, height=780, bg=primaryColor)
    w.place(relx=0.5, rely=0.5, anchor=CENTER)
    w.pack(side=TOP)

    create_good_rectangle(w, 150, 100, 1350, 700, 40, 8, primaryAccent)
    create_good_rectangle(w, 160, 110, 1340, 690, 40, 8, secondaryAccent)

    blueText(750, 50, 45, "Music Mixer")
    blueText(750, 160, 33, welcomeContent0)
    blueText(750, 230, 22, welcomeContent1)
    blueText(750, 280, 22, welcomeContent2)
    blueText(750, 340, 22, welcomeContent3)
    w.pack()

    continueButton = Button(w, text="Let's go",fg=secondaryColor, font=("Arial 39 bold"), command=start, anchor=CENTER)
    continueButton.configure(width=8, height=2, background=primaryColor, activebackground=primaryAccent, relief=GROOVE)
    continueButton_window = w.create_window(750, 440, anchor=N, window=continueButton)


    mainloop()