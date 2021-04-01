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
background = pygame.image.load("./background.jpg");

#ste5. display image on the game screen
#.bilt() stands for block image transfer
#the second parameter is coordinate
screen.blit(background, [0, 0])

} 
