import sys
import os
import random
import time
import winsound
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

        #track animation
        self.active_animations = 0
        self.won = False

        ttk.Button(self, text="⬅", command=self.back_button).place(x=3, y=8)

        #Bagan Welcome message, tas mawawara pag ma confirm na
        self.cfg_frame = ttk.Frame(self)
        self.cfg_frame.pack()
        ttk.Label(self.cfg_frame, text="The Tower of Hanoi",font=("Arial", 30, "bold")).pack(pady=10)
        
        self.spin_frame = ttk.Frame(self.cfg_frame)
        self.spin_frame.pack(pady=30)

        ttk.Label(self.spin_frame, text="Select the number of disks", font=("Arial", 15, "bold")).pack()
        spin = ttk.Spinbox(self.spin_frame, from_=3, to=10, textvariable=(self.disks_count))
        spin.pack(pady=10)

        ttk.Button(self.spin_frame, text="Confirm", command=self.start).pack()

        ttk.Label(self.cfg_frame, text="How to Play:", font=("Arial", 20, "bold")).pack(pady=(10, 5))
        ttk.Label(self.cfg_frame, text="1. Click a tower to select a disk", font=("Arial", 15)).pack(pady=2)
        ttk.Label(self.cfg_frame, text="2. Click another tower to move it there", font=("Arial", 15)).pack(pady=2)
        ttk.Label(self.cfg_frame, text="3. Move all disks to the colored (pink) tower", font=("Arial", 15)).pack(pady=2)
        ttk.Label(self.cfg_frame, text="4. You cannot place a larger disk on a smaller disk", font=("Arial", 15)).pack(pady=2)
        ttk.Label(self.cfg_frame, text="Good Luck!!", font=("Arial", 35, "bold")).pack(pady=30)
        ttk.Label(self.cfg_frame, text="                                                                                         ", font=("Arial", 35, "bold")).pack(pady=30)


    def start(self):
        self.won = False
        self.active_animations = 0

        #remove it nakaka ulang
        self.cfg_frame.pack_forget()
        self.start_timer()

        self.goal_tower = random.choice((1,2,3)) #The goal tower
        #towers
        self.towers_num = 4
        self.tower_width = 25
        self.tower_height = 300
        self.tower_spacing = 200
        self.base_y = 360
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

        self.canvas = ttk.Canvas(self, width=1000, height=500)
        self.canvas.pack(pady=120)

        self.draw_towers()
        self.draw_disks()

        self.highlight_tower(self.goal_tower, "lightcoral")

        #Logic
        self.disk_item = {}
        self.first_highlight = -1
        self.second_highlight = -1

        self.canvas.bind("<Button-1>", self.canvas_click)

    def canvas_click(self, event):
        if self.active_animations > 0:
            return

        #na handle hit mouse click
        tower = self.nearest_tower(event.x)
        self.play_beep(190, 100)

        if self.first_highlight == -1:
            self.first_highlight = tower
            self.highlight_tower(tower, "green")
            print(f"first clicked near tower {self.nearest_tower(event.x)}")
        else:
            self.second_highlight = tower

            #call the logic
            is_valid = self.H_logic.move_disk(self.first_highlight, self.second_highlight)
            print(is_valid)

            #return to correct color
            if self.first_highlight == self.goal_tower:
                self.highlight_tower(self.first_highlight, "lightcoral")
            else:
                self.highlight_tower(self.first_highlight, "brown")
            
            print(f"second clicked near tower {self.nearest_tower(event.x)}")

            #move the disk kun valid
            if is_valid:
                self.redraw_disks()

                disk_moved = self.H_logic.get_towers()[self.second_highlight][-1]
                moved_disk_id = self.disk_item[disk_moved]

                source_tower = self.H_logic.get_towers()[self.first_highlight]
                target_tower = self.H_logic.get_towers()[self.second_highlight]

                #x and y coords
                source_x = self.tower_positions[self.first_highlight]
                source_y =self.base_y - (len(source_tower) + 0.3) * self.disk_height 

                target_x  = self.tower_positions[self.second_highlight]
                lift_y = self.base_y - self.tower_height - 10
                drop_y = self.base_y - (len(target_tower) - 0.7) * self.disk_height

                self.animate_disks(moved_disk_id, (source_x, source_y), (source_x, lift_y), #raise the disk
                    on_done=lambda:
                        self.animate_disks(moved_disk_id, (source_x, lift_y), (target_x, lift_y), #slide the disk across
                    on_done=lambda:               
                        self.animate_disks(moved_disk_id, (target_x, lift_y), (target_x, drop_y))))#then drop the disk down
                    
                if self.is_won():
                    self.won = True
            else:
                self.play_beep(1000, 200)

            self.first_highlight = -1
            self.second_highlight = -1
            
    def nearest_tower(self, x):
        centers = self.tower_positions
        return min(range(4), key=lambda i: abs(centers[i] - x))

    def highlight_tower(self, tower, color):
        x = self.tower_positions[tower]
        self.canvas.itemconfig(self.tower_items[tower],fill=color)

    def draw_towers(self):

        #draw da LONG BROWN towers
        for x in range(self.towers_num):
            i = 200 + x * self.tower_spacing
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

                item = self.canvas.create_rectangle(x - disk_width // 2, y - self.disk_height, x + disk_width // 2, y, fill=self.get_random_color(), tags="disk")
                self.disks.append(item)     
                self.disk_item[disk_size] = item   

    def draw_disks(self):

        #draw disks
        for i in range(self.disks_num):
            disk_width = self.max_disk_width - i * (self.max_disk_width - self.min_disk_width) // (self.disks_num - 1)
            x = self.tower_positions[0]
            y = self.base_y - (i + 0.2) * self.disk_height
            disk = self.canvas.create_rectangle( x - disk_width // 2, y - self.disk_height, x + disk_width // 2, y, fill=self.get_random_color(), tags="disk")
            self.disks.append(disk)

    def animate_disks(self, disk, from_, to_,steps = 21, delay = 10, on_done=None):
        self.active_animations += 1

        x1,y1 = from_
        x2,y2 = to_

        x_left, y_top, x_right, y_bot = self.canvas.coords(disk)
        width = x_right - x_left

        dx = (x2 - x1) / steps
        dy = (y2 - y1) / steps

        
        def move(i=0):
            if i <= steps:
                #move the disk
                self.canvas.coords(disk, x1 + i * dx - width/2, y1 + i * dy - self.disk_height,x1 + i * dx + width/2,y1 + i * dy)
                self.after(delay, move, i+1)
            
            else:
                self.active_animations -= 1

                if i > steps and on_done: #para lambda functions
                    on_done()

                elif self.won and self.active_animations == 0:
                    self.after(300, self.display_win)

        move()
    
    def is_won(self):
        towers = self.H_logic.get_towers()

        #tower 0 is empty and the goal tower has all disks then player won
        return not towers[0] and len(towers[self.goal_tower]) == self.disks_num

    def display_win(self):
        self.win_frame = ttk.Frame(self)
        self.win_frame.pack()

        self.canvas.destroy()
        self.disks.clear()
        self.tower_positions.clear()

        ttk.Label(self.win_frame, text="Congratulations!!!", font="Arial").pack(padx=5, pady=10)
        ttk.Label(self.win_frame, text=f"Time {self.end_timer()}", font="Arial").pack(padx=5, pady=10)

        print(f"Time: {self.end_timer()}")

        ttk.Button(self, text="Back", command=self.back_button).pack(padx=10, pady=50)

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        if self.start_time:
            elapsed = time.time() - self.start_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            return f"{minutes:02d}:{seconds:02d}"
        return "00:00"

    def get_random_color(self):
        colors = [
            'red', 'blue', 'yellow', 'orange', 'purple', 
            'pink', 'cyan', 'magenta', 'violet',
            'lightblue', 'lightgreen',  'lightsteelblue'
        ]
        return random.choice(colors)

    def play_beep(self,frequency=1000, duration=500):
        winsound.Beep(frequency, duration)

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
        # super(self.parent.widgets()) #BUGG

if __name__ == "__main__": #pag test or ig run it UI mismo
    root = ttk.Window(themename="superhero")
    root.title("Hanoi UI")
    root.geometry("1000x600")
    root.resizable(False, False)

    test_window = Hanoi_ui(root)
    test_window.pack(fill="both", expand=True) # kaylangan hiya ma pack since frame man it Hanoi_ui
    
    root.mainloop()
