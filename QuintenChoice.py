from tkinter import *
from RectangleFunction import *
from ColorSchema import *
import loop
from multiprocessing import Process

chosenTones = []
chosenDrum = []
chosenBeats = []

def configureSong():

    myFont = ("Arial 15")

    win = Tk()
    win.geometry("1500x780")

    canvas = Canvas(win, bg="#c3ceda", height = "780", width = "1500")
    
    create_good_rectangle(canvas, 240, 90, 1260, 710, 40, 8, primaryAccent)
    create_good_rectangle(canvas, 250, 100, 1250, 700, 40, 8, secondaryAccent)
   
    canvas.create_text(860,400, text ="Beat 1", fill="#071330", font=("Arial 15 bold"))
    global beat1
    beat1 = Scale(canvas, from_= 1, to_=16, orient= HORIZONTAL)
    beat1.set(8)
    beat1.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    beat1Window = canvas.create_window(1000,400, window = beat1)

    canvas.create_text(860,450, text ="Beat 2", fill="#071330", font=("Arial 15 bold"))
    global beat2
    beat2 = Scale(canvas, from_= 1, to_=16, orient= HORIZONTAL)
    beat2.set(8)
    beat2.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    beat2Window = canvas.create_window(1000,450, window = beat2)

    canvas.create_text(860,500, text ="Beat 3", fill="#071330", font=("Arial 15 bold"))
    global beat3 
    beat3 = Scale(canvas, from_= 1, to_=16, orient= HORIZONTAL)
    beat3.set(8)
    beat3.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    beat3Window = canvas.create_window(1000,500, window = beat3)
    canvas.pack()

    canvas.create_text(750, 50, text ="Configure Your SONG", fill="#071330", font=("Arial 37 bold"))
    canvas.create_text(500, 170, text ="Choose tone", fill="#071330", font=("Arial 20 bold"))

    chosenText = Label(text = "Circle of fifths", font = myFont)
    chosenText_window = canvas.create_window(500, 390, window = chosenText, anchor = CENTER)
    class DrumButton:

        def __init__(self, drum, width = 9):
            self.width = width
            self.drum =drum

        def chooseDrum(self):
            #global chosenDrum
            chosenDrum.append(self.drum)
            print(chosenDrum)

        def chooseDrum(self):
            global chosenDrum
            chosenDrum = self.drum
            print("Verstorben")

        def create_button(self, x, y):
            self.button = Button(win, text = self.drum, font=myFont, command = self.chooseDrum, anchor = CENTER)
            self.button.configure(activebackground = "#738fa7", relief = FLAT)
            self.button = canvas.create_window(x, y, anchor = N, window=self.button)

    class QuintButton:

        def __init__(self, tone, width = 3, height = 1, ):
            self.height = height
            self.width = width
            self.tone = tone

        def chooseTone(self):
            #global chosenTone
            if self.tone in chosenTones:
                chosenTones.remove(self.tone)
            elif len(chosenTones) <= 3:
                chosenTones.append(self.tone)
            print(chosenTones)
            


        def create_button(self, x, y):
            self.button = Button(win, text = self.tone, font = myFont, command = self.chooseTone,  anchor = CENTER)
            self.button.configure(activebackground = "#738fa7", relief = FLAT)
            self.button = canvas.create_window(x, y, anchor = CENTER, window=self.button)

    class StartButton:

        def __init__(self, width = 4):
            self.width = width

        def playTrack(self):
            #print(chosenTone, chosenDrum, chosenSpeed) 
            global P
            P = Process(target=loop.playpulse, args= (beat1.get(), beat2.get(),beat3.get()))
            P.start()
            print("Play")
        #Song aus Parametern abspielen

        def create_button(self, x, y):
            self.button = Button(win, text = "Play", font = myFont, command = self.playTrack, anchor = W)
            self.button.configure(activebackground = "#738fa7", relief = FLAT)
            self.button = canvas.create_window(x, y, anchor = N, window=self.button)

    
    """
    class Slider:

        def __init__(self, name):
            self.name = name

        

        def create_scale(self, scalefrom, scaleto, x, y):
            canvas.create_text(850, 560, text = self.name, fill="#071330", font=("Arial 15 bold"))
            global chosenBeats
            chosenBeats = Scale(win, from_= scalefrom, to_=scaleto, orient= HORIZONTAL)
            chosenBeats.set(16)
            chosenBeats.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
            chosenBeats_window = canvas.create_window(x, y, anchor=CENTER, window=chosenBeats)
    """


    def stopTrack():
        global P
        P.terminate()
        P.join()

    buttonC = QuintButton("C")
    buttonC.create_button(500, 240)

    buttonG = QuintButton("G")
    buttonG.create_button(570, 270)

    buttonD = QuintButton("D")
    buttonD.create_button(625, 320)

    buttonA = QuintButton("A")
    buttonA.create_button(650, 390)

    buttonE = QuintButton("E")
    buttonE.create_button(625, 460)

    buttonH = QuintButton("H")
    buttonH.create_button(570, 510)

    buttonFis = QuintButton("Fis")
    buttonFis.create_button(500, 540)

    buttonDes = QuintButton("Des")
    buttonDes.create_button(430, 510)

    buttonAs = QuintButton("As")
    buttonAs.create_button(375, 460)

    buttonEs = QuintButton("Es")
    buttonEs.create_button(350, 390)

    buttonB = QuintButton("B")
    buttonB.create_button(375, 320)

    buttonF = QuintButton("F")
    buttonF.create_button(430, 270)

    buttonDrum1 = DrumButton("Drum One")
    buttonDrum1.create_button(1000, 200)
    
    buttonDrum2 = DrumButton("Drum Two")
    buttonDrum2.create_button(1000, 250)

    buttonDrum3 = DrumButton("Drum Three")
    buttonDrum3.create_button(1006, 300)

    playButton = StartButton()
    playButton.create_button(750, 630)

    stopButton = Button(win, text = "Stop", font = myFont, command = stopTrack, anchor = W)
    stopButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    stopButton_window = canvas.create_window(820, 630, anchor=N, window=stopButton)

    canvas.create_text(1000, 170, text ="Choose drumset", fill="#071330", font=("Arial 20 bold"))



    win.mainloop()

