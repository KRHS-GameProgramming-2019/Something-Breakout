# This is our ball 
import pygame, sys, math, random
class Ball():
    def __init__(self, speed, angle, startPos=[0,0]):
        self.base_image = pygame.image.load("images/gameBall/ballGrey.PNG")
        self.image = self.base_image 
        self.rect = self.image.get_rect(topleft = startPos)
        self.speed = speed
        self.angle = angle
        self.speedx = math.cos(math.radians(self.angle))*self.speed
        self.speedy = -math.sin(math.radians(self.angle))*self.speed
        self.rad = (self.rect.height/2 + self.rect.width/1)/1

        self.pos = startPos
        
        self.rot_angle = self.angle
        rot_image = pygame.transform.rotate(self.base_image, self.rot_angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.kind = "ball"
        self.animationTimer = 0
        self.animationTimerMax = 60/1
        
        self.randomness = 10
       
     
#        Invoke("respawnMethodName", 5);

    def update(self, size):
        self.move()
        isDead = self.wallCollide(size)
        #self.animate()
        return isDead
        
    def move(self):
        #print ("Angle: ",self.angle)
        self.didBounceX = False
        self.didBounceY = False
        self.pos[0] += self.speedx
        self.pos[1] += self.speedy
        self.rect.center = self.pos
        
    #def animate(self):
        #if self.angle != self.rot_angle:
            #self.rot_angle = self.angle
            #rot_image = pygame.transform.rotate(self.base_image, self.rot_angle)
            #rot_rect = self.rect.copy()
            #rot_rect.center = rot_image.get_rect().center
            #rot_image = rot_image.subsurface(rot_rect)
            #self.image = rot_image

    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceY:
            if self.rect.bottom > height:
                self.angle = -self.angle + random.randint(-self.randomness,self.randomness)
                self.speedx = math.cos(math.radians(self.angle))*self.speed
                self.speedy = -math.sin(math.radians(self.angle))*self.speed
            if self.rect.top < 0:
                return True
        if not self.didBounceX:
            if self.rect.right > width:
                self.angle = -self.angle+180 +  random.randint(-self.randomness,self.randomness)
                self.speedx = math.cos(math.radians(self.angle))*self.speed
                self.speedy = -math.sin(math.radians(self.angle))*self.speed
            if self.rect.left < 0:
                self.angle = -self.angle+180 +  random.randint(-self.randomness,self.randomness)
                self.speedx = math.cos(math.radians(self.angle))*self.speed
                self.speedy = -math.sin(math.radians(self.angle))*self.speed
        return False
            
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
                            xdiff = abs(self.rect.centerx - other.rect.centerx)
                            if xdiff > other.rect.width/2: #Leftg/Right
                                self.angle = -self.angle+180
                                self.speedx = math.cos(math.radians(self.angle))*self.speed
                                self.speedy = -math.sin(math.radians(self.angle))*self.speed
                            else:
                                self.angle = -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               self.angle
                                self.speedx = math.cos(math.radians(self.angle))*self.speed
                                self.speedy = -math.sin(math.radians(self.angle))*self.speed
                            return True
        return False
        

                             
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2) 
