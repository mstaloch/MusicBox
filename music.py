import pygame
from pygame import mixer


pygame.init()
mixer.init()

#SOUNDS
blop = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Blop.ogg")
clang = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Clang.ogg")
ting = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Ting.ogg")
banner = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Banner.ogg")
pling = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Pling.ogg")
moo = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/moo.ogg")

#MAIN
print("Press a key to play a sound! (ESC to quit)")
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				blop.play()
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			if event.key == pygame.K_w:
				clang.play()
			if event.key == pygame.K_e:
				ting.play()
			if event.key == pygame.K_r:
				banner.play()
			if event.key == pygame.K_t:
				pling.play()
			if event.key == pygame.K_y:
				moo.play()

