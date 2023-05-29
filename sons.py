import pygame

class sons():
    def __init__(self):
        self.music_volume=pygame.mixer.music.set_volume(0.25)
        self.explose_sound=pygame.mixer.Sound("explose.wav")
        self.tire_sound=pygame.mixer.Sound("tire.wav")
        self.sound_volume()

    def sound_volume(self):
        self.explose_sound.set_volume(1)
        self.tire_sound.set_volume(0.15)
