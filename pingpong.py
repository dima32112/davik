from pygame import*
init()



class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect_x = player_x
        self.rect_y = player_y
    def reset(self):
        window.blit(self.image, (self.rect_y, self.rect_x))

class Player(GameSprite):
    def update_l (self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect_y -= self.speed
        if keys [K_s] and self.rect.y > 450:
            self.rect_y += self.speed
    
    def update_r(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect_y -= self.speed
        if keys [K_DOWN] and self.rect.y > 450:
            self.rect_y += self.speed




window = display.set_mode((500, 500))        
display.set_caption("pingpong")


color(27,27,27)
game_mode = "play"

class pong(GameSprite):
    def update(self):
        self.rect_x += self.speed
        self.rect_y += self.speed
        

speed_x = 3
speed_y = 3

player_l = Player("player_l_image.png", 100, 100 ,10, 80, 50 )
player_r = Player("palyer_r_image.png", 100, 100, 10, 80, 50)








while game_mode :
    if "Finish" != True:
        pong.rect_x += speed_x
        pong.rect_y += speed_y
    if sprite.collide_rect(racket1, pong):
        sprite.collide_rect(racket2, pong):
        speed_x *= -1
        if pong.rect_y > win_height - 80 or pong.rect_y < 0:
            speed_y *= -1
        pong.update(speed_x,speed_y)



    


while exit != True:
    for e in event.get():
        if e == QUIT:
            exit = True
        
        if sprite.collide_rect(player_l,pong) or sprite.collide:
            pong.speed_x *= -1
        window.blit(bg,(0, 0))
        player_l.update_l()
        player_l.reset()
        player_r.update()
        player_r.reset()
        pong.reset()
    else:
        display.update()
        clock.tick(FPS)

