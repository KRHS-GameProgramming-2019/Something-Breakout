from Ball import *

class Block():
    def __init__(self, startPos=[0,0], color="blue"):
        if color == "blue":
            self.image = pygame.image.load("images/blocks/blue.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "blue"
        if color == "red":
            self.image = pygame.image.load("images/blocks/Red.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "red"
        if color == "orange":
            self.image = pygame.image.load("images/blocks/Orange.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "orange"
        if color == "yellow":
            self.image = pygame.image.load("images/blocks/Yellow.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "yellow"
        if color == "green":
            self.image = pygame.image.load("images/blocks/Green.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "green"
        if color == "purple":
            self.image = pygame.image.load("images/blocks/Purple.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "purple"
        if color == "pink":
            self.image = pygame.image.load("images/blocks/Pink.png")
            self.rect = self.image.get_rect(topleft = startPos)
            self.kind = "pink"
            
self.shape = None

        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
     
    def moveUp(self):
        self.rect = self.rect.move([0,-50])

    def __str__(self):
        if self.kind == "blue":
            return "b"
        if self.kind == "red":
            return "r"
        if self.kind == "orange":
            return "o"
        if self.kind == "yellow":
            return "y"
        if self.kind == "green":
            return "g"
        if self.kind == "purple":
            return "p"
        if self.kind == "pink":
            return "k"
    
    
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            self.living = False
                            return True
        return False
