#This will be the main game loop. Function and Classes will be outsourced from here
import pygame, sys, math, random
from Ball import *
from Platform import *
from Hud import *
from Block import *
pygame.init()
if not pygame.font: print("Warning, fonts disabled")

clock = pygame.time.Clock();

size = [900, 700]
screen = pygame.display.set_mode(size)

pics = ["images/gameBall/ball.png",
        "Images/gameBall/PYGameBall.png"
 

]



#balls += [Ball(pics[random.randint(0, len(pics)-1)], 
                #[random.randint(-7,7), random.randint(-7,7)],
                #[random.randint(100, 800), random.randint(100, 500)])
         #]       

counter = 0;
player = PlayerBall(4, [900, 700])
balls = [player]
score = Hud("Score: ", [0,0])
timer = Hud("Time: ",[900-200, 0])

kills = 0
time = 0

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
    counter += 1
    if counter >= 10:
        counter = 0;
        balls += [Ball([random.randint(-7,7), random.randint(-7,7)],
                [random.randint(100, 700), random.randint(100, 500)])
        ]
        for ball in balls:
            if balls[-1].ballCollide(ball):
                balls.remove(balls[-1])
                break
            
    for ball in balls:
        ball.update(size)
        
    timer.update(int(time/60))
    score.update(kills)
        
    for hittingBall in balls:
        for hitBall in balls:
            if hittingBall.ballCollide(hitBall):
                if hittingBall.kind == "player":
                    balls.remove(hitBall)
                    kills += 1
            
            
            
    screen.fill((100, 100, 100))
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(score.image, score.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    clock.tick(60)
    print(clock.get_fps())
