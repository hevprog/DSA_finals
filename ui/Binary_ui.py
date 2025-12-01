import ttkbootstrap as ttk
from tkinter import Label
import threading
from logic.binary import BinarySearchLogic

class Binary_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        self.logic = BinarySearchLogic(delay=1)

        self.arr = [1,2,3,4,5,6,7,8,9,10]
        self.target = None

        self.label_widgets = []
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self, text="Binary Search Visualizer")
        title.pack(pady=20)
        ttk.Button(self,text="back to menu",command=self.back_button).pack(pady=20)
        # Input field
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Enter target value: ").pack(side="left", padx=5)
        ttk.Canvas(self,width=1000,height=200).pack()
        self.target_entry = ttk.Entry(input_frame, width=10)
        self.target_entry.pack(side="left")

        container = ttk.Frame(self)
        container.pack(pady=20)

        # Create number labels
        for num in self.arr:
            lbl = Label(container, text=str(num), width=5, height=2, relief="groove",bg="white")
            lbl.pack(side="left", padx=5)
            self.label_widgets.append(lbl)

        start_btn = ttk.Button(self, text="Start Search", bootstyle="primary",
                               command=self.start_visualization)
        start_btn.pack(pady=20)

    def ui_callback(self, index, state):
        if state == "reset":
            for lbl in self.label_widgets:
                if lbl.cget("bg") not in ("red", "green"):
                    lbl.config(bg="white")

        elif state == "highlight":
            self.label_widgets[index].config(bg="yellow")

        elif state == "found":
            self.label_widgets[index].config(bg="green")

        elif state == "left_red":
            for i in range(0, index + 1):
                self.label_widgets[i].config(bg="red")

        elif state == "right_red":
            for i in range(index, len(self.label_widgets)):
                self.label_widgets[i].config(bg="red")

    def start_visualization(self):

        # Validate input
        try:
            val = int(self.target_entry.get())
            self.target = val
        except ValueError:
            # highlight input box in red for invalid input
            self.target_entry.delete(0, "end")
            self.target_entry.insert(0, "Invalid")
            return
        
        # Reset colors before new search
        for lbl in self.label_widgets:
            lbl.config(bg="white")

        threading.Thread(
            target=self.logic.run_search, 
            args=(self.arr, self.target, self.ui_callback),
            daemon=True
        ).start()

    def back_button(self):
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu
        