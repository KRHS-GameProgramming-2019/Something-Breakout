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
        for x, c in enumerate(line):
            if c == "b":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "blue")]
            if c == "r":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "red")]
            if c == "k":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "purple")]
            if c == "o":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "orange")]
            if c == "y":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "yellow")]
            if c == "g":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "green")]
            if c == "p":
                tiles += [Block([x*size+offset, y*size+offset+yshift], "pink")]
            print(c, end="")
            
    
    return tiles
    
