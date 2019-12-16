import pygame, sys, math
# this will be the platform
from Ball import *

class PlayerBall(Ball):
    def __init__(self, maxSpeed=4, startPos=[450,700]):
        Ball.__init__(self, [0,0], startPos)
        self.frame = 0
        self.frameMax = len(self.images) -1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()

        self.maxSpeed = maxSpeed
        self.kind = "player"
        
    #def goKey(self, direction):
        #if direction == "left":
            #self.speedx = -self.maxSpeed
        #elif direction == "right":
            #self.speedx = self.maxSpeed
        #elif direction == "sleft":
            #self.speedx = 0
        #elif direction == "sright":
            #self.speedx = 0
    
    def goMouse(self, pos):
        self.rect.center = [pos[0], self.rect.center[1]]
        pygame.mouse.set_visible(False)
    
    def update(self, size):
        self.move()
        self.wallCollide(size)
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
            if self.rect.top < 0:
                self.speedy = -self.speedy
                self.move()
                self.speedy = 0
                self.didBounceY = True
        if not self.didBounceX:
            if self.rect.right > width:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
            if self.rect.left < 0:
                self.speedx = -self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True
            
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            if self.getDist(other) < self.rad + other.rad:
                                return True
        return False
