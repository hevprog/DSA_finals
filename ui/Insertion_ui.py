import ttkbootstrap as ttk

class Hanoi_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text="This is the Insertion sort").pack()
        ttk.Button(self,text="back to menu").pack()
    
