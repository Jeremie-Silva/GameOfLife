"""GAME LIFE :
https://youtu.be/PlzV4aJ7iMI?si=8t2oHPY7qqY7DpL6
"""

import tkinter as tk
from random import randint


GRID_SIZE = 40  # square
SPEED = 100  # ms


def get_cells_neighbors(grid, vertical, horizontal):
    neighbors = []
    neighbors.append(grid[(vertical-1)%GRID_SIZE][(horizontal-1)%GRID_SIZE].cget("bg"))
    neighbors.append(grid[(vertical-1)%GRID_SIZE][horizontal].cget("bg"))
    neighbors.append(grid[(vertical-1)%GRID_SIZE][(horizontal+1)%GRID_SIZE].cget("bg"))
    neighbors.append(grid[vertical][(horizontal-1)%GRID_SIZE].cget("bg"))
    neighbors.append(grid[vertical][(horizontal+1)%GRID_SIZE].cget("bg"))
    neighbors.append(grid[(vertical+1)%GRID_SIZE][(horizontal+1)%GRID_SIZE].cget("bg"))
    neighbors.append(grid[(vertical+1)%GRID_SIZE][horizontal].cget("bg"))
    neighbors.append(grid[(vertical+1)%GRID_SIZE][(horizontal-1)%GRID_SIZE].cget("bg"))
    return neighbors


def update_grid(grid, size):
    for vertical in range(size):
        for horizontal in range(size):
            current_cell = grid[vertical][horizontal]
            neighbors = get_cells_neighbors(grid, vertical, horizontal)
            if current_cell.cget("bg") == "white":
                if neighbors.count("white") == 2 or neighbors.count("white") == 3:
                    pass
                else:
                    current_cell.config(bg="black")
            else:
                if neighbors.count("white") == 3:
                    current_cell.config(bg="white")
    root.after(SPEED, lambda: update_grid(grid, size=GRID_SIZE))


def create_grid(frame, size) -> list[list]:
    cells = []
    for vertical in range(size):
        row = []
        for horizontal in range(size):
            color = "black" if randint(0, 1) == 0 else "white"
            cell = tk.Label(frame, bg=color, width=2, height=1)
            cell.grid(row=vertical, column=horizontal)
            row.append(cell)
        cells.append(row)
    return cells


if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()
    grid = create_grid(frame, size=GRID_SIZE)
    root.after(SPEED, lambda: update_grid(grid, size=GRID_SIZE))
    root.mainloop()
