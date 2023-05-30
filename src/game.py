import sys
sys.path.insert(0, 'package/')

import os, pygame, random, time
from src.constants import *
from src.menu import drawMenu
from src.window import window, drawGrid, getRow, getCol
from src.board import Board, drawBoard
from src.ai import makeMove
from src.game_over import gameOver, drawWinMessage, drawMessage

os.environ['SDL_AUDIODRIVER'] = 'dsp'

pygame.init()

font = pygame.font.SysFont("monospace", 20)
board = Board()
player = 1
player_1_wins = 0
player_2_wins = 0
is_ai_opponent = True
difficulty = 0

def switchPlayer():
    if player == 1:
        return 2
    return 1

def updateGame(row, col):
    global player, player_1_wins, player_2_wins

    board.markCell(row, col, player)
    board_state = board.checkBoardState()

    if board_state != 0:
        gameOver(board, player, font, player_1_wins, player_2_wins)
        gameEnd(board_state)

    player = switchPlayer()

def menu():
    global is_ai_opponent, difficulty

    window.fill(BG)

    while True:
        drawMenu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posX = event.pos[0]
                posY = event.pos[1]

                if posX >= RECT_1[0] and posX <= RECT_1[0] + RECT_1[2] and\
                   posY >= RECT_1[1] and posY <= RECT_1[1] + RECT_1[3]:
                    is_ai_opponent = True
                    difficulty = random.randint(0, 2)
                    game()

                elif posX >= RECT_2[0] and posX <= RECT_2[0] + RECT_2[2] and\
                   posY >= RECT_2[1] and posY <= RECT_2[1] + RECT_2[3]:
                    is_ai_opponent = False
                    game()

        pygame.display.update()

def game():
    global board, player, player_1_wins, player_2_wins

    window.fill(BG)
    board = Board()
    player = 1

    while True:
        drawGrid(font, player_1_wins, player_2_wins)
        drawBoard(board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif player == 2 and is_ai_opponent:
                row, col = makeMove(board, difficulty)
                updateGame(row, col)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                posX = event.pos[0]
                posY = event.pos[1]

                if posX >= SIDE_BUFFER and posX <= SCREEN_WIDTH - SIDE_BUFFER and\
                    posY >= TOP_BUFFER and posY <= SCREEN_HEIGHT - BOTTOM_BUFFER:
                    row = getRow(posY)
                    col = getCol(posX)
                    if not board.isCellMarked(row, col):
                        updateGame(row, col)

        pygame.display.update()

def gameEnd(board_state):
    pygame.display.update()
    time.sleep(1)

    while True:
        global player

        if board_state == -1:
            drawMessage()
        else:
            drawWinMessage(player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                menu()

        pygame.display.update()
