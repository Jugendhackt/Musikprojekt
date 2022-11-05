from tkinter import *
master = Tk()

welcomeContent0 = "Welcome!"
welcomeContent1 = "With this system, you can easily create your own songs without any experience!"
welcomeContent2 = "It is simple and easy to use - but of course you still have a ton of options!"
welcomeContent3 = "Click on the button below to get started!"

w = Canvas(master, width=1500, height=1000, bg="#c3ceda")
w.place(relx=0.5, rely=0.5, anchor=CENTER)
w.pack(side=TOP)

w.create_rectangle(250, 100, 1250, 700, fill="#0c4160")
w.create_rectangle(260, 110, 1240, 690, fill="#738fa7")

w.create_text(750, 50, text="System7000", fill="black", font=('Arial 37 bold'), )
w.create_text(750, 150, text=welcomeContent0, fill="black", font=('Arial 27 bold'), )
w.create_text(750, 200, text=welcomeContent1, fill="black", font=('Arial 18 bold'), )
w.create_text(750, 250, text=welcomeContent2, fill="black", font=('Arial 18 bold'), )
w.create_text(750, 300, text=welcomeContent3, fill="black", font=('Arial 18 bold'), )
w.pack()


w.mainloop()
