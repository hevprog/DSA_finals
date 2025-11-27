import ttkbootstrap as ttk
from ui.ToH_ui import Hanoi_ui

class Main_window(ttk.Window):

    def __init__(self):
        super().__init__(themename="superhero") # puydi kita mag darkly or cyborg na theme, kamo bahala
        self.title("Testing")
        self.geometry("800x600") # or mas duro dako pa like 1000x650 or 1200×700?
        self.resizable(False, False)

        label1 = ttk.Label(master=self, text="Tower of Hanoi")
        label1.pack()

        button1 = ttk.Button(master=self, text="Click meee")
        button1.pack()



if __name__ == "__main__":
    window = Main_window()
    window.mainloop()
     