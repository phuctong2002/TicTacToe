import math
from constant import *


def check_map(cd):
    for p, value in pattern:
        if p == cd:
            return value
    return 0


def check_win(board):
    # Check rows
    for row in range(ROW):
        for col in range(COLUMN - 4):
            if board[row][col] != 0 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == board[row][col + 4]:
                return 1000000000000 if board[row][col] == 1 else -1000000000000

    # Check columns
    for col in range(COLUMN):
        for row in range(ROW - 4):
            if board[row][col] != 0 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == board[row + 4][col]:
                return 1000000000000 if board[row][col] == 1 else -1000000000000

    # Check diagonals
    for row in range(ROW - 4):
        for col in range(COLUMN - 4):
            if board[row][col] != 0 and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == board[row + 4][col + 4]:
                return 1000000000000 if board[row][col] == 1 else -1000000000000

            if board[row + 4][col] != 0 and board[row + 4][col] == board[row + 3][col + 1] == board[row + 2][col + 2] == board[row + 1][col + 3] == board[row][col + 4]:
                return 1000000000000 if board[row][col] == 1 else -1000000000000
    return 0


def evaluate_row(board):
    score = 0
    for r in range(ROW):
        for c in range(COLUMN - 4):
            score += check_map([board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3], board[r][c + 4]])
    return score


def evaluate_diagonal(board):
    score = 0
    for r in range(ROW - 4):
        for c in range(COLUMN - 4):
            score += check_map([board[r][c], board[r + 1][c + 1], board[r + 2][c + 2], board[r + 3][c + 3], board[r + 4][c + 4]])
            score += check_map([board[r+4][c], board[r+3][c + 1], board[r+2][c+ 2], board[r + 1][c + 3], board[r][c + 4]])
    return score


def evaluate_column(board):
    score = 0
    for r in range(ROW - 4):
        for c in range(COLUMN):
            score += check_map([board[r][c], board[r + 1][c], board[r + 2][c], board[r + 3][c], board[r + 4][c]])
    return score


def evaluate(board):
    score = 0
    score += evaluate_row(board)
    score += evaluate_column(board)
    score += evaluate_diagonal(board)
    return score


def get_possible_moves(board):
    possible_moves = []
    for r in range(ROW):
        for c in range(COLUMN):
            if board[r][c] == 0:
                possible_moves.append([r, c])
    return possible_moves


def make_move(board, move, bot):
    if bot:
        board[move[0]][move[1]] = 1
    else:
        board[move[0]][move[1]] = -1


def undo_make_move(board, move):
    board[move[0]][move[1]] = 0


def minimax_alpha_beta(board, depth, alpha, beta, bot):
    terminal = check_win(board)
    if terminal == 1000000000000:
        return 1000000000000, None
    if terminal == -1000000000000:
        return -1000000000000, None
    if depth == 0:
        return evaluate(board), None
    best_move = None
    if bot:
        max_eval = - math.inf
        for move in get_possible_moves(board):
            make_move(board, move, True)
            eval, tmp = minimax_alpha_beta(board, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            undo_make_move(board, move)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in get_possible_moves(board):
            make_move(board, move, False)
            eval, tmp = minimax_alpha_beta(board, depth - 1, alpha, beta, True)
            if min_eval > eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            undo_make_move(board, move)
            if beta <= alpha:
                break
        return min_eval, best_move

