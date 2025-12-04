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
        
        self.valid_move = pygame.mixer.Sound('ui/sounds/select.wav')
        pygame.mixer.music.pause()

        ttk.Label(self, text="This is the Insertion sort").pack(pady = 10)
        ttk.Button(self,text="back to menu", command=self.back_button).pack()
        ttk.Button(self, text="Sort", command=self.sorting).pack(side ="bottom", pady=10)
        ttk.Label(self, text= "Insertion Sort").pack(side="bottom")
        self.Label1 = ttk.Label(self)
        self.Label1.pack(pady=5, side="bottom")
        ttk.Button(self,text="Randomize", command=self.Shuffle).pack(side="bottom",pady= 20)
        self.canvas = ttk.Canvas(self, width=1000, height=500)
        self.canvas.pack(pady=5)

        self.labelCounts = []
        self.labelCountsStr = []

        self.sortedArr = []
        self.coins = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"]
        self.coin_values = [63, 22, 12, 23, 45, 34, 11, 23, 78, 99]
        self.coin_pos_x = []
        self.coin_pos_y = []

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
            tag = self.coins[i]

            # for every coin value divisible by 2
            self.canvas.create_oval(x1, y1, x2, y2, fill="pink" if value % 2 == 0 else "lightgreen", width=2, tags=(tag, tag+"_shape"))
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text = str(value), font=("Helvetica", 16, "bold"), tags= (tag, tag+"_txt"))
            self.sortedArr.append({"x":x1,"coin":self.coins[i]})
            self.coin_pos_x.append(x1)
            self.coin_pos_y.append(y1)
        self.ordered_places = self.coin_pos_x[:]
    
    def sorting(self):
        self.Label1.config(text = "Sorted")
        insertionC = insertion(self.coin_values)
        insertionC.sort()
        self.col = "green"
        self.play_sound()
        self.counts = ttk.Label(self, text="HIII").pack(pady=5)

    def Shuffle(self):
        
        self.Label1.config(text="Randomized")

        new_x_positions = self.coin_pos_x[:]
        r.shuffle(new_x_positions)

        for i, coin in enumerate(self.sortedArr):
            tag = coin["coin"]
            start_y = self.coin_pos_y[i]
            new_x = new_x_positions[i]
            self.canvas.itemconfig(tag+"_shape",width=2,outline="black")
            # pa up
            self.canvas.after(i * 300, lambda t=tag,x=self.canvas.winfo_width()//2, y=start_y: 
                self.canvas.moveto(t, x,y - 50)
            )

            self.canvas.after(i * 300 + 150, lambda t=tag, x=new_x, y=start_y: 
                self.canvas.moveto(t, x, y - 50)
            )
            self.canvas.after(i * 300 + 150,lambda:self.play_sound())
           
            self.canvas.after(i * 300 + 300, lambda t=tag, x=new_x, y=start_y: 
                self.canvas.moveto(t, x, y)
            )
        self.play_sound()
    
    def back_button(self):
        pygame.mixer.music.unpause()
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu
    
                
    def play_sound(self):
        self.valid_move.play()

    def moveDa_coin(self, tag, new_x, base_y, delay, done_callback=None):
        
        self.canvas.after(delay, lambda: self.canvas.moveto(tag, new_x, base_y - 40))
        self.canvas.after(delay + 200, lambda: self.canvas.moveto(tag, new_x, base_y))
        self.canvas.after(delay + 200, lambda: self.play_sound())
        if done_callback:
            self.canvas.after(delay + 250, done_callback)

    def animate(self):
        sortedValue = self.coin_values
        key = self.coin_values[1]

        for i, coin in enumerate(self.coin_values):
            tag = coin["coin"]
            key = self.coin_values[i]
            j = i - 1
            while j >= 0 and self.coin_values[j] > key:
                self.coin_values[j + 1] = self.coin_values[j]
                j -= 1
            self.coin_values[j + 1] = key
        
def play_sound(self,n=0,ms=3000):
    self.valid_move.play(loops=n)
def play_sound2(self,n=0,ms=3000):
    self.notif_random.play(loops=n)