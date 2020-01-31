# This is our ball 
import pygame, sys, math, random
class Ball():
    def __init__(self, speed = [0,0], startPos=[0,0]):
        self.images = [pygame.image.load("images/gameBall/OrangeBall.png")]
        self.frame = 0
        self.frameMax = len(self.images) -1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rad = (self.rect.height/2 + self.rect.width/2)/2

        self.rect = self.rect.move(startPos)
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.kind = "ball"
        self.animationTimer = 0
        self.animationTimerMax = 60/1
     
    def update(self, size):
        self.move()
        self.wallCollide(size)
        self.animate()
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def animate(self):
        self.animationTimer += 1
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 0
            if self.frame >= self.frameMax:
                self.frame = 0
            else:
                self.frame += 1
            self.image = self.images[self.frame]

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
            if self.rect.top < 0:
                #TopCollide= TopCollide+1
                self.speedy = -self.speedy
                self.didBounceY = True
        if not self.didBounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.didBounceX = True
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                if not self.didBounceX:
                                    self.speedx = -15
                                    self.didBounceX = True
                                if not self.didBounceY:
                                    self.speedy = -self.speedy
                                    self.didBounceY = True
                                return True
        return False

    def sqCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            #------HIT---------
                            if self.speedy > 0 and self.speedx > 0: # heading down right
                                xdiff = other.rect.top - self.rect.centery
                                ydiff = other.rect.left - self.rect.centerx
                                if xdiff >= ydiff:
                                    if not self.didBounceX:
                                        self.speedx = -self.speedx
                                        self.didBounceX = True
                                else:
                                    if not self.didBounceY:
                                        self.speedy = -self.speedy
                                        self.didBounceY = True
                            if self.speedy > 0 and self.speedx < 0: # heading down left
                                xdiff = abs(other.rect.top - self.rect.centery)
                                ydiff = abs(other.rect.right - self.rect.centerx)
                                if xdiff >= ydiff:
                                    if not self.didBounceX:
                                        self.speedx = -self.speedx
                                        self.didBounceX = True
                                else:
                                    if not self.didBounceY:
                                        self.speedy = -self.speedy
                                        self.didBounceY = True      
                            if self.speedy < 0 and self.speedx > 0: # heading up right
                                xdiff = other.rect.top - self.rect.centery
                                ydiff = other.rect.left - self.rect.centerx
                                if xdiff >= ydiff:
                                    if not self.didBounceX:
                                        self.speedx = -self.speedx
                                        self.didBounceX = True
                                else:
                                    if not self.didBounceY:
                                        self.speedy = -self.speedy
                                        self.didBounceY = True
                            if self.speedy < 0 and self.speedx < 0: # heading up left
                                xdiff = abs(other.rect.top - self.rect.centery)
                                ydiff = abs(other.rect.right - self.rect.centerx)
                                if xdiff >= ydiff:
                                    if not self.didBounceX:
                                        self.speedx = -self.speedx
                                        self.didBounceX = True
                                else:
                                    if not self.didBounceY:
                                        self.speedy = -self.speedy
                                        self.didBounceY = True  
                        
                                
                                    
                                return True
        return False
        

                             
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2) 
