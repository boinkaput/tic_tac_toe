import pygame, itertools
from src.constants import *
from src.window import window, drawGrid
from src.board import drawBoard

def gameOver(board, player, font, player_1_wins, player_2_wins):
    drawGrid(font, player_1_wins, player_2_wins)
    drawBoard(board)

    drawWinLine(board, player)

def drawWinLine(board, player):
    win_info = board.getWinInfo()

    if not win_info["type"]:
        return

    if win_info["type"] == "row":
        x = 0
        for x in range(BASE_CELL_CENTER_X - TOP_BUFFER + 1, BASE_CELL_CENTER_X + (N_COLS - 1) * (BOARD_SIZE // 3) + TOP_BUFFER + 1, WIN_LINE_DRAW_SPEED):
            pygame.draw.line(
                window,
                LINE_COLOR if player == 1 else CIRCLE_COLOR,
                (BASE_CELL_CENTER_X - TOP_BUFFER, BASE_CELL_CENTER_Y + win_info["index"] * (BOARD_SIZE / 3)),
                (x, BASE_CELL_CENTER_Y + win_info["index"] * (BOARD_SIZE / 3)),
                WIN_LINE_WIDTH
            )
            pygame.display.update()
    elif win_info["type"] == "col":
        y = 0
        for y in range(BASE_CELL_CENTER_Y - TOP_BUFFER + 1, BASE_CELL_CENTER_Y + (N_ROWS - 1) * (BOARD_SIZE // 3) + TOP_BUFFER + 1, WIN_LINE_DRAW_SPEED):
            pygame.draw.line(
                window,
                LINE_COLOR if player == 1 else CIRCLE_COLOR,
                (BASE_CELL_CENTER_X + win_info["index"] * (BOARD_SIZE / 3), BASE_CELL_CENTER_Y - TOP_BUFFER),
                (BASE_CELL_CENTER_X + win_info["index"] * (BOARD_SIZE / 3), y),
                WIN_LINE_WIDTH
            )
            pygame.display.update()
    elif win_info["type"] == "left_d":
        for x, y in itertools.zip_longest(
            range(BASE_CELL_CENTER_X - TOP_BUFFER + 1, BASE_CELL_CENTER_X + (N_COLS - 1) * (BOARD_SIZE // 3) + TOP_BUFFER + 1, WIN_LINE_DRAW_SPEED),
            range(BASE_CELL_CENTER_Y - TOP_BUFFER + 1, BASE_CELL_CENTER_Y + (N_ROWS - 1) * (BOARD_SIZE // 3) + TOP_BUFFER + 1, WIN_LINE_DRAW_SPEED)
        ):
            pygame.draw.line(
                window,
                LINE_COLOR if player == 1 else CIRCLE_COLOR,
                (BASE_CELL_CENTER_X - TOP_BUFFER, BASE_CELL_CENTER_Y - TOP_BUFFER),
                (x, y),
                WIN_LINE_WIDTH
            )
            pygame.display.update()
    else:
        for x, y in itertools.zip_longest(
            range(BASE_CELL_CENTER_X + (N_COLS - 1) * (BOARD_SIZE // 3) + TOP_BUFFER - 1, BASE_CELL_CENTER_X - TOP_BUFFER - 1, -WIN_LINE_DRAW_SPEED),
            range(BASE_CELL_CENTER_Y - TOP_BUFFER + 1, BASE_CELL_CENTER_Y + (N_ROWS - 1) * (BOARD_SIZE // 3) + TOP_BUFFER + 1, WIN_LINE_DRAW_SPEED)
        ):
            pygame.draw.line(
                window,
                LINE_COLOR if player == 1 else CIRCLE_COLOR,
                (BASE_CELL_CENTER_X + (N_COLS - 1) * (BOARD_SIZE / 3) + TOP_BUFFER, BASE_CELL_CENTER_Y - TOP_BUFFER),
                (x, y),
                WIN_LINE_WIDTH
            )
            pygame.display.update()

def drawWinMessage(player):
    window.fill(BG)
    pygame.init()

    font = pygame.font.SysFont("monospace", 70, True)

    message = f"Player {player} won!!"
    label = font.render(message, False, LINE_COLOR if player == 1 else CIRCLE_COLOR)
    window.blit(label, ((SCREEN_WIDTH - label.get_width()) / 2, ((SCREEN_HEIGHT - label.get_height()) / 2)))

    clickToContinue()

def drawMessage():
    window.fill(BG)
    pygame.init()

    font = pygame.font.SysFont("monospace", 60, True)

    message = "Game is a draw!!"
    label = font.render(message, False, DRAW_MESSAGE_COLOR)
    window.blit(label, ((SCREEN_WIDTH - label.get_width()) / 2, ((SCREEN_HEIGHT - label.get_height()) / 2)))

    clickToContinue()

def clickToContinue():
    pygame.init()

    font = pygame.font.SysFont("monospace", 20, True)

    message = "Click to continue..."
    label = font.render(message, False, CLICK_MESSAGE_COLOR)
    window.blit(label, ((SCREEN_WIDTH - label.get_width()) / 2, 500))
