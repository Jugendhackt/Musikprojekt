from midiTest import euclidean_rhythm
import time
from synthesizer import Player, Synthesizer, Waveform
from multiprocessing import Process
from playsound import playsound


#def playprocess(sound):
#    print(sound)
#    playsound(sound)

def play1():
    playsound("OS_ELK_SFX22.wav")

def play2():
    playsound("OS_ELK_C_Synth_Instrument_Hit_4.wav")



def playpulse():
    instrument1Beats=3
    instrument2Beats=2
    instrument4Beats=6
    instrument3Beats=16
    instrument5Beats=4

    instrument1= euclidean_rhythm(instrument1Beats,16)
    instrument2= euclidean_rhythm(instrument2Beats,16)
    instrument3= euclidean_rhythm(instrument3Beats,16)
    instrument4= euclidean_rhythm(instrument4Beats,16)
    instrument5= euclidean_rhythm(instrument5Beats,16)

    i1=0
    i2=0
    i3=0
    i4=0
    i5=0

    zähler=0
    global play
    play = True
    print("playpulse")

    beats= 6
    pulses= 50

    while play == True:
        if (instrument1[i1]==1):
            P1=Process(target=playsound, args=("OS_ELK_Kick6.wav",))
            P1.start()
        if (instrument2[i2]==1):
            P2=Process(target=playsound, args=("OS_ELK_Snare13.wav",))
            P2.start()
        if (instrument3[i3]==1):
            P3=Process(target=playsound, args=("OS_ELK_Top 14.wav",))
            P3.start()
        if (instrument4[i4]==1):
            P4=Process(target=playsound, args=("OS_ELK_Snare 20.wav",))
            P4.start()
        if (instrument5[i5]==1):
            P5 =Process(target=playsound, args=("bass_a.wav",))
            P5.start()
        i1=+1
        i2=+1
        i3=+1
        i4=+1
        i5=+1

        if (i1== len(instrument1)):
            i1 ==0
        if (i2== len(instrument1)):
            i2 ==0
        if (i3== len(instrument1)):
            i3 ==0
        if (i3== len(instrument1)):
            i3 ==0
        if (i4== len(instrument1)):
            i4 ==0
        if (i5== len(instrument1)):
            i5 ==0


        #for i in range (0, len(soundtest)) :
           # time.sleep(1)
           # if (soundtest[i] == 1):
               # P1 = Process(target=playsound, args=("OS_ELK_SFX22.wav",))
               # P2 = Process(target=playsound, args=("OS_ELK_C_Synth_Instrument_Hit_4.wav",))
                
                #P1 = Process(name="sound1", target=playsound, args=("OS_ELK_SFX22.wav",))
                #P2 = Process(name="sound2", target=playsound, args=("OS_ELK_C_Synth_Instrument_Hit_4.wav",))

                #P1 = Process(target=play1)
                #P2 = Process(target=play2)

                #P5.start()
                #P4.start()
                #P3.start()
               # P2.start()
                #P1.start()



    #print(euclidean_rhythm (4,16))
