import tkinter as tk
import tkinter.font as tkFont
from constant import *


step = 1


def move(event):
    global step
    if step % 2 == 1:
        print(event.widget.config(text="o"))
    else:
        event.widget.config(text="x")
    step = step + 1


def reset(frame):
    print("reset nhe")
    for widget in frame.winfo_children():
        print(widget.winfo_children()[0].config(text=""))


def create_game():
    window = tk.Tk()
    x = int((window.winfo_screenwidth() - WIDTH) / 2)
    y = int((window.winfo_screenheight() - HEIGHT) / 2)
    window.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x, y))
    frame1 = tk.Frame(window, width=600, height=HEIGHT, bg="red")
    frame1.pack(side=tk.LEFT)
    frame2 = tk.Frame(window, width=WIDTH - 600, height=HEIGHT)
    frame2.pack(side=tk.RIGHT)
    greeting = tk.Label(master=frame2, text="hello", name="alert")
    # add label into window
    greeting.pack()
    button = tk.Button(
        master=frame2,
        text="Reset game",
        command=lambda: reset(frame1),
        name="button"
    )
    button.pack()
    # grid
    for i in range(ROW):
        for j in range(COLUMN):
            frame = tk.Frame(
                master=frame1,
                relief=tk.RAISED,
                borderwidth=1,
                height=CELL_SIZE,
                width=CELL_SIZE,
                bg="#ffe6ff"
            )
            label = tk.Label(master=frame, text="", height=frame.winfo_height(),
                             width=frame.winfo_width(), font=tkFont.Font(size=40))
            label.bind("<Button-1>", move)
            label.pack(fill=tk.BOTH, expand=True)
            frame.pack_propagate(0)
            frame.grid(row=i, column=j)
    window.mainloop()
    return window
