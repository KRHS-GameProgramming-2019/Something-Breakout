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
                print("a. " + str(block))
                if not curKind:         #start of line
                    print(" b. No currKind")
                    if lineNum == 0:    #first block
                        print("  c. First Block")
                        curKind = block.kind
                        piece += [block]
                        block.piece = piece
                    else:               #first block of new line
                        #the one above us is like us
                        print("  c. Not First Block")
                        if self.blocks[lineNum - 1][blockNum].kind == block.kind:  
                            print("   d. Match Above")
                            self.blocks[lineNum - 1][blockNum].piece += [block]
                            block.piece = self.blocks[lineNum - 1][blockNum].piece
                            piece = block.piece
                            curKind = block.kind
                        else:       #the one above us is NOT like us
                            print("   d. No Match Above")
                            curKind = block.kind
                            piece += [block]
                            block.piece = piece
                elif curKind == block.kind:     #the one to the left is like us
                    print(" b. currKind: " + curKind)
                    if lineNum == 0: #top line special case
                        print("  c. Top Row")
                        piece += [block]
                        block.piece = piece
                    else:  # the rest of the lines
                        # the one above us is like us
                        print("  c. Not Top Row")
                        if self.blocks[lineNum - 1][blockNum].kind == block.kind:
                            print("   d. Match Above")
                            self.blocks[lineNum - 1][blockNum].piece += [block]
                            block.piece = self.blocks[lineNum - 1][blockNum].piece
                            piece = block.piece
                            curKind = block.kind
                        else:       #the one above us is NOT like us
                            print("   d. No Match Above")
                            curKind = block.kind
                            piece += [block]
                            block.piece = piece
                            
                else: # the one to the left is NOT like us
                    print(" b. kinds: " + curKind + " vs. " + block.kind)
                    if piece not in self.pieces: #Store the previous piece pieces
                        print("-------Break " + piece[0].kind + " Piece Off------")
                        self.pieces += [piece]
                    piece = []
                    if lineNum == 0: #top line special case
                        print("  c. Top Row")
                        curKind = block.kind
                        piece += [block]
                        block.piece = piece
                    else: 
                        print("  c. Not Top Row")
                        #the one above us is like us
                        if self.blocks[lineNum - 1][blockNum].kind == block.kind:  
                            print("   d. Match Above")
                            self.blocks[lineNum - 1][blockNum].piece += [block]
                            block.piece = self.blocks[lineNum - 1][blockNum].piece
                            piece = block.piece
                            curKind = block.kind
                        else:       #the one above us is NOT like us
                            print("   d. No Match Above")
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
        for line in self.blocks:
            for block in line:
                block.moveUp()
        
