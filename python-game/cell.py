from tkinter import Button, Label, messagebox
import random
from turtle import settiltangle
import settings
import sys

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location, 
            width=12,
            height=4,
            #text=f"{self.x},{self.y}"
        )
        # Left click
        btn.bind('<Button-1>', self.left_click_action)
        # Right click
        btn.bind('<Button-2>', self.right_click_action)
        self.cell_btn_object = btn
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells Left: {Cell.cell_count}",
            width=12,
            height=4,
            bg='black',
            fg='white',
            font=("", 20)
        )
        Cell.cell_count_label_object = lbl


    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If mines count is = to cells left count
            if Cell.cell_count == settings.MINES_COUNT:
                messagebox.showerror("Game over!", "Congratulations you won!")
        
        # Cancel left and right click events if cell is already opened:
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-2>')

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the values of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    # Read only attribute
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y +1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace the text of the cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Left: {Cell.cell_count}"
                )    
        # Mark the cell as opened 
        self.is_opened = True

    def show_mine(self):
        # Logic to interrupt the game and display a message tha player lost!
        self.cell_btn_object.configure(highlightbackground='red')
        messagebox.showerror("Game over!", "You click on a mine!")
        sys.exit()

    def right_click_action(self, event):
        print("I am right clicked!")
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                highlightbackground='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                highlightbackground='white'
            )
            self.is_mine_candidate = False

    # This method belongs to the entire class
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    # Change the Cell.all presentation
    def __repr__(self):
        return f"Cell({self.x},{self.y})"