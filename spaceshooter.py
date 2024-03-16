import pygame
import time
import random
pygame.init()
pygame.mouse.set_visible(0)
bg = pygame.image.load("bgspace.jpg")
bg = pygame.transform.scale(bg, (500,800))

color = (255, 255, 255)
rect_color = (255, 0, 0)
text = '0'
points = 0
font = pygame.font.SysFont(None, 48)
txt_points = font.render(text, True, (0,255,0))
clock = pygame.time.Clock()
canvas = pygame.display.set_mode((500, 800))
pygame.display.set_caption("Space Shooter")
exit = False
player_x = canvas.get_width()/2 - 30
player_y = 700
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
    def __init__(self,image):
       super().__init__()
       self.image = pygame.transform.scale(pygame.image.load(image), (100, 100))
       self.rect = self.image.get_rect()
       self.rect.x = canvas.get_width()/2 - 30
       self.rect.y = 700
    def show(self):
       self.rect.x = pygame.mouse.get_pos()[0]
       if self.rect.x >= 409:
          self.rect.x = 400
       canvas.blit(self.image,(self.rect.x,self.rect.y))
class Bullet(pygame.sprite.Sprite):
    def __init__(self,player):
      super().__init__()
      self.image = pygame.transform.scale(pygame.image.load('bullets.png'), (15, 50))
      self.rect = self.image.get_rect()
      self.rect.x = player.rect.x + 40
      self.rect.y = player.rect.y -30
    def update(self):
       canvas.blit(self.image, (self.rect.x, self.rect.y))
class Enemy(pygame.sprite.Sprite):
    def __init__(self,image):
      super().__init__()
      self.image = pygame.transform.scale(pygame.image.load(image), (50, 50))
      self.rect = self.image.get_rect()
      self.rect.x = random.randint(0,450)
      self.rect.y = 0
    def update(self):
       canvas.blit(self.image, (self.rect.x, self.rect.y))
player = Player('spaceship.png')
previous_time = pygame.time.get_ticks()
game_mode = 'play'
while not exit:
    current_time = pygame.time.get_ticks()
    collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
    collided_asteroids = pygame.sprite.spritecollide(player, asteroids, False)
    for i in collided_enemies:
        points += 1
        txt_points = font.render(str(points), True, (0, 255, 0))
        print(points)
        i.kill()
    if collided_asteroids:
        game_mode = 'lose'
    canvas.blit(bg, (0, 0))
    if game_mode == 'play':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rect.x -= 1
        if keys[pygame.K_RIGHT]:
            player.rect.x += 1
        if current_time - previous_time > 1000:
            previous_time = current_time
           #bullet = Bullet(player)
           #bullets.add(bullet)
            asteroid_probability = random.randint(0,10)
            if asteroid_probability == 9:
                enemy = Enemy('asteroid.png')
                asteroids.add(enemy)
            else:
                enemy = Enemy('enemys.png')
                enemies.add(enemy)
       #for i in bullets:
          #canvas.blit(i.image, (i.rect.x, i .rect.y))
           #i.rect.y -= 5
        for i in enemies:
          #canvas.blit(i.image, (i.rect.x, i .rect.y))
            i.rect.y += 5
        for i in asteroids:
           # canvas.blit(i.image, (i.rect.x, i .rect.y))
            i.rect.y += 3
        player.show()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
   #bullets.update()
    canvas.blit(txt_points, (canvas.get_width()-40, 50))
    enemies.update()
    asteroids.update()
    bullets.update()
    pygame.display.update()
    clock.tick(120)
