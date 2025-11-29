import tkinter as tk
import ttkbootstrap as ttk
from logic.bin import binarySEARCH

class binary_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.root = parent
        ttk.Label(self, text="Enter target number:").pack(pady=5)
        self.target_number = ttk.Entry(self, width=20)
        self.target_number.pack(pady=5)

        search_btn = ttk.Button(self, text="Run Binary Search", command=self.Run_Search, bootstyle="success")
        search_btn.pack(pady=10)

        self.output_text = tk.Text(self, height=15, width=70)
        self.output_text.pack(pady=10)
        ttk.Button(self,text="back to menu").pack()
        
    def Sort_Input(self):
        arr = self.arr_entry.get()
        try:
            unsorted_arr = list(map(int, arr.split(",")))
            unsorted_arr.sort()
           
            self.arr_entry.delete(0, tk.END)
            self.arr_entry.insert(0, ",".join(map(str, unsorted_arr)))

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Sorted Array: {arr}\n")
        except ValueError:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid input. Please enter integers only.")

    def Run_Search(self):
        arr_text = self.arr_entry.get()
        target_text = self.target_number.get()

        try:
            arr = list(map(int, arr_text.split(",")))
            arr.sort()
            target = int(target_text)

            index, steps = self.Binary_Search(arr, target)

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Array: {arr}\nTarget: {target}\n\n")
            for step in steps:
                self.output_text.insert(tk.END, step + "\n")

        except ValueError:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid input. Please enter integers only.")
    
    def back_button():
        return ttk.button