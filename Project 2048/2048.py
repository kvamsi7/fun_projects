from tkinter import Frame,Label,CENTER

import logics
import constants as c 


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>",self.key_down)
        self.commands = {c.KEY_UP:logics.move_up,
                         c.KEY_DOWN:logics.move_down,
                         c.KEY_LEFT:logics.move_left,
                         c.KEY_RIGHT:logics.move_right}

        self.grid_cells = []
        self.init_grid()    # create the grid cells in the grid
        self.init_matrix() # initialize with zeros
        self.update_grid_cells() # update  ui according to values
        self.mainloop() # actually runs the program

    def init_grid(self):
        background = Frame(self,bg=c.BACKGROUND_COLOR_GAME,
                           width = c.SIZE,height = c.SIZE)

        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(background,bg = c.BACKGROUND_COLOR_CELL_EMPTY,
                             width = c.SIZE/ c.GRID_LEN,
                             height = c.SIZE / c.GRID_LEN)
                cell.grid(row = i, column = j, padx = c.GRID_PADDING,
                          pady = c.GRID_PADDING)
                t = Label(master = cell, text = "",
                    bg = c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify = CENTER, font = c.FONT, width = 5, height = 2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def init_matrix(self):
        self.matrix = logics.start_game()
        logics.add_new_2(self.matrix)
        logics.add_new_2(self.matrix)
    
    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text = "", bg= c.BACKGROUND_COLOR_CELL_EMPTY
                    )
                else:
                    self.grid_cells[i][j].configure(text = str(new_number),
                    bg = c.BACKGROUND_COLOR_DICT[new_number],
                    fg = c.CELL_COLOR_DICT[new_number])
            self.update_idletasks()
    def key_down(self,event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix , changed = self.commands[repr(event.char)](self.matrix)
             
            if changed:
                logics.add_new_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if logics.get_current_state(self.matrix) == "WON":
                    self.grid_cells[1][1].configure(
                        text = "You", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text = "Win!",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if logics.get_current_state(self.matrix) == "LOST":
                    self.grid_cells[1][1].configure(
                        text = "You", bg= c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text = "Lose!",bg=c.BACKGROUND_COLOR_CELL_EMPTY)

if __name__ == "__main__":
    gamegrid = Game2048()
