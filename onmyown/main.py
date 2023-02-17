# DJ Holder 2/6/2023 v.1.1
# sources - (cat animation - https://www.artstation.com/artwork/nYnX2r)   (pygame.org) (hole - https://www.istockphoto.com/vector/big-hole-in-ground-brown-dry-soil-and-mine-element-of-desert-landscape-cartoon-gm1400004175-453707204)
# (forest_bg - https://www.shutterstock.com/search)     (animation - https://www.simplifiedpython.net/pygame-sprite-animation-tutorial/) (hole - https://www.remove.bg/upload)

import pygame
from pygame.locals import * 
import os
import math
pygame.init()

clock = pygame.time.Clock()
FPS = 30

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 432

speed = 5
x_pos = 300
y_pos = 325
move_right = False
move_down = False
move_left = False
move_up = False
move_downf = True
hx = 600
hy = 280
s = 0

pygame.mixer.init()
pygame.mixer.music.load(os.path.join('onmyown\Assets\jungle-shenanigans.mp3'))
pygame.mixer.music.play()

font = pygame.font.Font("freesansbold.ttf", 15)
font1 = pygame.font.Font("freesansbold.ttf", 30)
l_text = font1.render("You Lost", True, (255, 255, 255))
w_text = font1.render("You Won", True, (255, 255, 255))
wi_text = font1.render("The cat's journey to water", True, (255, 255, 255))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Parallax")

#define game variables
scroll = 0
ground_image = pygame.image.load("onmyown/Assets/ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

water = pygame.image.load("onmyown/Assets/cut_waterfr.jpg").convert_alpha()
water_height = water.get_height()
water = pygame.transform.scale(water, (600,water_height))
water_width = water.get_width()
water_height = water.get_height()

bg_images = []
bg_img = pygame.image.load(f"onmyown/Assets/plx-5.jpg").convert_alpha()
bg_image = pygame.transform.scale(bg_img, (600, 450))
bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

hole = pygame.image.load("onmyown/Assets/hole_better.png")
hole = pygame.transform.scale(hole, (230, 230))


def draw_bg():
  for x in range(15):
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2

def draw_ground():
  for x in range(20):
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))

class MySprite(pygame.sprite.Sprite):
  def __init__(self):
    super(MySprite, self).__init__()

    self.images = []
    for i in range(1,12):
      self.images.append(pygame.image.load(f'onmyown/Assets/cat_run{i} (1).png')) 

    self.index = 0

    self.image1 = self.images[self.index]
    self.image = pygame.transform.scale(self.image1, (20, 25))
    self.rect = pygame.Rect(x_pos, y_pos, 20, 25)

  def update(self):
    self.index += 1

    if self.index >= len(self.images):
      self.index = 0
      
    self.image = self.images[self.index]

class Jumpy(pygame.sprite.Sprite):
  def __init__(self):
    super(Jumpy, self).__init__()

    self.images = []
    x = 4
    for i in range(x):
      self.images.append(pygame.image.load('onmyown/Assets/cat_jump1_.png'))
    for i in range(x):
      self.images.append(pygame.image.load('onmyown/Assets/cat_jump2_.png'))
    for i in range(x):
      self.images.append(pygame.image.load('onmyown/Assets/cat_jump3_.png'))
    for i in range(x):
      self.images.append(pygame.image.load('onmyown/Assets/cat_jump4_.png'))
    for i in range(x):
      self.images.append(pygame.image.load('onmyown/Assets/cat_jump5_.png'))

    self.index = 0

    self.image1 = self.images[self.index]
    self.image = pygame.transform.scale(self.image1, (20, 25))
    self.rect = pygame.Rect(x_pos, y_pos, 20, 25)

  def update(self):
    self.index += 1
    self.index = math.floor(self.index)
    if self.index >= (len(self.images)):
      self.index = 0
    self.rect = pygame.Rect(x_pos, y_pos, 20, 25)      
    self.image = self.images[self.index]
               
jump = Jumpy()
jump_group = pygame.sprite.Group(jump)

my_sprite = MySprite()
my_group = pygame.sprite.Group(my_sprite)

still = pygame.image.load("onmyown/Assets/cat_still.png")
still = pygame.transform.scale(still, (80, 60))

jumps = pygame.image.load("onmyown/Assets/cat_jump1_.png")
jumps = pygame.transform.scale(jumps, (100, 100))

jumpe = pygame.image.load("onmyown/Assets/cat_jump4_.png")
jumpe = pygame.transform.scale(jumpe, (100, 100))

#game loop
run = True
while run:
  clock.tick(FPS)
  move_downf = False
  #draw world
  draw_bg()
  draw_ground()
  text = font.render(f"Score : {s}", True, (255, 255, 255))
  screen.blit(text, (5, 5))
  screen.blit(hole, (hx, hy))
  screen.blit(water, ((20 * ground_width) - scroll * 2.5, SCREEN_HEIGHT - water_height))
  
  #get keypresses
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT] and scroll > 0:
    scroll -= 5
  
  if key[pygame.K_RIGHT] and scroll < 8000:
    scroll += 5
  
  if scroll > (12*200)+60:
    screen.blit(w_text, (SCREEN_WIDTH/2-80, SCREEN_HEIGHT/2))
    pygame.display.update()
    pygame.time.wait(6000)
    pygame.quit()
    
    
    

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        move_right = True
      if event.key == pygame.K_LEFT:
        move_left = True
      if event.key == pygame.K_DOWN:
        move_down = True
      if event.key == pygame.K_UP:
        move_up = True
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        move_right = False
      if event.key == pygame.K_LEFT:
        move_left = False
      if event.key == pygame.K_DOWN:
        move_down = False
      if event.key == pygame.K_UP:
        move_up = False
  
  if move_up:# y_pos = 320
    if y_pos > 100:
      y_pos -=10
  if not move_up and y_pos < 320:
    move_downf = True
    y_pos += 10
    screen.blit(jumpe, (x_pos, y_pos-30))

  if move_right and not move_up and not move_downf:
    my_group.update()
    my_group.draw(screen)
  if not move_right and not move_up and not move_downf:
    screen.blit(still, (x_pos, y_pos))
  if move_up:
    screen.blit(jumps, (x_pos, y_pos))
    #jump_group.update()
    #jump_group.draw(screen)
  
  if move_right:
    hx -= 12.7
  if move_left:
    hx += 12.7
  
  if hx <= -200:
    hx = 900
  
  hp = 1
  if hx <= 240 and hx >= 230:
    s += 1
    
  if y_pos == 325 and hx <= 270 and hx >= 200:
    y_pos += 20
  if y_pos == 345:
    hp -= 1
  if hp == 0:
    screen.blit(l_text, (SCREEN_WIDTH/2-80, SCREEN_HEIGHT/2))
    pygame.display.update()
    pygame.time.wait(3000)
    pygame.quit()

    
    
  
  
  
  pygame.display.update()


pygame.quit()
