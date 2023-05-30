import math
from src.constants import *
from src.board import Board

minimax_scores = {
    "win": 1,
    "loss": -1,
    "draw": 0
}

def makeMove(board, difficulty):
    best_score = -math.inf
    best_move = (0, 0)

    for row in range(N_ROWS):
        for col in range(N_COLS):
            if not board.isCellMarked(row, col):
                new_board = Board(board.board)
                new_board.markCell(row, col, 2)
                new_score = minimax(new_board.board, getDifficultyScore(difficulty), False)
                if new_score > best_score:
                    best_score = new_score
                    best_move = (row, col)

    return best_move

def getDifficultyScore(difficulty):
    if difficulty == 0:
        return EASY_DEPTH
    elif difficulty == 1:
        return MEDIUM_DEPTH
    return HARD_DEPTH

def minimax(board, depth, maximizingPlayer):
    board_state = Board(board).checkBoardState()

    if depth == 0:
        board_state = -1

    if board_state != 0:
        if board_state == -1:
            return minimax_scores["draw"]
        else:
            return minimax_scores["win"] if board_state == 2 else minimax_scores["loss"]

    empty_positions = [(row, col) for row in range(N_ROWS) for col in range(N_COLS) if board[row][col] == 0]

    if maximizingPlayer:
        score = -math.inf
        for position in empty_positions:
            new_board = Board(board)
            new_board.markCell(position[0], position[1], 2)
            score = max(score, minimax(new_board.board, depth - 1, False))
        return score

    else:
        score = math.inf
        for position in empty_positions:
            new_board = Board(board)
            new_board.markCell(position[0], position[1], 1)
            score = min(score, minimax(new_board.board, depth - 1, True))
        return score
