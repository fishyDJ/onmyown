# DJ Holder 2/6/2023 v.1.1
# sources - (cat animation - https://www.artstation.com/artwork/nYnX2r)
# (forest_bg - https://www.shutterstock.com/search)     https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/

import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

x_pos = 350
y_pos = 350

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

#define game variables
scroll = 0
ground_image = pygame.image.load("onmyown/Assets/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
bg_img = pygame.image.load(f"onmyown/Assets/plx-5.jpg").convert_alpha()
bg_image = pygame.transform.scale(bg_img, (600, 450))
bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  for x in range(5):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2

def draw_ground():
  for x in range(15):
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))

class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"onmyown/Assets/exp{num}.png")
			img = pygame.transform.scale(img, (100, 100))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0

	def update(self):
		explosion_speed = 4
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, reset animation index
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()


explosion_group = pygame.sprite.Group()


#game loop
run = True
while run:
  
  clock.tick(FPS)

  #draw world
  draw_bg()
  draw_ground()
  
  box = pygame.draw.rect(screen, 'green', (x_pos, y_pos, 30, 30), 20)
  
  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and scroll > 0:
    scroll -= 5
  if key[pygame.K_RIGHT] and scroll < 3000:
    scroll += 5

  explosion_group.draw(screen)
  explosion_group.update()


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      explosion = Explosion(pos[0], pos[1])
      explosion_group.add(explosion)
      
      
  pygame.display.update()


pygame.quit()