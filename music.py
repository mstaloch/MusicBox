import pygame, time, keyboard
from pygame import mixer


pygame.init()
mixer.init()

blop = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Blop.ogg")
#blop.play()
#time.sleep(3)

#pygame.display.set_mode()


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				blop.play()
				time.sleep(0.8)
				break
			if event.key == pygame.K_ESCAPE:
				#airhorn.play()
				#time.sleep(1)
				sys.exit()
				break
#airhorn = pygame.mixer.Sound("home/rambler/264/MusicBox/sounds/AlienDrum.wav")
#airhorn.play()

#time.sleep(3)

print("DONE")

