from tkinter import *
from turtle import left
from cell import Cell
import settings
import utils

root = Tk()
# Override the settings of the window
root.configure(bg="black")
root.geometry(f'{int(settings.WIDTH*settings.WINDOW_PERCETAGE)}x{int(settings.HEIGHT*settings.WINDOW_PERCETAGE)}')
root.resizable(False, False) 
root.title("Minesweeper Game")

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH*settings.WINDOW_PERCETAGE,
    height= utils.height_prct(25)*settings.WINDOW_PERCETAGE
)

top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper Game",
    font=('', 48)
)

game_title.place(
    x=utils.width_prct(25), y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(25)*settings.WINDOW_PERCETAGE,
    height=utils.height_prct(75)*settings.WINDOW_PERCETAGE,
)

left_frame.place(x=0, y=utils.height_prct(25)*settings.WINDOW_PERCETAGE)

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_prct(75)*settings.WINDOW_PERCETAGE,
    height=utils.height_prct(75)*settings.WINDOW_PERCETAGE
)

center_frame.place(
    x=utils.width_prct(25)*settings.WINDOW_PERCETAGE,
    y=utils.height_prct(25)*settings.WINDOW_PERCETAGE)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

# Run the window
root.mainloop()