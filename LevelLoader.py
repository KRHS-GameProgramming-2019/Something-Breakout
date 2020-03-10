import pygame, sys, math
from Wall import *

def loadLevel(lev):
    f = open(lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/2
    tiles = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in lines:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines
   
    
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                tiles += [Wall([x*size+offset, y*size+offset])]
    
    return tiles
    
loadLevel("levels/1.lvl")
