from tkinter import *
from RectangleFunction import *
from ColorSchema import *
def configureSong():
    
    chosenTone = 0
    chosenDrum = 0
    chosenSpeed = 0
    myFont = ("Arial 15")

        
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
    win.geometry("1500x780")

    canvas = Canvas(win, bg="#c3ceda", height = "780", width = "1500")

    create_good_rectangle(canvas, 250, 100, 1250, 700, 40, 8, secondaryAccent)

    canvas.pack()

    canvas.create_text(750, 50, text ="Configure Your SONG", fill="#071330", font=("Arial 37 bold"))
    canvas.create_text(500, 170, text ="Choose tone", fill="#071330", font=("Arial 20 bold"))

    chosenText = Label(text = "Tone Choice", font = myFont)
    chosenText_window = canvas.create_window(500, 390, window = chosenText, anchor = CENTER)

    class QuintButton:

        def __init__(self, tone, width = 3, height = 1, ):
            self.height = height
            self.width = width
            self.tone = tone

        def chooseTone(self):
            chosenTone = self.tone
            print("Verstorben")

        def create_buttons(self, x, y):
            self.button = Button(win, text = self.tone, font = myFont, command = self.chooseTone,  anchor = CENTER)
            self.button.configure(activebackground = "#738fa7", relief = FLAT)
            self.button = canvas.create_window(x, y, anchor = CENTER, window=self.button)

    buttonC = QuintButton("C")
    buttonC.create_buttons(500, 240)

    buttonG = QuintButton("G")
    buttonG.create_buttons(570, 270)

    buttonD = QuintButton("D")
    buttonD.create_buttons(625, 320)

    buttonA = QuintButton("A")
    buttonA.create_buttons(650, 390)

    buttonE = QuintButton("E")
    buttonE.create_buttons(625, 460)

    buttonH = QuintButton("H")
    buttonH.create_buttons(570, 510)

    buttonFis = QuintButton("Fis")
    buttonFis.create_buttons(500, 540)

    buttonDes = QuintButton("Des")
    buttonDes.create_buttons(430, 510)

    buttonAs = QuintButton("As")
    buttonAs.create_buttons(375, 460)

    buttonEs = QuintButton("Es")
    buttonEs.create_buttons(350, 390)

    buttonB = QuintButton("B")
    buttonB.create_buttons(375, 320)

    buttonF = QuintButton("F")
    buttonF.create_buttons(430, 270)

    
    canvas.create_text(1000, 170, text ="Choose drumset", fill="#071330", font=("Arial 20 bold"))

    buttonDrum1 = Button(win, text = "One", font=myFont, command = chooseDrum("Drum1"), anchor = CENTER)
    buttonDrum1.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum1_window = canvas.create_window(1000, 200, anchor=N, window=buttonDrum1)

    buttonDrum2 = Button(win, text = "Two", font=myFont, command = chooseDrum("Drum2"), anchor = CENTER)
    buttonDrum2.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum2_window = canvas.create_window(1000, 250, anchor=N, window=buttonDrum2)

    buttonDrum3 = Button(win, text = "Three", font=myFont, command = chooseDrum("Drum3"), anchor = CENTER)
    buttonDrum3.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum3_window = canvas.create_window(1000, 300, anchor=N, window=buttonDrum3)


    canvas.create_text(850, 400, text ="Speed", fill="#071330", font=("Arial 15 bold"))
    chosenSpeed = Scale(win, from_= 1, to_=200, orient= HORIZONTAL)
    chosenSpeed.set(100)
    chosenSpeed.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    chosenSpeed_window = canvas.create_window(1000, 400, anchor=CENTER, window=chosenSpeed)

    canvas.create_text(850, 480, text ="Pulse", fill="#071330", font=("Arial 15 bold"))
    chosenPulse = Scale(win, from_= 1, to_=32, orient= HORIZONTAL)
    chosenPulse.set(16)
    chosenPulse.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    chosenPulse_window = canvas.create_window(1000, 480, anchor=CENTER, window=chosenPulse)

    canvas.create_text(850, 560, text ="Beats", fill="#071330", font=("Arial 15 bold"))
    chosenBeats = Scale(win, from_= 1, to_=32, orient= HORIZONTAL)
    chosenBeats.set(16)
    chosenBeats.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    chosenBeats_window = canvas.create_window(1000, 560, anchor=CENTER, window=chosenBeats)



    playButton = Button(win, text = "Play", font = myFont, command = playTrack(chosenTone, chosenDrum, chosenSpeed), anchor = W)
    playButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    playButton_window = canvas.create_window(710, 630, anchor=N, window=playButton)

    stopButton = Button(win, text = "Stop", font = myFont, command = stopTrack, anchor = W)
    stopButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    stopButton_window = canvas.create_window(790, 630, anchor=N, window=stopButton)

    mainloop()
