import math
from constant import *


def check_win(board, bot):
    # Check rows
    for row in range(ROW):
        for col in range(COLUMN - 3):
            if board[row][col] != 0 and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3] == bot:
                return True

    # Check columns
    for col in range(COLUMN):
        for row in range(ROW - 3):
            if board[row][col] != 0 and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col] == bot:
                return True

    # Check diagonals
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if board[row][col] != 0 and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3] == bot:
                return True

            if board[row + 3][col] != 0 and board[row + 3][col] == board[row + 2][col + 1] == board[row + 1][col + 2] == board[row][col + 3]:
                return True

    return False


def evaluate_row(board, bot):
    score = 0
    for r in range(COLUMN):
        cell = 0
        for c in range(ROW):
            if board[c][r] == bot:
                cell += 1
            else:
                cell = 0
                if cell == 2:
                    score += 10
                if cell == 3:
                    score += 100

    return score


def evaluate_diagonal(board, bot):
    score = 0
    checked = [[0 for _ in range(10)] for _ in range(10)]
    for r in range(ROW - 2):
        for c in range(COLUMN - 2):
            if board[r][c] == 0:
                if board[r][c] == board[r + 1][c + 1] == board[r + 2][c + 2] == bot:
                    score += 100
                    checked[r][c] = checked[r + 1][c + 1] = checked[r + 2][c + 2] = 1
                elif board[r][c] == board[r + 1][c + 1] == bot:
                    score += 10
                    checked[r][c] = checked[r + 1][c + 1] = 1
    return score


def evaluate_column(board, bot):
    score = 0
    for r in range(ROW):
        cell = 0
        for c in range(COLUMN):
            if board[r][c] == bot:
                cell += 1
            else:
                cell = 0
                if cell == 2:
                    score += 10
                if cell == 3:
                    score += 100
    return score


def evaluate(board):
    score = 0
    if check_win(board, 1):
        score -= 1000000
        return score
    if check_win(board, 2):
        score += 10000000
        return score
    score += evaluate_row(board, 2)
    score -= evaluate_row(board, 1)
    score += evaluate_column(board, 2)
    score -= evaluate_column(board, 1)
    score += evaluate_diagonal(board, 2)
    score -= evaluate_diagonal(board, 1)
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
        board[move[0]][move[1]] = 2
    else:
        board[move[0]][move[1]] = 1


def undo_make_move(board, move):
    board[move[0]][move[1]] = 0


def minimax_alpha_beta(board, depth, alpha, beta, bot):
    if depth == 0:
        return evaluate(board), None
    best_move = None
    if check_win(board, 2):
        return 1000000, None
    if check_win(board, 1):
        return -1000000, None
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

