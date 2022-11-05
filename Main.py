from tkinter import *
from QuintenChoice import *
master = Tk()

def start():
    master.destroy()
    configureSong()

def blueText(x, y, size, content):
    w.create_text(x, y, text=content, fill="#071330", font=('Arial '+str(size)+' bold'))

welcomeContent0 = "Welcome!"
welcomeContent1 = "With this system, you can easily create your own songs without any experience!"
welcomeContent2 = "It is simple and easy to use - and you still have a variety of options to choose from."
welcomeContent3 = "Click on the button below to get started!"

w = Canvas(master, width=1500, height=1000, bg="#c3ceda")
w.place(relx=0.5, rely=0.5, anchor=CENTER)
w.pack(side=TOP)

w.create_rectangle(250, 100, 1250, 700, fill="#0c4160")
w.create_rectangle(260, 110, 1240, 690, fill="#738fa7")

blueText(750, 50, 37, "Music Mixer")
blueText(750, 160, 27, welcomeContent0)
blueText(750, 230, 18, welcomeContent1)
blueText(750, 280, 18, welcomeContent2)
blueText(750, 340, 18, welcomeContent3)
w.pack()

continueButton = Button(w, text="Let's go!", font=("Arial 43 bold"), command=start, anchor=CENTER)
continueButton.configure(width=9, height=2, background="#c3ceda",activebackground="#0c4160", relief=FLAT)
continueButton_window = w.create_window(750, 420, anchor=N, window=continueButton)

w.mainloop()