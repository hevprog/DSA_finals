import ttkbootstrap as ttk
from customTheme import *

class Main_window(ttk.Window ):
    def __init__(self):
        super().__init__()

        style = self.style 
        style.register_theme(theme5_light) #change this to (theme1_light, theme2_dark, etc.)
        style.theme_use("theme5_light") #change this to the name of the theme(theme4_light, theme4_dark)

        self.title("DSA Sim")
        self.geometry("1000x600") # or mas duro dako pa like 1000x650 or 1200×700?
        self.resizable(False, False)
        self.frame = ttk.Frame(master=self)
        self.frame.pack()
        self.custom_style = ttk.Style()
        self.custom_style.configure('primary.TButton', font=('Arial', 15))

        self.widgets()

    def widgets(self):
        self.label1 = ttk.Label(self.frame, text="Data Structures and Algorithms Simulator", font=("Arial", 31, "bold"))

        self.button1 = ttk.Button(self, text="Tower of Hanoi", bootstyle="primary", width=25)
        self.button2 = ttk.Button(self, text="Counting sort", bootstyle="primary", width=25)
        self.button3 = ttk.Button(self, text="Insertion sort", bootstyle="primary", width=25)
        self.button4 = ttk.Button(self, text="Stacks", bootstyle="primary", width=25)
        self.button5 = ttk.Button(self, text="Binary search", bootstyle="primary", width=25)
        self.button6 = ttk.Button(self, text="Quit", bootstyle="danger", width=45)
        self.label1.pack(pady=20)

        self.button1.place(x=80, y=150)
        self.button2.place(x=600, y=150)
        self.button3.place(x=80, y=300)
        self.button4.place(x=600, y=300)
        self.button5.place(x=80, y=450)
        self.button6.place(x=600, y=450)
    

if __name__ == "__main__":
    window = Main_window()
    window.mainloop()



    