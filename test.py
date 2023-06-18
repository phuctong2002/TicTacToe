from algorithm import *
# from constant import *

# Tạo một bảng 3x3 ban đầu
broad = [
    [1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Gọi hàm minimax_alpha_beta để tính toán nước đi tối ưu
depth = 3  # Độ sâu của thuật toán
alpha = -math.inf  # Giá trị alpha ban đầu
beta = math.inf  # Giá trị beta ban đầu
bot = True  # Xác định bot là người chơi đang đi (True) hay không (False)
eval, best_move = minimax_alpha_beta(broad, depth, alpha, beta, bot)
#
# # Hiển thị kết quả
print("Giá trị đánh giá tốt nhất:", eval)
print("Nước đi tối ưu:", best_move)

# if check_win(broad, 2):
#     print("boot thang")

