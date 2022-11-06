from synthesizer import Player, Synthesizer, Waveform
from pychord import Chord
import pretty_midi
import os


i = 0

def create_midi(chords):
    global i 
    i += 1
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program("Acoustic Grand Piano")
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            piano.notes.append(note)
    midi_data.instruments.append(piano)
    midi_data.write("chord" + str(i) + ".mid")



def chordStr(chordtypes):
    chords_str = [chordtypes]
    chords = [Chord(c) for c in chords_str]
    create_midi(chords)


def doSound(chordfile):
    player = Player()
    player.open_stream()
    synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
    player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

    chord = [440.0, 550.0, 660.0]
    player.play_wave(synthesizer.generate_chord(chord, 3.0))

    from playsound import playsound
    playsound(chordfile)

def deleteChords():
    if os.path.exists(("chord" + str(i) + ".mid")):
        os.remove(("chord" + str(i) + ".mid"))
        i =- 1
    else:
        print("The file does not exist")

def onClick_C():
    chordStr("C")
    print("chord" + str(i) + ".mid")
    doSound("chord" + str(i) + ".mid")

onClick_C()
onClick_C()
onClick_C()
onClick_C()