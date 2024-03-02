from pygame import*
init()

Clock = time.Clock()


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


game_mode = "play"

class Pong(GameSprite):
    def update(self):
        self.rect_x += self.speed
        self.rect_y += self.speed
        

speed_x = 3
speed_y = 3

player_l = Player("palyer_l_image.png", 100, 100 ,10, 80, 50 )
player_r = Player("palyer_r_image.png", 100, 100, 10, 80, 50)
pong = Pong("pong.png",100,100, 50,50 ,5, 5)

win_wight = 80
win_height = 50






while game_mode :
    if "Finish" != True:
        pong.rect.x += speed_x
        pong.rect.y += speed_y
    if sprite.collide_rect(player_l, pong):
        sprite.collide_rect(player_r, pong)  
        speed_x *= -1
        if pong.rect_y >= win_height - 80 or pong.rect_y < 0:
            speed_y *= -1
            pong.update(speed_x,speed_y)


while exit != True:
    for e in event.get():
        if e.type == QUIT:

            exit = True
        window.blit(color, (0, 0))
        if finish != True:
            if sprite.collide_rect(player_l, pong) or sprite.collide_rect(player_r, pong):
                speed_x *= -1
            if pong.rect_y > win_height - 80 or pong.rect.y < -50:
                speed_y*-1
            if pong.rect_x < 8:
                lose = font.render('PLAYER 1 LOSE!', True, (180, 0, 0))
                finish = True
            if pong.rect_x > win_wight:
                finish = True
                lose = font.render('PLAYER 2 LOSE!', True, (180, 0, 0))
            pong.update(speed_x, speed_y)
            player_l.update_l()
            player_r.update_r()
    Clock.tick(60)


