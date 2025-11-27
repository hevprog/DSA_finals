import ttkbootstrap as ttk

class Hanoi_ui(ttk.Frame):
    def __init__(self, parent):

        super().__init__(parent)

        ttk.Label(self, text="The Tower of HANOI").pack(pady=40)

        self.canvas = ttk.Canvas(self, width=800, height=400)
        self.canvas.pack(pady=20)

        #sticks
        self.sticks_num = 4
        self.stick_width = 25
        self.stick_height = 350
        self.stick_spacing = 200
        self.base_y = 350
        self.stick_positions = []

        #draw da LONG BROWN sticks
        for x in range(self.sticks_num):
            i = 100 + x * self.stick_spacing
            self.stick_positions.append(i)
            self.canvas.create_rectangle(i - self.stick_width // 2, self.base_y - self.stick_height, i + self.stick_width // 2, self.base_y, fill="brown")

        #The disks
        self.disks_num = 3
        self.disk_height = 20
        self.max_disk_width = 130
        self.min_disk_width = 70
        self.disks = []

        #draw disks
        for i in range(self.disks_num):
            disk_width = self.max_disk_width - i * (self.max_disk_width - self.min_disk_width) // (self.disks_num - 1)
            x = self.stick_positions[0]
            y = self.base_y - (i + 0.2) * self.disk_height
            disk = self.canvas.create_rectangle( x - disk_width // 2, y - self.disk_height, x + disk_width // 2, y, fill="yellow")
            self.disks.append(disk)
    

if __name__ == "__main__": #pag test or ig run it UI mismo
    root = ttk.Window(themename="superhero")
    root.title("Hanoi UI")
    root.geometry("800x600")
    root.resizable(False, False)

    test_window = Hanoi_ui(root)
    test_window.pack(fill="both", expand=True) # kaylangan hiya ma pack since frame man it Hanoi_ui
    
    root.mainloop()