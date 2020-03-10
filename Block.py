    #this will be the class block
from Ball import *

class Block():
    def __init__(self, startPos=[0,0], color="blue"):
        if color == "1":
            self.image = pygame.image.load("images/blocks/blue.png")
        self.rect = self.image.get_rect(topleft = startPos)
        self.kind = "blue"
        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
     
    def moveUp(self):
        self.rect = self.rect.move([0,-50])

    1=blue
    2=red
    3=green
    4=yellow
    5=orange
    
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            self.living = False
                            return True
        return False
