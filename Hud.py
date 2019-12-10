# This will be our heads up display, and will include most public values
import pygame, sys, math

class Hud():
    def __init__(self, baseText, startPos=[0,1]):
        pygame.font.get_fonts()
        pygame.font.match_font
        self.font = pygame.font.Font(None, 50)
        self.baseText = baseText
        self.image = self.font.render("Score: 0", 1, (0, 0, 0))
        self.rect = self.image.get_rect(topleft = startPos)
    def update(self, score):
        text = self.baseText + str(score)
        self.image = self.font.render(text , 1, (0, 0, 0))
        self.rect = self.image.get_rect(topleft = self.rect.topleft)
