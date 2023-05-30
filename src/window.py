import pygame
from src.constants import *

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(BG)
pygame.display.set_caption("Tic Tac Toe")

def drawGrid(font, player_1_wins, player_2_wins):
    score = f"Player 1 : {player_1_wins}    Player 2 : {player_2_wins}"
    label = font.render(score, False, TEXT_COLOR)
    window.blit(label, TEXT_POINT)

    pygame.draw.line(
        window,
        GRID_COLOR,
        (SIDE_BUFFER + (BOARD_SIZE / 3), TOP_BUFFER),
        (SIDE_BUFFER + (BOARD_SIZE / 3), SCREEN_HEIGHT - BOTTOM_BUFFER),
        GRID_WIDTH
    )

    pygame.draw.line(
        window,
        GRID_COLOR,
        (SIDE_BUFFER + 2 * (BOARD_SIZE / 3), TOP_BUFFER),
        (SIDE_BUFFER + 2 * (BOARD_SIZE / 3), SCREEN_HEIGHT - BOTTOM_BUFFER),
        GRID_WIDTH
    )

    pygame.draw.line(
        window,
        GRID_COLOR,
        (SIDE_BUFFER, TOP_BUFFER + (BOARD_SIZE / 3)),
        (SCREEN_WIDTH - SIDE_BUFFER, TOP_BUFFER + (BOARD_SIZE / 3)),
        GRID_WIDTH
    )

    pygame.draw.line(
        window,
        GRID_COLOR,
        (SIDE_BUFFER, TOP_BUFFER + 2 * (BOARD_SIZE / 3)),
        (SCREEN_WIDTH - SIDE_BUFFER, TOP_BUFFER + 2 * (BOARD_SIZE / 3)),
        GRID_WIDTH
    )

def getRow(posY):
    if posY >= TOP_BUFFER and posY < TOP_BUFFER + (BOARD_SIZE / 3):
        return 0
    elif posY >= TOP_BUFFER + (BOARD_SIZE / 3) and posY < TOP_BUFFER + 2 * (BOARD_SIZE / 3):
        return 1
    return 2

def getCol(posX):
    if posX >= SIDE_BUFFER and posX < SIDE_BUFFER + (BOARD_SIZE / 3):
        return 0
    elif posX >= SIDE_BUFFER + (BOARD_SIZE / 3) and posX < SIDE_BUFFER + 2 * (BOARD_SIZE / 3):
        return 1
    return 2
