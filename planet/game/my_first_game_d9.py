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
#step11. load
alien_index = 0
aliens = ["./alien.png", "./alien2.png", "./alien3.png"]
alien = pygame.image.load(aliens[alien_index])
#step12. make animation direction and animation move steps
#step13. make bullet's animation
keep_alive = True
alien_x = 140
move_direction = "right"
#step14. set fps(= frame per seconds)
clock = pygame.time.Clock()

fired = False
bullet_y = 500

while keep_alive:
  pygame.event.get()

  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE] == True:
    fired = True

  if move_direction == "right":
    alien_x += 5
    if alien_x == 300:
      move_direction = "left"
  else:
    alien_x -= 5
    if alien_x == 0:
      move_direction = "right"

  if fired:
    bullet_y -= 8
    if bullet_y < 50:
      fired = False
      bullet_y = 500

  screen.blit(background, [0, 0])
  screen.blit(alien, [alien_x, 50])
  screen.blit(bullet, [0, bullet_y])
  screen.blit(spaceship, [0, 500])

  #step15. watch if its collide
  if (bullet_y < 80 and alien_x > 100 and alien_x < 180):
    alien_index += 1
    print("boom")
    if alien_index < len(aliens):
      alien = pygame.image.load(aliens[alien_index])
      alien_x = 10
    else:
      print("You win")
      keep_alive = False

  pygame.display.update()
  clock.tick(60)



