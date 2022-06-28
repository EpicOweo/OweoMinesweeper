import random

from tkinter import *

easiness = 3

grid = []
length = 15
width = 15

button_grid = []
spritesheet = []
root = None

generated = False


def get_stuff(bg, ss, rt, options):
    global button_grid, spritesheet, root, length, width, easiness
    button_grid = bg
    spritesheet = ss
    root = rt
    length = int(options['board_length'])
    width = int(options['board_width'])
    easiness = int(options['easiness'])


class GridSquare:
    def __init__(self, x, y, bomb):
        self.x = x
        self.y = y
        self.bomb = bomb
        self.revealed = False
        self.flag = False

    def check_adjacent(self):
        count = 0
        if self.bomb:
            return
        i = -1
        while i <= 1:
            j = -1
            while j <= 1:
                #  print(f'scanning square [{self.x + i}, {self.y + j}]...')
                if 0 <= self.x + i < length and 0 <= self.y + j < width:
                    if grid[self.x + i][self.y + j].bomb:
                        #  print(f'bomb at [{self.x + i}, {self.y + j}]')
                        count += 1
                j += 1
            i += 1
        return count

    def set_flag(self, *args):
        if self.revealed:
            return
        if self.flag:
            newimg = spritesheet[11]
        else:
            newimg = spritesheet[10]
        self.flag = not self.flag
        button_grid[self.x][self.y].configure(image=newimg)

    def setcmd(self):
        button_grid[self.x][self.y].configure(command=lambda: reveal(self.x, self.y))
        button_grid[self.x][self.y].bind("<Button-3>", self.set_flag)


def reveal(a, b):
    global generated, grid

    if not generated:
        generated = True
        grid = []
        generate_grid(a, b)

    square = grid[a][b]

    if square.revealed or square.flag:
        return

    if square.bomb:
        # root.destroy()
        for i in range(length):
            for j in range(width):
                if grid[i][j].bomb:
                    newimg = spritesheet[9]
                    button_grid[i][j].configure(image=newimg)
        return

    print(f'revealing {square.x},{square.y}')
    newimg = spritesheet[square.check_adjacent()]
    button_grid[a][b].configure(image=newimg)

    square.revealed = True

    if square.check_adjacent() != 0:
        return

    i = -1
    while i <= 1:
        j = -1
        while j <= 1:
            if 0 <= a + i < length and 0 <= b + j < width:
                if not grid[a + i][b + j].revealed:
                    reveal(a+i, b+j)
            j += 1
        i += 1

def generate_grid(a=0, b=0):
    global length, width, grid

    l = length
    w = width

    for i in range(l):
        grid.append([])

        for j in range(w):
            bomb = True if random.randint(0, easiness) == easiness else False
            if abs(a-i) <= 1 and abs(b-j) <= 1:
                bomb = False
            if not generated:
                bomb = False
            grid[i].append(GridSquare(i, j, bomb))

    for i in range(l):
        for j in range(w):
            grid[i][j].setcmd()

    return grid
