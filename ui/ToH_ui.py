import ttkbootstrap as ttk

class Hanoi_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Label(self, text="123456").pack(pady=40)

        ttk.Button(self, text="A button").pack(pady=20)


if __name__ == "__main__": #pag test 
    root = ttk.Window(themename="superhero")
    root.title("Hanoi test")
    root.geometry("800x600")
    root.resizable(False, False)

    test_window = Hanoi_ui(root).pack() # so kaylangan hiya ma pack since frame man it Hanoi_ui
    root.mainloop()