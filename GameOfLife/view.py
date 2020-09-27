from tkinter import *
import model
import controller

class View():
    def __init__(self, master, controller, model):
        self.frame = Frame(master)
        self.frame.pack()
        
        self.controller = controller

        self.grid_view = Canvas(self.frame, width=model.width*controller.cell_size,
                        height=model.height*controller.cell_size,
                        borderwidth=0,
                        highlightthickness=0,
                        bg='white')
        self.grid_view.bind('<Button-1>', controller.grid_handler)
        self.start_button = Button(self.frame, text='Start', width=12)
        self.start_button.bind('<Button-1>', controller.start_handler)
        self.clear_button = Button(self.frame, text='Clear', width=12)
        self.clear_button.bind('<Button-1>', controller.clear_handler)

        self.choice = StringVar(self.frame)
        self.choice.set('Choose a Pattern')

        self.option = OptionMenu(self.frame, self.choice, 'Choose a Pattern', 'glider', 'glider gun', 'random', command=controller.option_handler)
        self.option.config(width=20)

        self.grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
        self.start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
        self.option.grid(row=1, column=1, padx=20)
        self.clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)