#This will be the main game loop. Function and Classes will be outsourced from here
import pygame, sys, math, random
from Ball import *
from Hud import *
from Platform import *
from Hud import *
from Block import *
pygame.init()
if not pygame.font: print("Warning, fonts disabled")

clock = pygame.time.Clock();

size = [1000, 900]
screen = pygame.display.set_mode(size)




# += [Ball(pics[random.randint(0, len(pics)-1)], 
                #[random.randint(-7,7), random.randint(-7,7)],
                #[random.randint(100, 800), random.randint(100, 500)])
        #]       

counter = 1;
player = Platform(4, [1600/2, 800])
ball = Ball(5,-45, [900/2,100])
balls = [player, ball]
block = (4, [1600/2, 800])
score = Hud("Score: ", [0,0])
timer = Hud("Time: ",[1000-200, 0])
deaths= Hud("Deaths: ",[1600-180,0])

crash_sound = pygame.mixer.Sound("welcome.wav")
pygame.mixer.music.load('welcome.wav')
pygame.mixer.music.play(1)

kills = 0
time = 0

blocks = []
blockTimer = 120
blockTimerMax = 60*2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
            #if event.key == pygame.K_a or  event.key == pygame.K_LEFT:
                #player.goKey("left")
            #elif event.key == pygame.K_d or  event.key == pygame.K_RIGHT:
                #player.goKey("right")
        #elif event.type == pygame.KEYUP:
            #if event.key == pygame.K_a or  event.key == pygame.K_LEFT:
                #player.goKey("sleft")
            #elif event.key == pygame.K_d or  event.key == pygame.K_RIGHT:
                #player.goKey("sright")
        elif event.type == pygame.MOUSEMOTION:
            player.goMouse(event.pos)
    time += 1
    
    
    if blockTimer < blockTimerMax:
        blockTimer += 1
    else:
        blockTimer = 0
        for block in blocks:
            block.moveUp()
        for i in range(10):
            blocks += [Block([i*100, 900-50])]
            
    for block in blocks:
        if block.ballCollide(ball):
            blocks.remove(block)
            ball.sqCollide(block)
    
            
    ball.update(size)
    ball.sqCollide(player)
    timer.update(int(time/60  ))
    score.update(kills)
   
            
            
            
    screen.fill((100, 100, 100))
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    for block in blocks:
        screen.blit(block.image, block.rect)
    screen.blit(score.image, score.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)
#   print(clock.get_fps())
