from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

import os, sys

import ms

import re

button_grid = []

options = {}

l = 15
w = 15

dark_mode = False

def read_options(file):
    global options
    f = open(file, 'r')

    checkstr = re.compile('(\w+)=(\w+)')

    for line in f:
        m = checkstr.match(line)
        options[m.group(1)] = m.group(2)

    print(options)
    f.close()
    return options

def load_options():
    global dark_mode, l, w

    if options['dark_mode'].lower() == 'true':
        dark_mode = True
    else:
        dark_mode = False

    l = int(options['board_length'])
    w = int(options['board_width'])


def main(argv):
    global options

    os.chdir(argv)

    options = read_options('options.txt')
    load_options()

    root = Tk()
    frame = ttk.Frame(root)
    frame.grid()
    
    spritesheet = []
    
    if dark_mode:
        ssimg = Image.open('spritesheet_dark.png')
        ttk.Style().configure("TButton", padding=0, background='black')
    else:
        ssimg = Image.open('spritesheet.png')
        ttk.Style().configure("TButton", padding=0)

    for i in range(12):
        spritesheet.append(ImageTk.PhotoImage(ssimg.crop((68 * i, 0, 68 * (i + 1), 68))))
    
    
    for i in range(l):
        button_grid.append([])
        for j in range(w):
            button_grid[i].append([j])
    for i in range(l):
        for j in range(w):
            button_grid[i][j] = ttk.Button(frame, image=spritesheet[11], command=ms.generate_grid)
            button_grid[i][j].grid(row=i, column=j)
    
    ms.get_stuff(button_grid, spritesheet, root, options)
    
    grid = ms.grid
    
    ms.generate_grid()
    
    root.mainloop()


if __name__ == "__main__":
    main(sys.argv[1])
