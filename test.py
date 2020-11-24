import pygame, time
from pygame import mixer

pygame.init()
mixer.init()

blop = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Blop.ogg")
blop.play()

time.sleep(0.8)

#airhorn = pygame.mixer.Sound("home/rambler/264/MusicBox/sounds/AlienDrum.wav")
#airhorn.play()

#time.sleep(3)

print("DONE")
