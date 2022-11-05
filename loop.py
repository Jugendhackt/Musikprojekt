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


if __name__ == '__main__':
    zähler=0
    play=True

    beats= 6
    pulses= 50

    while play == True:
        soundtest=euclidean_rhythm (beats,pulses)
        for i in range (0, len(soundtest)) :
            time.sleep(1)
            if (soundtest[i] == 1):
                P1 = Process(target=playsound, args=("OS_ELK_SFX22.wav",))
                P2 = Process(target=playsound, args=("OS_ELK_C_Synth_Instrument_Hit_4.wav",))
                
                #P1 = Process(name="sound1", target=playsound, args=("OS_ELK_SFX22.wav",))
                #P2 = Process(name="sound2", target=playsound, args=("OS_ELK_C_Synth_Instrument_Hit_4.wav",))
                
                #P1 = Process(target=play1)
                #P2 = Process(target=play2)
                 
                
                P2.start()
                P1.start()
                            
                            
                    
    #print(euclidean_rhythm (4,16))

    