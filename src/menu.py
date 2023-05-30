import os, pygame
from src.constants import *
from src.window import window

os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()

def drawMenu():
    font = pygame.font.SysFont("monospace", 50, True)

    title = "Tic Tac Toe"
    label = font.render(title, False, TITLE_COLOR)
    window.blit(label, ((SCREEN_WIDTH - label.get_width()) / 2, TITLE_Y))

    pygame.draw.rect(window, RECT_COLOR, RECT_1)
    pygame.draw.rect(window, RECT_COLOR, RECT_2)

    font = pygame.font.SysFont("monospace", 20, True)

    title = "PvE"
    label = font.render(title, False, PVE_COLOR)
    window.blit(label, ((SCREEN_WIDTH - label.get_width()) / 2, RECT_MID_1 - label.get_height() / 2))

    title = "PvP"
    label = font.render(title, False, PVP_COLOR)
    window.blit(label, ((SCREEN_WIDTH - label.get_width()) / 2, RECT_MID_2 - label.get_height() / 2))
