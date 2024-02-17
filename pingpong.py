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

class pong():
    def __init__(self, pong_x, pong_y, pong_collide):
        self.rect_x = pong_x
        self.rect_y = pong_y
        self.collide = pong_collide



while not exit:
    window.blit(color)
    if pong_x == 500 or -500:
        game_mode = "over"
        break

