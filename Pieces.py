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
        for lineNum, line in enumerate(self.blocks):
            piece=[]
            curKind=None
            for blockNum, block in enumerate(line):
                if not curKind:         #start of line
                    if lineNum == 0:    #first block
                        curKind = block.kind
                        piece += [block]
                        block.piece = piece
                    else:
                        if self.blocks[lineNum - 1][blockNum].kind == block.kind:
                            self.blocks[lineNum - 1][blockNum].piece += [block]
                            block.piece = self.blocks[lineNum - 1][blockNum].piece
                            piece = block.piece
                            curKind = block.kind
                        else:
                            curKind = block.kind
                            piece += [block]
                            block.piece = piece
                else:
                    if curKind == block.kind:
                        if self.blocks[lineNum - 1][blockNum].kind == block.kind:
                            self.blocks[lineNum - 1][blockNum].piece += [block]
                            block.piece = self.blocks[lineNum - 1][blockNum].piece
                            piece = block.piece
                            curKind = block.kind
                        else:
                            piece += [block]
                            block.piece = piece
                        
        
