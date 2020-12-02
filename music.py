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

bikeHorn = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Bike Horn.ogg")
drumRoll = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Drum Roll.ogg")
growl = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Growl.ogg")
jokeSting = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Joke Sting.ogg")
metalBang = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Metal Bang.ogg")
stag = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Red-Stag-Roar.ogg")
smallChain = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Small Chain.ogg")
suspense = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/Suspense Chord.ogg")
trex = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/TRex.ogg")
bite = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/bite.ogg")
chomp = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/chomp.ogg")
doorbell = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/doorbell.ogg")
deskBells = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/front-desk-bells.ogg")
kick = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/kick.ogg")
oldFashion = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/old-fashioned.ogg")
ping = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/ping.ogg")
punch = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/punch.ogg")
slap = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/slap.ogg")
woof = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/woof.ogg")
buzzer = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/buzzer.ogg")
eagle = pygame.mixer.Sound("/home/rambler/264/MusicBox/sounds/eagle.ogg")

pygame.display.init()
screen = pygame.display.set_mode ( ( 320 , 240 ) )

#MAIN
print("Press a key to play a sound! (ESC to quit)")
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				sys.exit
			if event.key == pygame.K_q:
				blop.play()
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
			if event.key == pygame.K_u:
				bikeHorn.play()
			if event.key == pygame.K_i:
				drumRoll.play()
			if event.key == pygame.K_o:
				growl.play()
			if event.key == pygame.K_p:
				jokeSting.play()
			if event.key == pygame.K_a:
				metalBang.play()
			if event.key == pygame.K_s:
				stag.play()
			if event.key == pygame.K_d:
				smallChain.play()
			if event.key == pygame.K_f:
				suspense.play()
			if event.key == pygame.K_g:
				trex.play()
			if event.key == pygame.K_h:
				bite.play()
			if event.key == pygame.K_j:
				chomp.play()
			if event.key == pygame.K_k:
				doorbell.play()
			if event.key == pygame.K_l:
				deskBells.play()
			if event.key == pygame.K_z:
				kick.play()
			if event.key == pygame.K_x:
				oldFashion.play()
			if event.key == pygame.K_c:
				ping.play()
			if event.key == pygame.K_v:
				slap.play()
			if event.key == pygame.K_b:
				woof.play()
			if event.key == pygame.K_n:
				buzzer.play()
			if event.key == pygame.K_m:
				eagle.play()
