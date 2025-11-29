import ttkbootstrap as ttk

class binary_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text="This is the binary search").pack()
        ttk.Button(self,text="back to menu").pack()
    
