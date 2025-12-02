import sys
import os
import random
import pygame
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.stack import stack

class stack_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("C:/Users/LENOVO/Downloads/FINALS DSA\DSA_finals/files/Jeremih - oui (Official Audio).mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        
        self.text_display = ttk.StringVar()
        self.parent.attributes("-fullscreen", TRUE)
        self.tower_height = 0
        self.tower_spacing = 00
        self.base_y = 730
        self.tower_positions = 495
        self.tower_items = []
        
        
        self.disks_num = 2
        self.disk_height = 50
        self.disk_width = 255
        self.disks = []
        

        self.canvas = ttk.Canvas(self, width=1000, height=800)
        self.canvas.pack()
        
        
        ttk.Button(self,bootstyle ="danger", text="⬅️", command=self.back_button).place(x = 15, y = 15)
        ttk.Label(self, bootstyle="secondary", padding=90, text="STACK",font=("Arial Rounded MT Bold", 40, "bold")).place(relx=0.5, rely=0.1, anchor=CENTER)
        
        self.display()
        self.stack_bin()
        self.create_disk()
        self.buttonGroup()
        self.disk_push()

    def pop_SEffect(self):
        sound_effect = pygame.mixer.Sound("C:/Users/LENOVO\Downloads/FINALS DSA/DSA_finals/files/scream cut.mp3")
        sound_effect.play()
        sound_effect.set_volume(0.2)
    
    def push_SEffects(self):
        sound_effect = pygame.mixer.Sound("C:/Users/LENOVO/Downloads/FINALS DSA/DSA_finals/files/aughh shorter.mp3")
        sound_effect.play()
        sound_effect.set_volume(0.8)
        
    def createButton(self, master, text):
        if text == "SIZE":
            bootstyle = INFO
        elif text == "POP":
            bootstyle = LIGHT
        elif text == "PEEK":
            bootstyle = LIGHT
        elif text == "EMPTY CHECK":
            bootstyle= INFO
        elif text == "EXIT":
            bootstyle= DANGER
        else:
            bootstyle = LIGHT
        
                
        return ttk.Button(
            master=master,
            text=text,
            command=lambda x=text: self.buttonPress(x),
            bootstyle=bootstyle,
            width=14,
            padding=10,
            
        )
    
    def display(self):
        container = ttk.Frame(master=self, padding=2)
        container.place(relx=0.5, rely=0.775, anchor=CENTER)
        display = ttk.Label(
            master=container,
            font=("Courier New", 20, "bold"),
            textvariable=self.text_display,
            anchor=E,
        )
        display.pack(fill=X)
        
    def buttonGroup(self):
        container = ttk.Frame(master=self, padding=50)
        container.pack(expand=YES, anchor='s')
        matrix = [
                ("PUSH", "POP", "PEEK"),
                ("SIZE",  "EMPTY CHECK", "EXIT")
            ]
        for i, row in enumerate(matrix):
                container.rowconfigure(i)
                for j, num_txt in enumerate(row):
                    container.columnconfigure(j, weight=2)
                    btn = self.createButton(master=container, text=num_txt)
                    btn.grid(row=i, column=j, padx=6, pady=6)
                    
    def buttonPress(self, txt):
        if txt == "PUSH":
            self.push_SEffects()
            self.disk_push()
        elif txt == "POP":
            self.disk_pop()
        elif txt == "PEEK":
            self.disk_peek()
        elif txt == "SIZE":
            self.stack_length()
        elif txt == "EMPTY CHECK":
            self.isEmpty()
        elif txt == "EXIT":
            self.dialog()
            
    def stack_bin(self):
            self.canvas.create_line(350,300, 350,750, fill="red", width=5)  
            self.canvas.create_line(640,300, 640,750, fill="red", width=5)  
            self.canvas.create_line(348,750, 643,750, fill="red", width=15) 

        
    def create_disk(self):      
        for i in range(self.disks_num):
            disk_width = self.disk_width
            x = self.tower_positions
            y = self.base_y - (i + 0.2) * self.disk_height
            item = self.canvas.create_rectangle( x - disk_width // 2, y - self.disk_height, x + disk_width // 2, y, fill=self.get_random_color(), tags="disk")
            self.disks.append(item)      
        
    def get_random_color(self):
        colors = [
            'red', 'blue', 'yellow', 'orange', 'purple', 
            'pink', 'cyan', 'magenta', 'violet',
            'lightblue', 'lightgreen',  'lightsteelblue'
        ]
        return random.choice(colors)
    
    def disk_push(self):
        if len(self.disks) >= 8:
            self.text_display.set("STACK IS FULL")
            self.canvas.after(3000, lambda: self.text_display.set(""))
            return 
        i = len(self.disks) 
        disk_width = self.disk_width
        x = self.tower_positions
        y = self.base_y - (i + 7) * self.disk_height
        item = self.canvas.create_rectangle(x - disk_width // 2, y - self.disk_height, x + disk_width // 2,y,fill=self.get_random_color(), tags="disk")
        self.animate_drop(item)
        self.disks.append(item)  

    
    def disk_pop(self):
        if(len(self.disks)>0):
            self.pop_SEffect()
            top_disk = self.disks.pop()
            self.animate_lift(top_disk)
        else:
            self.text_display.set("STACK IS ALREADY EMPTY")
            self.canvas.after(3000, lambda: self.text_display.set(""))
        return top_disk
        
    
    def disk_peek(self):
        if(len(self.disks)>0):
            top = self.disks[-1]
            self.canvas.itemconfig(top , width=10)
        else:
            self.text_display.set("NOTHING TO PEEK")
            self.canvas.after(3000, lambda: self.text_display.set(""))
        self.canvas.after(1500, lambda: self.canvas.itemconfig(top , width=1))
        return top
    
    def stack_length(self):
        length = (f"Size: {len(self.disks)}")
        self.text_display.set(length)
        self.canvas.after(3000, lambda: self.text_display.set(""))
        
    def isEmpty(self):
        if len(self.disks) > 0:
            check = ("FALSE")
        elif len(self.disks) <= 0:
            check = ("TRUE")
        self.text_display.set(check)
        self.canvas.after(3000, lambda: self.text_display.set(""))
        
    def dialog(self):
        confirmation = messagebox.askyesno(title="WARNING!", message="You are about to terminate the program\n\nCONTINUE?")
        if confirmation == TRUE:
            sys.exit()

    def animate_drop(self, item):
        target_dx = 0       
        target_dy = 343 
        steps = 80           
        delay = 10          
        step_x = target_dx / steps
        step_y = target_dy / steps
        def smooth_step(step=0):
            if step < steps:
                self.canvas.move(item, step_x, step_y)
                self.canvas.after(delay, lambda: smooth_step(step + 1))
        smooth_step()
    
    def animate_lift(self, top_disk):
        target_dx = 0       
        target_dy = -900
        steps = 40           
        delay = 10          
        step_x = target_dx / steps
        step_y = target_dy / steps
        def smooth_step(step=0):
            if step < steps:
                self.canvas.move(top_disk, step_x, step_y)
                self.canvas.after(delay, lambda: smooth_step(step + 1))
        smooth_step()
    
        
    def back_button(self):
        pygame.mixer.music.stop()
        self.parent.destroy()
        
        
    def exit_full(self, event):
        window.attributes("-fullscreen", False)
        
        
if __name__ == "__main__":
    window = ttk.Window(
        themename="vapor",
        title="Stack",
        resizable=(FALSE, FALSE)
    )
    window.attributes("-fullscreen", True)
    test_window = stack_ui(window)
    test_window.pack(fill="both", expand=True)
        
    window.mainloop()
