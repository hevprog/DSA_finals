import ttkbootstrap as ttk
from logic.counting import counting
import random as r
import winsound

class Counting_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.col = 'black'
        self.parent = parent
        ttk.Label(self, text="This is counting sort").pack(pady= 10)
        ttk.Button(self,text="back to menu",command=self.back_button).pack()
        ttk.Button(self,text="Sort", command=self.sorting).pack(side="bottom",pady=10)
        ttk.Label(self,text="A counting sort is a sorting algorithm. The basic idea behind Counting Sort is to count the frequency \nof each distinct element and use that information to place the elements in a sorted way").pack(side="bottom")
        self.label1 = ttk.Label(self)
        self.label1.pack(pady=5,side="bottom")
        ttk.Button(self,text="Randomize", command=self.randomize_val).pack(side="bottom",pady= 20)
        self.canvas = ttk.Canvas(self, width= 1000,height= 500) # ig 1000 nala em width para ma fix
        self.canvas.pack(pady=5)


        self.coin_values = [1,1,5,2,4,4,6,7,3,3]
        self.coin_items = []
        x_start = 150
        y_pos = 100
        coin_size = 50
        gap = 20
        
        #to create and desplay coins
        for i, value in enumerate(self.coin_values):
            x1 = x_start + i * (coin_size + gap)
            y1 = y_pos
            x2 = x1 + coin_size
            y2 = y_pos + coin_size
            #for every coin value na divisible by 2 paint it gold!
            self.canvas.create_oval(x1, y1, x2, y2, fill="gold" if value % 2 == 0 else "Darkgoldenrod3", width=2)
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text=str(value), font=("Helvetica", 16, "bold"))
    def sorting(self):
        self.label1.config(text="Sorted")
        countingC = counting(self.coin_values)
        countingC.sort()
        self.coin_values = countingC.get_array()
        self.col = "green"
        winsound.Beep(500,20)
        self.redraw()
        
    def randomize_val(self):
        self.label1.config(text="Randomized")
        r.shuffle(self.coin_values)
        self.col = "black"
        self.redraw()
    def back_button(self):
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu
    def redraw(self):
        self.coin_items = []
        x_start = 150
        y_pos = 100
        coin_size = 50
        gap = 20
        for i, value in enumerate(self.coin_values):

            x1 = x_start + i * (coin_size + gap)
            y1 = y_pos
            x2 = x1 + coin_size
            y2 = y_pos + coin_size
            
            self.canvas.create_oval(x1, y1, x2, y2, fill="gold" if value % 2 == 0 else "Darkgoldenrod3", width=2,outline=self.col)
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text=str(value), font=("Helvetica", 16, "bold"))

            if(self.col != "green"):
                winsound.Beep(1000,100)