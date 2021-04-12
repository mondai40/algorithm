#step1. import pygame
import pygame

#step2. define screen size
screen_size = [360, 600]

#step3. create screen
#you need to do something on a screen, so create a valuable for screen
screen = pygame.display.set_mode(screen_size)

#step4. load a image
#you need to move this image, so create a variable
#If you have many images to load, you had better criate a function or class
background = pygame.image.load("./background.jpg")

#ste5. display image on the game screen
#.bilt() stands for block image transfer
#the second parameter is coordinate
#screen.blit(background, [0, 0])

#step6. create game loop => loop displaying image
#keep_alive = True
#while keep_alive:
#	screen.blit(background, [0,0])
#	pygame.display.update()

#step7. load a spaceship and a bullet image
#blit a bullet first, followed by spaceship,
#because the bullet should be hide behind spaceship
spaceship = pygame.image.load('./rocket-2442125_640.png')
bullet = pygame.image.load('./bullet-310444_640.png')
#keep_alive = True
#while keep_alive:
#	screen.blit(background, [0, 0])
#	screen.blit(bullet, [180, 500])
#	screen.blit(spaceship, [160, 500])
#	pygame.display.update()

#step8. activate evet listenr
#step9. collect all keys
#step10. listen and check the pressed key
#step11. load alien
#step12. make animation direction and animation move steps
alien = pygame.image.load('./alien.png')
keep_alive = True
alien_x = 140
move_direction = "right"
while keep_alive:
	pygame.event.get()

	keys = pygame.key.get_pressed()
	if keys[pygame.K_SPACE] == True:
		print("Space is typed")

	if move_direction == "right":
		alien_x += 1
		if alien_x == 300:
			move_direction = "left"
	else:
		alien_x -= 1
		if alien_x == 0:
			move_direction = "right"

	screen.blit(background, [0, 0])
	screen.blit(alien, [alien_x, 50])
	screen.blit(bullet, [180, 500])
	screen.blit(spaceship, [160, 500])
	pygame.display.update()
