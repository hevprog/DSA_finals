import tkinter as tk
import ttkbootstrap as ttk
from logic.counting import counting
import random as r
import pygame

class inconvient_typing:
    def tkInt(a):
        return ttk.IntVar(value=a)
    def tkStr(a):
        return ttk.StringVar(value=a)
class Counting_ui(ttk.Frame,inconvient_typing):
    MIN =0
    MAX =9
    def __init__(self, parent):
        super().__init__(parent)
        self.col = 'black'
        self.parent = parent
        
        self.valid_move = pygame.mixer.Sound('DSA_finals/ui/sounds/select.wav')
        self.notif_random = pygame.mixer.Sound('DSA_finals/ui/sounds/wrong_move.wav')
        pygame.mixer.music.pause()
        
        
        ttk.Label(self, text="This is counting sort").pack(pady= 10)
        ttk.Button(self,text="back to menu",command=self.back_button).pack()
        ttk.Button(self,text="Sort", command=self.sorting).pack(side="bottom",pady=10)
        ttk.Label(self,text="A counting sort is a sorting algorithm. The basic idea behind Counting Sort is to count the frequency \nof each distinct element and use that information to place the elements in a sorted way").pack(side="bottom")
        self.label1 = ttk.Label(self)
        self.label1.pack(pady=5,side="bottom")
        ttk.Button(self,text="Shuffle", command=self.Shuffle).pack(side="bottom",pady= 20)
        ttk.Button(self,text="random values", command=self.random_val).pack(side="bottom",pady= 5)
        self.canvas = ttk.Canvas(self, width= 1000,height= 500) # ig 1000 nala em width para ma fix
        self.canvas.pack(pady=5)

        self.labelcounts = []
        self.labelcounts_Str = []

        self.sortArr = []
        self.count = []
        self.coins = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"]
        self.coin_values = [1,1,5,2,4,4,6,7,4,3]
        self.coin_posx = []
        self.coin_posy = []
        self.ordered_places =[]
        
        x_start = 150
        y_pos = 100
        self.coin_size = 50
        gap = 20
        
        #ma himo hin coins
        for i, value in enumerate(self.coin_values):
            x1 = x_start + i * (self.coin_size + gap)
            y1 = y_pos
            x2 = x1 + self.coin_size
            y2 = y_pos + self.coin_size
            tag = self.coins[i]
            #mga even numbers magiging gold para may variety
            self.canvas.create_oval(x1, y1, x2, y2, fill="gold" if value % 2 == 0 else "Darkgoldenrod3", width=2,tags=(tag, tag+"_shape"))
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text=str(value), font=("Helvetica", 16, "bold"),tags=(tag, tag+"_txt"))
            self.sortArr.append({"x":x1,"coin":self.coins[i]})
            self.coin_posx.append(x1)
            self.coin_posy.append(y1)
        self.ordered_places = self.coin_posx[:]


    def sorting(self):
        self.label1.config(text="Sorted")
        countingC = counting(self.coin_values)
        countingC.sort()
        self.count = countingC.get_count()
        self.coin_values = countingC.get_array()
        self.col = "green"
        self.play_sound(0)
        total_delay_step1 = self.animate_sort_step1()
        self.counts = ttk.Label(self, text="HIII").pack(pady=5)
        self.display_countings()
        self.canvas.after(total_delay_step1, self.animate_sort)
        
    def random_val(self):
        for n in range(len(self.coin_values)):
            self.coin_values[n] = r.randint(self.MIN,self.MAX)
        for i, coin in enumerate(self.coins):
            tag = coin + "_txt"
            shape_tag = coin + "_shape"
            new_value = self.coin_values[i]
            self.canvas.itemconfig(tag,text=str(new_value))
            self.after(100, lambda t= shape_tag :self.canvas.itemconfig(t,width=5,outline="blue"))
            self.after(500, lambda t= shape_tag :self.canvas.itemconfig(t,width=2,outline="black"))
        self.play_sound2()

    def Shuffle(self):
        
        self.label1.config(text="Randomized")

        new_x_positions = self.coin_posx[:]
        r.shuffle(new_x_positions)

        for i, coin in enumerate(self.sortArr):
            tag = coin["coin"]
            start_y = self.coin_posy[i]
            new_x = new_x_positions[i]
            self.canvas.itemconfig(tag+"_shape",width=2,outline="black")
            # pa up
            self.canvas.after(i * 300, lambda t=tag,x=self.canvas.winfo_width()//2, y=start_y: 
                self.canvas.moveto(t, x,y - 50)
            )

            self.canvas.after(i * 300 + 150, lambda t=tag, x=new_x, y=start_y: 
                self.canvas.moveto(t, x, y - 50)
            )
            self.canvas.after(i * 300 + 150,lambda:self.play_sound(0))
           
            self.canvas.after(i * 300 + 300, lambda t=tag, x=new_x, y=start_y: 
                self.canvas.moveto(t, x, y)
            )
        self.play_sound(1)
            
    def back_button(self):
        pygame.mixer.music.unpause()
        self.valid_move.stop
        self.notif_random.stop
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu


    def display_countings(self):
        DEFAULT_Y = 100
        incn = inconvient_typing.tkInt
        incs = inconvient_typing.tkStr
        a_str = [incs("Zero"),incs("One"),incs("Two"),incs("Three"),incs("Four"),incs("Five"),
                 incs("Six"),incs("Seven"),incs("Eight"),incs("Nine"),incs("Ten")]
        a = [incn(0)]*len(self.ordered_places)
        for n,val in enumerate(self.count):
            a[n] = ttk.IntVar(value=val)
        for n in range(len(self.ordered_places)):
            lbl = ttk.Label(self, textvariable=a[n])
            lbl.place(x=self.ordered_places[n]+((self.coin_size)/2), y=DEFAULT_Y)

            lbl_str = ttk.Label(self, textvariable=a_str[n])
            lbl_str.place(x=self.ordered_places[n]+((self.coin_size)/2), y=DEFAULT_Y+20)
            self.labelcounts.append(lbl)
            self.labelcounts_Str.append(lbl_str)
        
    def moveDa_coin(self, tag, new_x, base_y, delay, done_callback=None):
        
        self.canvas.after(delay, lambda: self.canvas.moveto(tag, new_x, base_y - 40))
        self.canvas.after(delay + 200, lambda: self.canvas.moveto(tag, new_x, base_y))
        self.canvas.after(delay + 200, lambda: self.play_sound())
        if done_callback:
            self.canvas.after(delay + 250, done_callback)


    def animate_sort_step1(self):
        sorted_vals = self.coin_values[:]
        used = [0] * len(self.sortArr)
        unique_vals = sorted(set(sorted_vals))
        value_to_x = self.ordered_places[:]
        value_stacks = {val: 0 for val in unique_vals}

        delay = 0

        for value in sorted_vals:
            for i, coin in enumerate(self.sortArr):
                tag = coin["coin"]
                text_tag = tag + "_txt"
                original_val = int(self.canvas.itemcget(text_tag, "text"))

                if original_val == value and not used[i]:
                    used[i] = True
                    new_x = value_to_x[value]
                    stack_count = value_stacks[value]
                    new_y = 100 + stack_count * 30
                    value_stacks[value] += 1

                    self.moveDa_coin(tag, new_x, new_y, delay)
                    delay += 200
                    break

        return delay + 500  # return total duration so we know when step1 ends

    def animate_sort(self):
        
        sorted_vals = self.coin_values[:]  # This is CountingC.get_array()
        used = [0] * len(self.sortArr)
        delay = 0
        coin_size = 50
        gap = 20
        x_start = 150
        y_row = 100  # final row for sorted coins

        for position_index, value in enumerate(sorted_vals):
            for i, coin in enumerate(self.sortArr):
                tag = coin["coin"]
                text_tag = tag + "_txt"
                original_val = int(self.canvas.itemcget(text_tag, "text"))

                if original_val == value and not used[i]:
                    used[i] = True

                    # Current position (stacked after step1)
                    current_coords = self.canvas.coords(tag)
                    current_x = current_coords[0] if len(current_coords) >= 2 else self.coin_posx[i]
                    current_y = current_coords[1] if len(current_coords) >= 2 else self.coin_posy[i]

                    # Target position according to sorted array
                    new_x = x_start + position_index * (coin_size + gap)
                    new_y = y_row

                    self.moveDa_coin(tag, new_x, new_y, delay)
                    delay += 200
                    break
        for lbl in self.labelcounts:
            lbl.destroy()
        for lbl in self.labelcounts_Str:
            lbl.destroy()
        for coin in self.coins:
            shape_tag = coin + "_shape"
            self.after(delay, lambda t= shape_tag :self.canvas.itemconfig(t,width=5,outline="lime"))
            self.after(delay+100, lambda t= shape_tag :self.canvas.itemconfig(t,width=2,outline="black"))
        



    def play_sound(self,n=0,ms=3000):
        self.valid_move.play(loops=n)
    def play_sound2(self,n=0,ms=3000):
        self.notif_random.play(loops=n)