import sys
import os
import random
import time
import winsound
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.stack import stack

class stack_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        ttk.Button(self,bootstyle ="danger", text="back to menu").place(x = 15, y = 15)
        ttk.Label(self,  bootstyle="secondary", text="STACK",font=("Arial Rounded MT Bold", 40, "bold")).place(relx=0.5, rely=0.155, anchor=CENTER)
        
        self.buttonGroup()
    
    def create_button(self, master, text):
        if text == "SIZE":
            bootstyle = INFO
        elif text == "EMPTY CHECK":
            bootstyle= INFO
        elif text == "RESET":
            bootstyle= DANGER
        else:
            bootstyle = LIGHT
        return ttk.Button(
            master=master,
            text=text,
            #command=lambda x=text: self.on_button_pressed(x),
            bootstyle=bootstyle,
            width=14,
            padding=10,
        )
        
    def buttonGroup(self):
        container = ttk.Frame(master=self, padding=50)
        ttk.Frame.place(self, x=100, y=50)
        container.pack(expand=YES, anchor='s')
        matrix = [
                ("PUSH", "POP", "PEEK"),
                ("SIZE",  "EMPTY CHECK", "RESET")
            ]
        for i, row in enumerate(matrix):
                container.rowconfigure(i)
                for j, num_txt in enumerate(row):
                    container.columnconfigure(j, weight=2)
                    btn = self.create_button(master=container, text=num_txt)
                    btn.grid(row=i, column=j, padx=6, pady=6)
    
if __name__ == "__main__":
    window = ttk.Window(
        themename="vapor",
        title="Stack",
        resizable=(False, False)
    )
    window.geometry("800x600")
        
    test_window = stack_ui(window)
    test_window.pack(fill="both", expand=True)
        
    window.mainloop()
        
    
    
