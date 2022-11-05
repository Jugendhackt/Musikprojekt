from tkinter import *

def configureSong():
    
    chosenTone = 0
    chosenDrum = 0
    chosenSpeed = 0
    myFont = ("Arial 15")

    def chooseTone(tone):
        chosenTone = tone
        print("Verstorben")

        
    def chooseDrum(drum):
        chosenDrum = drum

    def chooseSpeed(speed):
        chosenSpeed =speed

    def playTrack(tone, drums, speed):
        print("Song wird abgespielt")
        #Song aus Parametern abspielen
    def stopTrack():
        print("Song angehalten")
        #Song anhalten

    win = Tk()
    win.geometry("1500x1000")

    canvas = Canvas(win, bg="#c3ceda", height = "1000", width = "1500")

    canvas.create_rectangle(250,100,1250,700, fill = "#738fa7")
    canvas.pack()

    canvas.create_text(750, 40, text ="Configure Your SONG", fill="black", font=("Arial 37 bold"))
    canvas.create_text(500, 170, text ="Quintenzirkel", fill="black", font=("Arial 20 bold"))

    chosenText = Label(text = "Hello mf", font = myFont)
    chosenText_window = canvas.create_window(500, 350, window = chosenText, anchor = CENTER)
    



    buttonC = Button(win, text = "C", font=myFont, command = chooseTone("C"), anchor = CENTER)
    buttonC.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonC_window = canvas.create_window(500, 200, anchor=N, window=buttonC)

    buttonG = Button(win, text = "G", font=myFont, command = chooseTone("G"), anchor = CENTER)
    buttonG.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonG_window = canvas.create_window(570, 230, anchor=N, window=buttonG)

    buttonD = Button(win, text = "D", font=myFont, command = chooseTone("D"), anchor = CENTER)
    buttonD.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonD_window = canvas.create_window(625, 280, anchor=N, window=buttonD)



    buttonA = Button(win, text = "A", font=myFont, command = chooseTone("A"), anchor = CENTER)
    buttonA.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonA_window = canvas.create_window(650, 350, anchor=N, window=buttonA)

    buttonE = Button(win, text = "E", font=myFont, command = chooseTone("E"), anchor = CENTER)
    buttonE.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonE_window = canvas.create_window(625, 420, anchor=N, window=buttonE)

    buttonH = Button(win, text = "H", font=myFont, command = chooseTone("H"), anchor = CENTER)
    buttonH.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonH_window = canvas.create_window(570, 470, anchor=N, window=buttonH)



    buttonE = Button(win, text = "Fis", font=myFont, command = chooseTone("Fis"), anchor = CENTER)
    buttonE.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonE_window = canvas.create_window(500, 500, anchor=N, window=buttonE)

    buttonDes = Button(win, text = "Des", font=myFont, command = chooseTone("Des"), anchor = CENTER)
    buttonDes.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonDes_window = canvas.create_window(430, 470, anchor=N, window=buttonDes)

    buttonAs = Button(win, text = "As", font=myFont, command = chooseTone("As"), anchor = CENTER)
    buttonAs.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonAs_window = canvas.create_window(375, 420, anchor=N, window=buttonAs)



    buttonEs = Button(win, text = "Es", font=myFont, command = chooseTone("Es"), anchor = CENTER)
    buttonEs.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonEs_window = canvas.create_window(350, 350, anchor=N, window=buttonEs)

    buttonB = Button(win, text = "B", font=myFont, command = chooseTone("B"), anchor = CENTER)
    buttonB.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonB_window = canvas.create_window(375, 280, anchor=N, window=buttonB)

    buttonF = Button(win, text = "F", font=myFont, command = chooseTone("F"), anchor = CENTER)
    buttonF.configure(width = 3, height = 1, activebackground = "#738fa7", relief = FLAT)
    buttonF_window = canvas.create_window(430, 230, anchor=N, window=buttonF)



    buttonDrum1 = Button(win, text = "Drum One", font=myFont, command = chooseDrum("Drum1"), anchor = CENTER)
    buttonDrum1.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum1_window = canvas.create_window(1000, 200, anchor=N, window=buttonDrum1)

    buttonDrum2 = Button(win, text = "Drum Two", font=myFont, command = chooseDrum("Drum2"), anchor = CENTER)
    buttonDrum2.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum2_window = canvas.create_window(1000, 250, anchor=N, window=buttonDrum2)

    buttonDrum3 = Button(win, text = "Drum Three", font=myFont, command = chooseDrum("Drum3"), anchor = CENTER)
    buttonDrum3.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum3_window = canvas.create_window(1000, 300, anchor=N, window=buttonDrum3)


    canvas.create_text(850, 420, text ="Speed", fill="black", font=("Arial 15 bold"))
    slider = Scale(win, from_= 1, to_=200, orient= HORIZONTAL)
    slider.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    slider_window = canvas.create_window(1000, 400, anchor=N, window=slider)



    playButton = Button(win, text = "Play", font = myFont, command = playTrack(chosenTone, chosenDrum, chosenSpeed), anchor = W)
    playButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    playButton_window = canvas.create_window(750, 630, anchor=N, window=playButton)

    stopButton = Button(win, text = "Stop", font = myFont, command = stopTrack, anchor = W)
    stopButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    stopButton_window = canvas.create_window(820, 630, anchor=N, window=stopButton)

    win.mainloop()

configureSong()