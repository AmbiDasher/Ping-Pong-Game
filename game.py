from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect < win_height - 80:
            self.rect.y += self.speed
            
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect < win_height - 80:
            self.rect.y += self.speed
            
background_color = (0, 102, 51)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background_color)

game = True
finish = False
clock = time.Clock()
fps = 60

racket1 = Player("Racket(PPG).png", 30, 200, 4, 50, 150)
racket2 = Player("Racket(PPG).png", 520, 200, 4, 50, 150)
ball = Player("RacketBall(PPG).png", 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        racket1.reset()
        racket2.reset()
        ball.reset()
    display.update()
    clock.tick(fps)
