import sys
import time
import pygame
import warnings
import tkinter as tk
from tkinter import messagebox
from algorithm import check_nilpotency

"""
    This is the main script which renders the graphical user interface of the 
    app and performs the logic behind nilpotency check.
    gui.main is called main script with i/p size argument.

    Developer: Vedant Raghuwanshi, 118EE0705

"""

warnings.filterwarnings("ignore", category=DeprecationWarning)


def main(size):
    pygame.font.init()

    class Grid:
        grid = [[float("inf")] * size for i in range(size)]

        def __init__(self, rows, cols, width, height, win):
            self.rows = rows
            self.cols = cols
            self.cubes = [
                [Cube(self.grid[i][j], i, j, width, height) for j in range(cols)]
                for i in range(rows)
            ]
            self.width = width
            self.height = height
            self.model = None
            self.update_model()
            self.selected = None
            self.win = win

        def update_model(self):
            self.model = [
                [self.cubes[i][j].value for j in range(self.cols)]
                for i in range(self.rows)
            ]

        def place(self, val):
            row, col = self.selected
            if self.cubes[row][col].value == float("inf"):
                self.cubes[row][col].set(val)
                self.update_model()

            return True

        def sketch(self, val):
            row, col = self.selected
            self.cubes[row][col].set_temp(val)

        def draw(self):
            # Draw Grid Lines
            gap = self.width / size
            for i in range(self.rows + 1):
                if i % 3 == 0 and i != 0:
                    thick = 4
                else:
                    thick = 1
                pygame.draw.line(
                    self.win,
                    (255, 255, 255),
                    (0, i * gap),
                    (self.width, i * gap),
                    thick,
                )
                pygame.draw.line(
                    self.win,
                    (255, 255, 255),
                    (i * gap, 0),
                    (i * gap, self.height),
                    thick,
                )

            # Draw Cubes
            for i in range(self.rows):
                for j in range(self.cols):
                    self.cubes[i][j].draw(self.win)

        def select(self, row, col):
            # Reset all other
            for i in range(self.rows):
                for j in range(self.cols):
                    self.cubes[i][j].selected = False

            self.cubes[row][col].selected = True
            self.selected = (row, col)

        def clear(self):
            row, col = self.selected
            # if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(float("inf"))

        def click(self, pos):
            """
            :param: pos
            :return: (row, col)
            """
            if pos[0] < self.width and pos[1] < self.height:
                gap = self.width / size
                x = pos[0] // gap
                y = pos[1] // gap
                return int(y), int(x)
            else:
                return None

        def solve_gui(self):
            matrix = [
                [self.cubes[i][j].value for i in range(size)] for j in range(size)
            ]

            for i in range(size):
                for j in range(size):
                    matrix[i][j] = self.cubes[i][j].value
                    self.cubes[i][j].draw_change(self.win, True)
                    pygame.display.update()
                    pygame.time.delay(100)

            eigvalues, isnilpotent = check_nilpotency(matrix)
            return eigvalues, isnilpotent

    class Cube:
        rows = size
        cols = size

        def __init__(self, value, row, col, width, height):
            self.value = value
            self.temp = 0
            self.row = row
            self.col = col
            self.width = width
            self.height = height
            self.selected = False

        def draw(self, win):
            fnt = pygame.font.SysFont("comicsans", 40)

            gap = self.width / size
            x = self.col * gap
            y = self.row * gap

            if self.temp == 0 and self.value == float("inf"):
                text = fnt.render("inf", 1, (255, 255, 255))
                win.blit(
                    text,
                    (
                        x + (gap / 2 - text.get_width() / 2),
                        y + (gap / 2 - text.get_height() / 2),
                    ),
                )

            elif self.temp != float("inf") and self.value == float("inf"):
                text = fnt.render(str(self.temp), 1, (255, 255, 255))
                win.blit(text, (x + 5, y + 5))

            elif not (self.value == float("inf")):
                text = fnt.render(str(self.value), 1, (255, 255, 255))
                win.blit(
                    text,
                    (
                        x + (gap / 2 - text.get_width() / 2),
                        y + (gap / 2 - text.get_height() / 2),
                    ),
                )

            if self.selected:
                pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

        def draw_change(self, win, g=True):
            fnt = pygame.font.SysFont("comicsans", 40)

            gap = self.width / size
            x = self.col * gap
            y = self.row * gap

            pygame.draw.rect(win, (0, 0, 0), (x, y, gap, gap), 0)

            text = fnt.render(str(self.value), 1, (255, 255, 255))
            win.blit(
                text,
                (
                    x + (gap / 2 - text.get_width() / 2),
                    y + (gap / 2 - text.get_height() / 2),
                ),
            )
            if g:
                pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
            else:
                pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

        def set(self, val):
            self.value = val

        def set_temp(self, val):
            self.temp = val

    def redraw_window(win, grid, time):
        win.fill((0, 0, 0))
        # Draw time
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render("Time: " + format_time(time), 1, (255, 255, 255))
        win.blit(text, (540 - 160, 560))
        text = fnt.render("Vedant Raghuwanshi", 1, (255, 255, 255))
        win.blit(text, (20, 560))
        # Draw grid and grid
        grid.draw()

    def format_time(secs):
        sec = secs % 60
        minute = secs // 60

        mat = " " + str(minute) + ":" + str(sec)
        return mat

    def popup_msg(msg):
        root = tk.Tk()
        root.title("Result")
        label = tk.Label(root, text=msg)
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)
        button = tk.Button(root, text="OK", command=lambda: root.destroy())
        button.pack(side="bottom", fill="none", expand=True)
        root.mainloop()

    def process():
        win = pygame.display.set_mode((540, 600))
        pygame.display.set_caption("IsNilpotent App")
        grid = Grid(size, size, 540, 540, win)
        key = ""
        run = True
        negative = False
        start = time.time()
        while run:

            play_time = round(time.time() - start)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    # if event.key == pygame.K_n:
                    #     negative = not negative
                    # if event.key == pygame.K_0:
                    #     key = 0
                    # if event.key == pygame.K_1:
                    #     key = -1 if negative else 1
                    # if event.key == pygame.K_2:
                    #     key = -2 if negative else 2
                    # if event.key == pygame.K_3:
                    #     key = -3 if negative else 3
                    # if event.key == pygame.K_4:
                    #     key = -4 if negative else 4
                    # if event.key == pygame.K_5:
                    #     key = -5 if negative else 5
                    # if event.key == pygame.K_6:
                    #     key = -6 if negative else 6
                    # if event.key == pygame.K_7:
                    #     key = -7 if negative else 7
                    # if event.key == pygame.K_8:
                    #     key = -8 if negative else 8
                    # if event.key == pygame.K_9:
                    #     key = -9 if negative else 9
                    key += event.unicode

                    if event.key == pygame.K_DELETE:
                        grid.clear()
                        key = ""

                    if event.key == pygame.K_SPACE:
                        try:
                            eigvalues, isnilpotent = grid.solve_gui()
                            if isnilpotent:
                                popup_msg(
                                    f"The I/P Matrix is NILPOTENT\n Eigven Values: {eigvalues}"
                                )
                            else:
                                popup_msg(
                                    f"The I/P Matrix is NOT NILPOTENT\n Eigen Values: {eigvalues}"
                                )

                            # print("Over")

                        except TypeError:
                            pass

                    if event.key == pygame.K_RETURN:
                        i, j = grid.selected
                        # if grid.cubes[i][j].temp != 0:
                        if grid.place(grid.cubes[i][j].temp):
                            pass
                        key = ""

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    clicked = grid.click(pos)
                    if clicked:
                        grid.select(clicked[0], clicked[1])
                        key = ""

            if grid.selected and key is not None:
                grid.sketch(key)

            redraw_window(win, grid, play_time)
            pygame.display.update()

    process()
    pygame.quit()


if __name__ == "__main__":

    sz = int(sys.argv[1])
    main(sz)
    sys.exit()
