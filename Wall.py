#this load lines of the game
import pygame, sys, math
from Ball import *
from Block import *

class Wall():
    def __init__(self, pos=[25,25]):
        self.image = pygame.image.load("images/blocks/Red.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "wall"
                
        self.widthInCells = 10
        self.heightInCells = 16
        self.groups = []
        self.curCell = [0,0]
        colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
        colorNum = 0
        color = colors[colorNum]
        group = [Block([self.curCell[0]*50, self.curCell[1]*50]), color]
        
    def getDist(self, other):
        x1 = self.rect.centerx
        x2 = other.rect.centerx
        y1 = self.rect.centery
        y2 = other.rect.centery
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
     
    def moveUp(self):
        self.rect = self.rect.move([0,-50])

    
    
    def ballCollide(self, other):
        if self != other:
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top:
                        if self.rect.top < other.rect.bottom:
                            self.living = False
                            return True
        return False
