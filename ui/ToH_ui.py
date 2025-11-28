import sys
import os
import ttkbootstrap as ttk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#temporary only, para maka run it python didi mismo

from logic.ToH_logic import Hanoi_logic

H_logic = Hanoi_logic(3)

class Hanoi_ui(ttk.Frame):

    def __init__(self, parent):

        super().__init__(parent)
        self.parent = parent
        self.disks_count = ttk.IntVar(value=3)

        ttk.Label(self, text="The Tower of HANOI").pack(pady=5)
        ttk.Button(self, text="Back", command=self.back_button).place(x=3, y=8)

        
        ttk.Label(self, text="Select the number of disks", font="Arial").pack()
        spin = ttk.Spinbox(self, from_=3, to=10, textvariable=(self.disks_count))
        spin.pack(pady=10)

        ttk.Button(self, text="Confirm", command=self.start).pack()


    
    def start(self):
        #towers
        self.towers_num = 4
        self.tower_width = 25
        self.tower_height = 350
        self.tower_spacing = 200
        self.base_y = 350
        self.tower_positions = []

        #The disks
        self.disks_num = self.disks_count.get()
        self.disk_height = 20
        self.max_disk_width = 130
        self.min_disk_width = 70
        self.disks = []

        self.canvas = ttk.Canvas(self, width=800, height=400)
        self.canvas.pack(pady=20)

        self.draw_towers()
        self.draw_disks()

    def draw_towers(self):
        #draw da LONG BROWN towers
        for x in range(self.towers_num):
            i = 100 + x * self.tower_spacing
            self.tower_positions.append(i)
            self.canvas.create_rectangle(i - self.tower_width // 2, self.base_y - self.tower_height, i + self.tower_width // 2, self.base_y, fill="brown")
        
    def draw_disks(self):
        #draw disks
        for i in range(self.disks_num):
            disk_width = self.max_disk_width - i * (self.max_disk_width - self.min_disk_width) // (self.disks_num - 1)
            x = self.tower_positions[0]
            y = self.base_y - (i + 0.2) * self.disk_height
            disk = self.canvas.create_rectangle( x - disk_width // 2, y - self.disk_height, x + disk_width // 2, y, fill="yellow")
            self.disks.append(disk)


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
