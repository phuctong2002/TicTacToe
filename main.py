# from game import create_game
from constant import *
import tkinter as tk
import tkinter.font as tkFont


def move(event):
    global step
    index = event.widget.winfo_name().split("*")
    if matrix[int(index[0])][int(index[1])] == 0:
        if step % 2 == 1:
            event.widget.config(text="x")
            print(event.widget)
            step = step + 1
            matrix[int(index[0])][int(index[1])] = 1
        else:
            event.widget.config(text="o")
            print(event.widget)
            step = step + 1
            matrix[int(index[0])][int(index[1])] = 2

        #     cho nay nen bat sau do roi chay luon o day di
        # if step % 2 == 1:
        #     event.widget.config(text="x")
        #     step = step + 1
        #     matrix[int(index[0])][int(index[1])] = 1
#             den luot may di nhe

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
            label.bind("<Button-1>", move)
            label.place(x=20 + i * (CELL_SIZE + 1), y=10 + j * (CELL_SIZE + 1), height=CELL_SIZE + 1, width=CELL_SIZE + 1)
    window.mainloop()


create_game()
