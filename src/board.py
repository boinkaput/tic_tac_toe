import pygame, copy
from src.constants import *
from src.window import window

def drawBoard(board):
    for i, row in enumerate(board.board):
        for j, cell in enumerate(row):
            if cell == 1:
                drawX(i, j)
            elif cell == 2:
                drawO(i, j)

def drawX(row, col):
    line_start_1 = (BASE_LINE_X + col * (BOARD_SIZE / 3), BASE_LINE_Y + row * (BOARD_SIZE / 3))
    line_end_1 = (line_start_1[0] + LINE_BUFFER, line_start_1[1] + LINE_BUFFER)
    line_start_2 = (line_end_1[0], line_start_1[1])
    line_end_2 = (line_start_1[0], line_end_1[1])
    pygame.draw.line(window, LINE_COLOR, line_start_1, line_end_1, LINE_WIDTH)
    pygame.draw.line(window, LINE_COLOR, line_start_2, line_end_2, LINE_WIDTH)

def drawO(row, col):
    center = (BASE_CIRCLE_CENTER_X + col * (BOARD_SIZE / 3), BASE_CIRCLE_CENTER_Y + row * (BOARD_SIZE / 3))
    pygame.draw.circle(window, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

class Board(object):
    def __init__(self, board = None):
        if not board:
            self.board = [[0 for i in range(N_COLS)] for j in range(N_ROWS)]
        else:
            self.board = copy.deepcopy(board)

        self.winInfo = {"type": None, "index": -1}

    def getWinInfo(self):
        return self.winInfo

    def isCellMarked(self, row, col):
        return self.board[row][col] != 0

    def markCell(self, row, col, player):
        self.board[row][col] = player

    def checkBoardState(self):
        board_state = self.checkWin()
        if board_state != 0:
            return board_state

        return self.checkDraw()

    def checkWin(self):
        # Check rows
        for i, row in enumerate(self.board):
            if row[0] != 0 and row.count(row[0]) == len(row):
                self.winInfo["type"] = "row"
                self.winInfo["index"] = i
                return row[0]

        # Check cols
        col = 0
        for col in range(N_COLS):
            column = [self.board[row][col] for row in range(N_ROWS)]
            if column[0] != 0 and column.count(column[0]) == len(column):
                self.winInfo["type"] = "col"
                self.winInfo["index"] = col
                return column[0]

        # Check left diagonal
        left_diagonal = [self.board[i][i] for i in range(N_ROWS)]
        if left_diagonal[0] != 0 and left_diagonal.count(left_diagonal[0]) == len(left_diagonal):
            self.winInfo["type"] = "left_d"
            self.winInfo["index"] = 0
            return left_diagonal[0]

        # Check right diagonal
        right_diagonal = [self.board[i][N_COLS - 1 - i] for i in range(N_ROWS)]
        if right_diagonal[0] != 0 and right_diagonal.count(right_diagonal[0]) == len(right_diagonal):
            self.winInfo["type"] = "right_d"
            self.winInfo["index"] = 0
            return right_diagonal[0]

        return 0

    def checkDraw(self):
        row = 0
        for row in range(N_ROWS):
            col = 0
            for col in range(N_COLS):
                if self.board[row][col] == 0:
                    return 0

        return -1
