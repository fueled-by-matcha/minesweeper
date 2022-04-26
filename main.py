from tkinter import *
import settings
import utilities
from cell import Cell

root = Tk()
# Override the settings of the window
root.configure(bg = "black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

# Create top frame
top_frame = Frame(
    root,
    bg = "black", #change to black
    width = settings.WIDTH,
    height = utilities.height_prct(25)
)
top_frame.place(x = 0, y = 0)

# Create left frame
left_frame = Frame(
    root,
    bg = "black",
    width = utilities.width_prct(25),
    height = utilities.height_prct(75)
)
left_frame.place(x = 0, y = utilities.height_prct(25))

# Create center frame
center_frame = Frame(
    root,
    bg = "black",
    width = utilities.width_prct(75),
    height = utilities.height_prct(75)
)
center_frame.place(x = utilities.width_prct(25), y = utilities.height_prct(25))

# Create game grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row = y
        )
print(Cell.all)
#Run the window
root.mainloop()