from pygame import * 
from random import randint
mixer.init()

w = 700 
h = 500 
clock = time.Clock()
window = display.set_mode((w,h)) 
display.set_caption("Шутер") 
background = transform.scale(image.load("fon.jpg"),(w,h))  
patrons = sprite.Group()

lost = 0
score = 0

font.init()
font1 = font.Font(None, 60)
win = font1.render("YOU WIN!", True, (0,0,0))
lose = font1.render("YOU LOST!", True, (0,0,0))
score_text = font1.render(str(score), True,(250,250,250))
mixer.init()

class Player(sprite.Sprite): 
    def __init__(self, player_image, player_x, player_y,): 
        super().__init__() 
        self.image = transform.scale(image.load(player_image),(70,70)) 
        self.rect = self.image.get_rect() 
        self.rect.x = player_x 
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y)) 

class Hero(Player): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_RIGHT] and self.rect.y <= 620: 
            self.rect.y += 5
        if keys[K_LEFT] and self.rect.x >= 30: 
            self.rect.y -= 5
    def fire(self):
        b = Patron("pyl.png",self.rect.centerx,self.rect.top, 5)
        patrons.add(b)
class Patron(Player):
    def update(self):
        self.rect.y -= 5
        if self.rect.y < 0:
            self.kill()
class Enemy(Player): 
        direction = "right" 
        def update(self): 
            if self.rect.x <= randint(5,75): 
                self.direction = "right" 
            if self.rect.x >= randint(350,700): 
                self.direction = "left" 
            if self.direction == "left": 
                self.rect.x  -= 7
            if self.direction == "right": 
                self.rect.x  += 7


FPS = 60 
clock = time.Clock() 
game = True 
finish = False 
hero = Hero("asdf.png",200,400)
enemy = Enemy("fh.png",400,40)
patron = Patron("pyl.png",hero.rect.x,380)
while game: 
    for e in event.get():  
        if e.type == QUIT:  
            game = False 
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                hero.fire()
    if finish != True: 
        window.blit(background,(0,0)) 
        hero.update() #Змушуемо рухати гг
        patrons.update()
        enemy.update()  
        hero.reset() #Оновлюемо гг 
        enemy.reset()
        patrons.draw(window)
 


    display.update()
    clock.tick(FPS)
     