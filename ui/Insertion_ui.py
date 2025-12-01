import ttkbootstrap as ttk
from logic.insertion import insertion
import random as r
import winsound
import pygame

class InsertionUi(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.col = 'black'
        self.parent = parent
        ttk.Label(self, text="This is the Insertion sort").pack(pady = 10)
        ttk.Button(self,text="back to menu", command=self.back_button).pack()
        ttk.Button(self, text="Sort", command=self.sorting).pack(side ="bottom", pady=10)
        ttk.Label(self, text= "Insertion Sort").pack(side="bottom")
        self.Label1 = ttk.Label(self)
        self.Label1.pack(pady=5, side="bottom")
        ttk.Button(self, text="Randomize", command=self.randomize_val).pack(side = "bottom", pady=20)
        self.canvas = ttk.Canvas(self, width=750, height=500)
        self.canvas.pack(pady=5)

        pygame.mixer.music.pause()

        self.coin_values = [63, 22, 12, 23, 45, 34, 11, 23, 78, 99]
        self.coin_items = []
        x_start = 50
        y_pos = 100
        coin_size = 50
        gap = 20

        # to create and display coins

        for i, value in enumerate(self.coin_values):
            x1 = x_start + i * (coin_size + gap)
            y1 = y_pos
            x2 = x1 + coin_size
            y2 = y_pos + coin_size

            # for every coin value divisible by 2
            self.canvas.create_oval(x1, y1, x2, y2, fill="pink" if value % 2 == 0 else "lightgreen", width=2)
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text = str(value), font=("Helvetica", 16, "bold"))
    
    def sorting(self):
        self.Label1.config(text = "Sorted")
        insertionC = insertion(self.coin_values)
        insertionC.sort()
        self.col = "green"
        winsound.Beep(500, 20)
        self.redraw()

    def randomize_val(self):
        self.Label1.config(text="Randomized")
        r.shuffle(self.coin_values)
        self.col = "black"
        self.redraw()
    
    def back_button(self):
        pygame.mixer.music.unpause()
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu
    
    def redraw(self):
        self.coin_items = []
        x_start = 50
        y_pos = 100
        coin_size = 50
        gap = 20
        
        for i, value in enumerate(self.coin_values):

            x1 = x_start + i * (coin_size + gap)
            y1 = y_pos
            x2 = x1 + coin_size
            y2 = y_pos + coin_size

            self.canvas.create_oval(x1, y1, x2, y2, fill="pink" if value % 2 == 0 else "lightgreen", width=2, outline=self.col)
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text=str(value), font=("Helvetica", 16, "bold"))

            if(self.col != "green"):
                winsound.Beep(1000,100)