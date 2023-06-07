import math


def evaluate(broad):
    # ham danh gia trang thai cua tro choi
    return 0


def get_possible_moves(broad):
    # ham chi ra nhung diem co the di duoc
    return []


def make_move(broad, move):
    # danh dau la da di roi
    return []


def minimax_alpha_beta(broad, depth, alpha, beta, player):
    if depth == 0:
        return evaluate(broad), None

    best_move = None

    if player:
        max_eval = - math.inf
        for move in get_possible_moves(broad):
            new_broad = make_move(broad, move)
            eval, tmp = minimax_alpha_beta(new_broad, depth - 1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for move in get_possible_moves(broad):
            new_broad = make_move(broad, move)
            eval, tmp = minimax_alpha_beta(broad, depth - 1, alpha, beta, True)
            if min_eval > eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move
