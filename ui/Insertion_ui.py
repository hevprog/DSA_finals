import ttkbootstrap as ttk
from logic.insertion import insertion
import random as r
import pygame

class InsertionUi(ttk.Frame):
    MIN = 0
    MAX = 9

    def __init__(self, parent):
        super().__init__(parent)
        self.col = 'black'
        self.parent = parent
        
        self.valid_move = pygame.mixer.Sound('DSA_finals/ui/sounds/select.wav')
        pygame.mixer.music.pause()

        ttk.Label(self, text="This is the Insertion sort").pack(pady = 10)
        ttk.Button(self,text="back to menu", command=self.back_button).pack()
        ttk.Button(self, text="Sort", command=self.sorting).pack(side ="bottom", pady=10)
        ttk.Label(self, text= "Insertion Sort").pack(side="bottom")
        self.Label1 = ttk.Label(self)
        self.Label1.pack(pady=5, side="bottom")
        ttk.Button(self,text="Shuffle", command=self.Shuffle).pack(side="bottom",pady= 20)
        ttk.Button(self,text="random values", command=self.random_val).pack(side="bottom",pady= 5)
        ttk.Button(self, text="Randomize", command=self.randomize_val).pack(side = "bottom", pady=20)
        self.canvas = ttk.Canvas(self, width=1000, height=500)
        self.canvas.pack(pady=5)

        self.labelCounts = []
        self.labelCountsStr = []

        self.sortedArr = []
        self.key = []
        self.coins = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"]
        self.coin_values = [63, 22, 12, 23, 45, 34, 11, 23, 78, 99]
        self.coin_pos_x = []
        self.coin_pos_y = []
        self.ordered_places = []

        x_start = 50
        y_pos = 100
        self.coin_size = 50
        gap = 20

        # to create and display coins

        for i, value in enumerate(self.coin_values):
            x1 = x_start + i * (self.coin_size + gap)
            y1 = y_pos
            x2 = x1 + self.coin_size
            y2 = y_pos + self.coin_size

            # for every coin value divisible by 2
            self.canvas.create_oval(x1, y1, x2, y2, fill="pink" if value % 2 == 0 else "lightgreen", width=2, tags=(tag, tag+"_shape"))
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text = str(value), font=("Helvetica", 16, "bold"))
    
    def sorting(self):
        self.Label1.config(text = "Sorted")
        insertionC = insertion(self.coin_values)
        insertionC.sort()
        self.col = "green"
        self.play_sound()
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
                self.play_sound()
                
                
    def play_sound(self):
        self.valid_move.play()