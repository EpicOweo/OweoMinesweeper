from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import ms

button_grid = []

l = 15
w = 15

root = Tk()
frame = ttk.Frame(root)
frame.grid()

spritesheet = []

ssimg = Image.open('spritesheet.png')
for i in range(11):
    spritesheet.append(ImageTk.PhotoImage(ssimg.crop((50 * i, 0, 50 * (i + 1), 50))))

square = PhotoImage(file='square.png')

ttk.Style().configure("TButton", background='black')


for i in range(l):
    button_grid.append([])
    for j in range(w):
        button_grid[i].append([j])
for i in range(l):
    for j in range(w):
        button_grid[i][j] = ttk.Button(frame, image=square, command=ms.generate_grid)
        button_grid[i][j].grid(row=i, column=j)

ms.get_stuff(button_grid, spritesheet, root, square)

grid = ms.grid

ms.generate_grid()

root.mainloop()
