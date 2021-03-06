#step1. import pygame
import pygame

#step2. define screen size
#step3. create screen
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

#step4. load a image
background = pygame.image.load("./background.jpg")

#ste5. display image on the game screen
#step6. create game loop => loop displaying image
# keep_alive = True
# while keep_alive:
# 	screen.blit(background, [0,0])
# 	pygame.display.update()

#step7. load a spaceship and a bullet image
#blit a bullet first, followed by spaceship,
#because the bullet should be hide behind spaceship
spaceship = pygame.image.load("./rocket-2442125_640.png")
bullet = pygame.image.load("./bullet-310444_640.png")
keep_alive = True
while keep_alive:
	screen.blit(background, [0, 0])
	screen.blit(bullet, [50, 400])
	screen.blit(spaceship, [20, 400])
	pygame.display.update()

