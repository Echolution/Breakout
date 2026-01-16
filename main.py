import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,800))

font = pygame.font.Font(None, 80)

class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100,250),random.randrange(100,250),random.randrange(100,250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100, 50))

    def collide(self, ball_x, ball_y):
        if not self.isDead:
            if (ball_x + ball_size > self.xpos and ball_x < self.xpos + 100 and ball_y + ball_size > self.ypos and ball_y < self.ypos + 50):
                self.isDead = True
                return True
            return False

#game veriables
xpos = 0
ypos = 800
px = 800
ball_x = 400
ball_y = 400
ball_size = 30
bVx = 0.35
bVy = 0.35
pScore = 0
life = 3

b0 = brick(0,50)
b1 = brick(100,100)
b2 = brick(200,50)
b3 = brick(300,100)
b4 = brick(400,50)
b5 = brick(500,100)
b6 = brick(600,50)
b7 = brick(700,100)
b8 = brick(0,150)
b9 = brick(200,150)

#Run, Run
running = True
while running: #Game loop
    
    #imput section-------------------------------------------
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
        if life == 0:
            running = False
            
    if px < 0: #hit top
        px = 0 #stop moving
    if px > 680:
        px = 680
            
    keys = pygame.key.get_pressed() #keybord state
    if keys[pygame.K_a]:
        px -= 0.35
    if keys[pygame.K_d]:
        px += 0.35
        
    #physics section-------------------------------------------
    if ball_x < 0 or ball_x > 800:
        bVx *=-1
    ball_x += bVx
    
    if ball_y < 0 or ball_y >800:
        bVy *=-1
    ball_y += bVy
    
    #if ball_y > 800:
    
    #ballxbrick
    if b0.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b1.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b2.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b3.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b4.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b5.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b6.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b7.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b8.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
        
    if b9.collide(ball_x, ball_y):
        bVy *=-1
        pScore+=1
    
    #Left paddle collision
    if bVy > 0 and ball_y+30 >= 763 and ball_y <= 770 and ball_x+30 >= px and ball_x <= px+120:
        bVy *= -1
    
    #render section-------------------------------------------
    screen.fill((0,0,0))
    b0.draw()
    b1.draw()
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    pygame.draw.rect(screen,(255,255,255),(px,750,120,20)) # Left paddle
    pygame.draw.rect(screen,(255,255,255),(ball_x,ball_y,20,20))# Ball
    add = font.render(str("Score: "), True, (255,255,255))
    pain = font.render(str("Lifes: "), True, (255,255,255))
    score = font.render(str(pScore), True, (255,255,255))
    lifes = font.render(str(life), True, (255,255,255))
    screen.blit(add, (20, 20))
    screen.blit(pain, (20, 75))
    screen.blit(score, (195, 25))
    screen.blit(lifes, (180, 78))
    
    pygame.display.flip()
pygame.quit()
