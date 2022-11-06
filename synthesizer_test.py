from synthesizer import Player, Synthesizer, Waveform

from multiprocessing import Process


def play1():
    from playsound import playsound
    playsound('OS_ELK_SFX22.wav')
    
def play2():
    from playsound import playsound
    playsound('OS_ELK_C_Synth_Instrument_Hit_4.wav')

if __name__ == '__main__':
    P1 = Process(name="playsound1", target=play1)
    P1.start()

    P2 = Process(name="playsound2", target=play2)
    P2.start()

"""playsound('OS_ELK_SFX22.wav', block=True)
playsound('OS_ELK_C_Synth_Instrument_Hit_4.wav', block=True)


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))


chord = [440.0, 550.0, 660.0]
player.play_wave(synthesizer.generate_chord(chord, 3.0))"""

