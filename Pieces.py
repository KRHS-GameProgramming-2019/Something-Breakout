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
                elif curKind == block.kind:
                    if lineNum == 0: 
                        piece += [block]
                        block.piece = piece
                    else: 
                        if self.blocks[lineNum - 1][blockNum].kind == block.kind:
                            self.blocks[lineNum - 1][blockNum].piece += [block]
                            block.piece = self.blocks[lineNum - 1][blockNum].piece
                            piece = block.piece
                            curKind = block.kind
                        else:
                            piece += [block]
                            block.piece = piece
                else:
                    if piece not in self.pieces:
                        self.pieces += [piece]
                    piece = []
                    if lineNum == 0:
                        curKind = block.kind
                        piece += [block]
                        block.piece = piece
            if piece not in self.pieces:
                self.pieces += [piece]
        print (str(self))
        
    def __str__ (self):
        out = "-----------\n"
        for i in self.pieces:
            for j in i:
                out += str(j) + "\n"
            out += "\n"
        out += ">>>>>>>>\n"
        for piece in self.pieces:
            if len (piece) > 0:
                out += piece [0].kind + " piece, size: " + str(len(piece)) + "\n"
        out += "--------\n\n"
        return out
                        
        
    def moveUp(self):
        for block in self.blocks:
            block.moveUp()
        
