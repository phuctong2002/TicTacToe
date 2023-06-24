# from game import create_game
from constant import *
import tkinter as tk
import tkinter.font as tkFont
from algorithm import *
from constant import *


def move(event, frame1, frame2):
    global step
    index = event.widget.winfo_name().split("*")
    print(frame2)
    if matrix[int(index[0])][int(index[1])] == 0:
        if step % 2 == 0:
            tmp = check_win(matrix)
            if abs(tmp) == 1000000000000:
                return
            event.widget.config(text="o")
            step = step + 1
            matrix[int(index[0])][int(index[1])] = -1

            eval, best_move = minimax_alpha_beta(matrix, 2, -math.inf, math.inf, True)
            frame1.nametowidget(f"{best_move[0]}*{best_move[1]}").config(text="x")
            matrix[best_move[0]][best_move[1]] = 1
            step = step + 1


def reset(frame):
    global matrix
    global step
    for i in range(ROW):
        for j in range(COLUMN):
            frame.nametowidget(f"{i}*{j}").config(text="")
    for i in range(ROW):
        for j in range(COLUMN):
            matrix[i][j] = 0
    step = 0


def create_game():
    window = tk.Tk()
    frame1 = tk.Frame(master=window, width=600, height=HEIGHT)
    frame1.pack(side=tk.LEFT)
    frame2 = tk.Frame(master=window, width=200, height=HEIGHT)
    frame2.pack_propagate(False)
    frame2.pack(side=tk.RIGHT)
    info = tk.Label(master=frame2, text="Hello")
    info.pack()
    button = tk.Button(master=frame2, text="Reset game", name="button", command=lambda: reset(frame1))
    button.pack()
    for i in range(ROW):
        for j in range(COLUMN):
            label = tk.Label(master=frame1, text="", name=f"{i}*{j}", borderwidth=1, relief="solid", bg="#ffe6ff", font=tkFont.Font(size=40))
            # label.bind("<Button-1>", move)
            label.bind("<Button-1>", lambda event: move(event, frame1, frame2))
            label.place(x=20 + i * (CELL_SIZE + 1), y=10 + j * (CELL_SIZE + 1), height=CELL_SIZE + 1, width=CELL_SIZE + 1)
    window.mainloop()


create_game()
