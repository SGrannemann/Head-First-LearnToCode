from model import Model
from view import View

from tkinter import *




class Controller():
    def __init__(self):
        self.root = Tk()
        self.root.title('The Game of Life')
        self.cell_size = 5
        self.is_running = False
        self.model = Model()
        self.view = View(self.root, self, self.model)
        self.root.mainloop()



    def grid_handler(self, event):
        

        x = int(event.x / self.cell_size)
        y = int(event.y / self.cell_size)

        if (self.model.grid_model[x][y] == 1):
            self.model.grid_model[x][y] = 0
            self.draw_cell(x, y, 'white')
        else:
            self.model.grid_model[x][y] = 1
            self.draw_cell(x, y, 'black')


    def clear_handler(self, event):
        
            
        self.is_running = False
        self.view.start_button.configure(text='Start')
        for i in range(0, self.model.height):
            for j in range(0, self.model.width):
                self.model.grid_model[i][j] = 0

        self.update()

    def option_handler(self, event):
       

        self.is_running = False
        self.view.start_button.configure(text='Start')

        selection = self.view.choice.get()

        if selection == 'glider':
            self.model.load_pattern(self.model.glider_pattern, 10, 10)
        
        elif selection == 'glider gun':
            self.model.load_pattern(self.model.glider_gun_pattern, 10, 10)

        elif selection == 'random':
            self.model.randomize()

            self.update()

    def start_handler(self, event):
        

        if self.is_running:
            self.is_running = False
            self.view.start_button.configure(text='Start')
        else:
            self.is_running = True
            self.view.start_button.configure(text='Pause')
            self.update()


    def update(self):
        

        self.view.grid_view.delete(ALL)
        
        self.model.next_gen()
        for i in range(0, self.model.height):
            for j in range(0, self.model.width):
                if self.model.grid_model[i][j] == 1:
                    self.draw_cell(i, j, 'black')
        if (self.is_running):
            self.root.after(100, self.update)


    def draw_cell(self, row, col, color):
        

        if color == 'black':
            outline = 'grey'
        else:
            outline = 'white'

        self.view.grid_view.create_rectangle(row*self.cell_size,
                                    col*self.cell_size,
                                    row*self.cell_size+self.cell_size,
                                    col*self.cell_size+self.cell_size,
                                    fill=color, outline=outline)
