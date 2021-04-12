#step1. import pygame
import pygame

#step2. define screen size
#step3. create screen
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

#step4. load a image
background = pygame.image.load("./background.jpg")

#ste5. display image on the game screen
#screen.blit(background, [0, 0])

#step6. create game loop => loop displaying image
keep_alive = True
while keep_alive:
	screen.blit(background, [0,0])
	pygame.display.update()