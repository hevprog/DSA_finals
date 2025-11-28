import sys
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#temporary only, para maka run it python didi mismo

from logic.ToH_logic import Hanoi_logic

class Hanoi_ui(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)
        self.parent = parent
        self.disks_count = ttk.IntVar(value=3)

        ttk.Button(self, text="Back", command=self.back_button).place(x=3, y=8)

        #Bagan Welcome message, tas mawawara pag ma confirm na
        self.cfg_frame = ttk.Frame(self)
        self.cfg_frame.pack()
        ttk.Label(self.cfg_frame, text="The Tower of HANOI",font="Arial").pack(pady=5)
        
        ttk.Label(self.cfg_frame, text="Select the number of disks", font="Arial").pack()
        spin = ttk.Spinbox(self.cfg_frame, from_=3, to=10, textvariable=(self.disks_count))
        spin.pack(pady=10)

        ttk.Button(self.cfg_frame, text="Confirm", command=self.start).pack()
    
    def start(self):

        #remove it nakaka ulang
        self.cfg_frame.pack_forget()

        #towers
        self.towers_num = 4
        self.tower_width = 25
        self.tower_height = 350
        self.tower_spacing = 200
        self.base_y = 350
        self.tower_positions = []
        self.tower_items = []

        #The disks
        self.disks_num = self.disks_count.get()
        self.disk_height = 20
        self.max_disk_width = 130
        self.min_disk_width = 70
        self.disks = []

        self.H_logic = Hanoi_logic(self.disks_count.get())

        if hasattr(self, 'canvas'):
            self.canvas.destroy()
            self.disks.clear()
            self.tower_positions.clear()

        self.canvas = ttk.Canvas(self, width=800, height=400)
        self.canvas.pack(pady=120)

        self.draw_towers()
        self.draw_disks()

        #Logic
        self.first_highlight = -1
        self.second_highlight = -1
        self.canvas.bind("<Button-1>", self.canvas_click)

    def canvas_click(self, event):
        #na handle hit mouse click
        tower = self.nearest_tower(event.x)

        if self.first_highlight == -1:
            self.first_highlight = tower
            self.highlight_tower(tower, "orange")
            print(f"first clicked near tower {self.nearest_tower(event.x)}")
        else:
            self.second_highlight = tower

            #call the logic
            is_valid = self.H_logic.move_disk(self.first_highlight, self.second_highlight)
            print(is_valid)

            self.highlight_tower(self.first_highlight, "brown")
            print(f"second clicked near tower {self.nearest_tower(event.x)}")

            #move the disk kun valid
            if is_valid:
                self.redraw_disks()

            self.first_highlight = -1
            self.second_highlight = -1
        
    def move_disks(self, to_tower):
        pass

    def nearest_tower(self, x):
        centers = self.tower_positions
        return min(range(4), key=lambda i: abs(centers[i] - x))

    def highlight_tower(self, tower, color):
        x = self.tower_positions[tower]
        self.canvas.itemconfig(self.tower_items[tower],fill=color)

    def draw_towers(self):
        
        #draw da LONG BROWN towers
        for x in range(self.towers_num):
            i = 100 + x * self.tower_spacing
            self.tower_positions.append(i)
            item = self.canvas.create_rectangle(i - self.tower_width // 2, self.base_y - self.tower_height, i + self.tower_width // 2, self.base_y, fill="brown")
            self.tower_items.append(item)

    def redraw_disks(self):

        #ig 'remove' it mga disks
        self.canvas.delete("disk")
        self.disks.clear()

        towers = self.H_logic.get_towers()

        #iterrate ngan redraw
        for tower_indx, tower in enumerate(towers):

            for disk_indx, disk_size in enumerate(tower):

                disk_width = self.max_disk_width - (disk_size-1) * (self.max_disk_width - self.min_disk_width) // (self.disks_num - 1)
                x = self.tower_positions[tower_indx]
                y = self.base_y - (disk_indx + 0.2) * self.disk_height

                item = self.canvas.create_rectangle(x - disk_width // 2,y - self.disk_height,x + disk_width // 2,y,fill="yellow", tags="disk")
                self.disks.append(item)         

    def draw_disks(self):

        #draw disks
        for i in range(self.disks_num):
            disk_width = self.max_disk_width - i * (self.max_disk_width - self.min_disk_width) // (self.disks_num - 1)
            x = self.tower_positions[0]
            y = self.base_y - (i + 0.2) * self.disk_height
            disk = self.canvas.create_rectangle( x - disk_width // 2, y - self.disk_height, x + disk_width // 2, y, fill="yellow", tags="disk")
            self.disks.append(disk)

    #helper functions para mag back to main
    def get_frame(self):
        return self.frame
    
    def unshow(self,frame:ttk.Frame):
        frame.forget()

    def show(self, frame:ttk.Frame):
        frame.pack()
        frame.tkraise()

    def back_button(self):
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu

if __name__ == "__main__": #pag test or ig run it UI mismo
    root = ttk.Window(themename="superhero")
    root.title("Hanoi UI")
    root.geometry("800x600")
    root.resizable(False, False)

    test_window = Hanoi_ui(root)
    test_window.pack(fill="both", expand=True) # kaylangan hiya ma pack since frame man it Hanoi_ui
    
    root.mainloop()
