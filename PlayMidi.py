import pygame

pygame.mixer.init()

def play_midi(midi_file):
    pygame.mixer.music.load(midi_file)
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play()
    print("Start")
    while pygame.mixer.music.get_busy():
        print("Nicht Ende")
    print("Ende?")

def play_midi2():
   sound = pygame.mixer.Sound("chord.mid")
   sound.play()



play_midi("chord.mid")
print("Ende")






