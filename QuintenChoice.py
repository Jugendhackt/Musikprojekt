from tkinter import *

chosenTone = 0
chosenDrum = 0
chosenSpeed = 0

def chooseTone(tone):
    chosenTone = tone

def chooseDrum(drum):
    chosenDrum = drum

def chooseSpeed(speed):
    chosenSpeed =speed

def playTrack(tone, drums, speed):
    a = 1
    #An Backend senden


win = Tk()
win.geometry("1500x1000")
canvas = Canvas(win, bg="#738fa7", height = "1500", width = "1000")
canvas.pack()

playButton = Button(win, text = "Play", command = playTrack(chosenTone, chosenDrum, chosenSpeed), anchor = W)
playButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
playButton_window = canvas.create_window(200, 400, anchor=NW, window=playButton)

buttonC = Button(win, text = "C", command = chooseTone("C"), anchor = W)
buttonC.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonC_window = canvas.create_window(500, 200, anchor=NW, window=buttonC)

buttonG = Button(win, text = "G", command = chooseTone("G"), anchor = W)
buttonG.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonG_window = canvas.create_window(570, 230, anchor=NW, window=buttonG)

buttonD = Button(win, text = "D", command = chooseTone("D"), anchor = W)
buttonD.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonD_window = canvas.create_window(625, 275, anchor=NW, window=buttonD)



buttonA = Button(win, text = "A", command = chooseTone("A"), anchor = W)
buttonA.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonA_window = canvas.create_window(650, 350, anchor=NW, window=buttonA)

buttonE = Button(win, text = "E", command = chooseTone("E"), anchor = W)
buttonE.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonE_window = canvas.create_window(625, 425, anchor=NW, window=buttonE)

buttonH = Button(win, text = "H", command = chooseTone("H"), anchor = W)
buttonH.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonH_window = canvas.create_window(570, 470, anchor=NW, window=buttonH)



buttonE = Button(win, text = "Fis", command = chooseTone("Fis"), anchor = W)
buttonE.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonE_window = canvas.create_window(500, 500, anchor=NW, window=buttonE)

buttonDes = Button(win, text = "Des", command = chooseTone("Des"), anchor = W)
buttonDes.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonDes_window = canvas.create_window(430, 470, anchor=NW, window=buttonDes)

buttonAs = Button(win, text = "As", command = chooseTone("As"), anchor = W)
buttonAs.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonAs_window = canvas.create_window(375, 430, anchor=NW, window=buttonAs)



buttonEs = Button(win, text = "Es", command = chooseTone("Es"), anchor = W)
buttonEs.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonEs_window = canvas.create_window(350, 350, anchor=NW, window=buttonEs)

buttonB = Button(win, text = "B", command = chooseTone("B"), anchor = W)
buttonB.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonB_window = canvas.create_window(375, 275, anchor=NW, window=buttonB)

buttonF = Button(win, text = "F", command = chooseTone("F"), anchor = W)
buttonF.configure(width = 2, activebackground = "#738fa7", relief = FLAT)
buttonF_window = canvas.create_window(430, 230, anchor=NW, window=buttonF)


win.mainloop()

