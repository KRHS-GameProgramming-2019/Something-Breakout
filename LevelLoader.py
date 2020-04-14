#this loads the tetris like levels.
import pygame, sys, math
from Wall import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = 0
    tiles = []
    
    yshift = 17*size
    
    # ~ newLines = []
    # ~ for line in lines:
        # ~ newLine = ""
        # ~ for c in lines:
            # ~ if c != "\n":
                # ~ newLine += c
        # ~ newLines += [newLine]
    # ~ lines = newLines
    
    
   
    
    
    for y, line in enumerate(lines):
        newLine=[]
        for x, c in enumerate(line):
            if c == "b":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "blue")]
            if c == "r":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "red")]
            if c == "p":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "purple")]
            if c == "o":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "orange")]
            if c == "y":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "yellow")]
            if c == "g":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "green")]
            if c == "k":
                newLine += [Block([x*size+offset, y*size+offset+yshift], "pink")]
        tiles+=[newLine]
            
            
    
    return tiles
    
