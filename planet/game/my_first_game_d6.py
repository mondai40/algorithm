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
#step7. load a spaceship and a bullet image
spaceship = pygame.image.load('./rocket-2442125_640.png')
bullet = pygame.image.load('./bullet-310444_640.png')

#step8. activate evet listenr
#step9. collect all keys
#step10. listen and check the pressed key
#step11. load alien
alien = pygame.image.load('./alien.png')
#step12. make animation direction and animation move steps
#step13. make bullet's animation
keep_alive = True
alien_x = 140
move_direction = "right"

fired = False
bullet_y = 500

while keep_alive:
  pygame.event.get()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE] == True:
    fired = True

  if move_direction == "right":
    alien_x += 1
    if alien_x == 300:
      move_direction = "left"
  else:
    alien_x -= 1
    if alien_x == 0:
      move_direction = "right"

  if fired:
    bullet_y -= 5
    if bullet_y == 50:
      fired = False
      bullet_y = 500

  screen.blit(background, [0, 0])
  screen.blit(alien, [alien_x, 50])
  screen.blit(bullet, [0, bullet_y])
  screen.blit(spaceship, [0, 500])
  pygame.display.update()



