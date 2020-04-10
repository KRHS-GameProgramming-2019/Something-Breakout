import math, pygame, random
from LevelLoader import *
from Block import *


class Pieces():
    def __init__(self):
        self.blocks = []
        self.blockTimer = 0
        self.blockTimerMax = 60*3
        self.pieces = []
    
    def loadBlocks(self, level):
        self.blocks = loadLevel("levels/"+str(level)+".lvl")
        self.findPieces()
        
    def findPieces(self):
        self.pieces = []
        
    def moveUp(self):
        for block in self.blocks:
            block.moveUp()
        
