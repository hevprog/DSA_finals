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

        #draw da LONG BROWN sticks
        for x in range(self.sticks_num):
            i = 100 + x * self.stick_spacing
            self.canvas.create_rectangle(i - self.stick_width // 2, self.base_y - self.stick_height, i + self.stick_width // 2, self.base_y, fill="brown")


if __name__ == "__main__": #pag test or ig run it UI mismo
    root = ttk.Window(themename="superhero")
    root.title("Hanoi UI")
    root.geometry("800x600")
    root.resizable(False, False)

    test_window = Hanoi_ui(root)
    test_window.pack(fill="both", expand=True) # kaylangan hiya ma pack since frame man it Hanoi_ui
    
    root.mainloop()