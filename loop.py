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
    zähler=0
    global play
    play = True
    print("playpulse")

    beats= 6
    pulses= 50

    while play == True:
        soundtest1=euclidean_rhythm (beats,pulses)
        soundtest2=euclidean_rhythm (beats+3,pulses)
        for i in range (0, len(soundtest1)) :
            time.sleep(0.5)
            if (soundtest1[i] == 1):
                P1 = Process(target=playsound, args=(u"Sounds/OS_ELK_Kick6.wav",))
                
                
                #P1 = Process(name="sound1", target=playsound, args=("OS_ELK_SFX22.wav",))
                #P2 = Process(name="sound2", target=playsound, args=("OS_ELK_C_Synth_Instrument_Hit_4.wav",))
                
                #P1 = Process(target=play1)
                #P2 = Process(target=play2)
                P1.start()

            if (soundtest2[i] == 1):     

                P2 = Process(target=playsound, args=(u"Sounds/OS_ELK_Snare13.wav",))
                P2.start()
                
                            
                            
                    
    #print(euclidean_rhythm (4,16))

    