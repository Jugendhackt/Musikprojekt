from tkinter import *

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
    win.geometry("1500x1000")

    canvas = Canvas(win, bg="#c3ceda", height = "1000", width = "1500")

    canvas.create_rectangle(250,100,1250,700, fill = "#738fa7")
    canvas.pack()

    canvas.create_text(750, 40, text ="Configure Your SONG", fill="black", font=("Arial 37 bold"))
    canvas.create_text(500, 170, text ="Choose tone", fill="black", font=("Arial 20 bold"))

    chosenText = Label(text = "Tone Choice", font = myFont)
    chosenText_window = canvas.create_window(500, 350, window = chosenText, anchor = CENTER)

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
            self.button = canvas.create_window(x, y, anchor = N, window=self.button)

    buttonC = QuintButton("C")
    buttonC.create_buttons(500, 200)

    buttonG = QuintButton("G")
    buttonG.create_buttons(570, 230)

    buttonD = QuintButton("D")
    buttonD.create_buttons(625, 280)

    buttonA = QuintButton("A")
    buttonA.create_buttons(650, 350)

    buttonE = QuintButton("E")
    buttonE.create_buttons(625, 420)

    buttonH = QuintButton("H")
    buttonH.create_buttons(570, 470)

    buttonFis = QuintButton("Fis")
    buttonFis.create_buttons(500, 500)

    buttonDes = QuintButton("Des")
    buttonDes.create_buttons(430, 470)

    buttonAs = QuintButton("As")
    buttonAs.create_buttons(375, 420)

    buttonEs = QuintButton("Es")
    buttonEs.create_buttons(350, 350)

    buttonB = QuintButton("B")
    buttonB.create_buttons(375, 280)

    buttonF = QuintButton("F")
    buttonF.create_buttons(430, 230)



    buttonDrum1 = Button(win, text = "Drum One", font=myFont, command = chooseDrum("Drum1"), anchor = CENTER)
    buttonDrum1.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum1_window = canvas.create_window(1000, 200, anchor=N, window=buttonDrum1)

    buttonDrum2 = Button(win, text = "Drum Two", font=myFont, command = chooseDrum("Drum2"), anchor = CENTER)
    buttonDrum2.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum2_window = canvas.create_window(1000, 250, anchor=N, window=buttonDrum2)

    buttonDrum3 = Button(win, text = "Drum Three", font=myFont, command = chooseDrum("Drum3"), anchor = CENTER)
    buttonDrum3.configure(width = 9, activebackground = "#738fa7", relief = FLAT)
    buttonDrum3_window = canvas.create_window(1000, 300, anchor=N, window=buttonDrum3)


    canvas.create_text(850, 400, text ="Speed", fill="black", font=("Arial 15 bold"))
    sliderSpeed = Scale(win, from_= 1, to_=200, orient= HORIZONTAL)
    sliderSpeed.set(100)
    sliderSpeed.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    sliderSpeed_window = canvas.create_window(1000, 400, anchor=CENTER, window=sliderSpeed)

    canvas.create_text(850, 480, text ="Pulse", fill="black", font=("Arial 15 bold"))
    sliderPulse = Scale(win, from_= 1, to_=32, orient= HORIZONTAL)
    sliderPulse.set(16)
    sliderPulse.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    sliderPulse_window = canvas.create_window(1000, 480, anchor=CENTER, window=sliderPulse)

    canvas.create_text(850, 560, text ="Beats", fill="black", font=("Arial 15 bold"))
    sliderBeats = Scale(win, from_= 1, to_=32, orient= HORIZONTAL)
    sliderBeats.set(16)
    sliderBeats.configure(length= 200, activebackground = "#738fa7", relief = FLAT)
    sliderBeats_window = canvas.create_window(1000, 560, anchor=CENTER, window=sliderBeats)



    playButton = Button(win, text = "Play", font = myFont, command = playTrack(chosenTone, chosenDrum, chosenSpeed), anchor = W)
    playButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    playButton_window = canvas.create_window(750, 630, anchor=N, window=playButton)

    stopButton = Button(win, text = "Stop", font = myFont, command = stopTrack, anchor = W)
    stopButton.configure(width = 4, activebackground = "#738fa7", relief = FLAT)
    stopButton_window = canvas.create_window(820, 630, anchor=N, window=stopButton)

    win.mainloop()