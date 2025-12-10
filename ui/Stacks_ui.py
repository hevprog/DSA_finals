import sys
import os
import random
import pygame
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox



sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



class stack_ui(ttk.Frame):
    def __init__(self, parent, on_hanoi, on_counting, on_insertion, on_binary):
        super().__init__(parent)
        self.parent = parent
        self.on_hanoi_switch = on_hanoi
        self.on_counting_switch = on_counting
        self.on_insertion_switch = on_insertion
        self.on_binary_switch = on_binary
        
        pygame.mixer.music.unload()
        pygame.mixer.music.load("ui/sounds/Jeremih - oui (Official Audio).mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        self.custom_style = ttk.Style()
        self.custom_style.configure('danger.TButton', font=('Verdana', 8))
        self.menu_style = ttk.Style()
        
        
        self.text_display = ttk.StringVar()
        self.project_textDisplay = ttk.StringVar()
        self.parent.attributes("-fullscreen", True)
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
        
        
        
        ttk.Label(self, bootstyle="secondary", padding=90, text="STACK",font=("Arial Rounded MT Bold", 40, "bold")).place(relx=0.5, rely=0.15, anchor=CENTER)
        
        self.project_display()
        self.display()
        self.stack_bin()
        self.create_disk()
        self.buttonGroup()
        self.top_menu()
        
    def top_menu(self):
        
        self.menu_style.configure('colorFrame.TFrame', background='#140224')
        container = ttk.Frame(self, style='colorFrame.TFrame')
        container.place(relx=0.5, rely=0, anchor='n', width=2000, height=45)
        
        title = ttk.Label(master=container, text="DSA FINALS (STACKS) - John Reymark Binghoy", bootstyle="light", font=("Times New Roman", 12, "bold"))
        ttk.Button(master=container, bootstyle ="danger", text="❌", command=self.exit_full).place(relx=0.965, rely=0.5, anchor='center')
        title.place(relx=0.5, rely=0.5, anchor=CENTER)
        menu = ttk.Menubutton(
                            master=container,
                            bootstyle="info-outline",
                            text="MENU"
                            )
        menu.place(relx=0.08, rely=0.5, anchor='center')
        options_menu = ttk.Menu(menu) 
        options_menu.add_radiobutton(label="Tower of Hanoi", command=self.switch_toHanoi)
        options_menu.add_radiobutton(label="Counting Sort", command=self.switch_toCounting)
        options_menu.add_radiobutton(label="Insertion sort", command=self.switch_toInsertion )
        options_menu.add_radiobutton(label="Binary Search", command=self.switch_toBinary)
        options_menu.add_radiobutton(label="Exit", command=sys.exit)
        menu["menu"] = options_menu
        
        project = ttk.Menubutton(
                            master=container,
                            bootstyle="info-outline",
                            text="PROJECT"
                            )
        project.place(relx=0.12, rely=0.5, anchor='center')
        project_menu = ttk.Menu(project)
        project_menu.add_radiobutton(label="Contributors", command=self.contributors)
        project_menu.add_radiobutton(label="About", command=self.about)
        project_menu.add_radiobutton(label="Clear", command=self.clear)
        project["menu"] = project_menu
        
        ttk.Button(master=container,bootstyle ="danger", text="⬅️", command=self.back_button).place(relx=0.04, rely=0.5, anchor='center')
        
    def contributors(self):
        self.project_textDisplay.set("Henry V Singzon\nKent Andrew Parejas\nMichael Andre Pacheco\nNico Timothy Babaylan\nJohn Reymark Binghoy" )
    
    def about(self):
        self.project_textDisplay.set("Data Structures and Algorithms \nSimulator\n\nDSA FINALS\nIn compliance to Sir Ricky Nuevas\n\nFor the subject\nData Strucutres and Algorithms")
            
    def clear(self):
        self.project_textDisplay.set("")
        
    def project_display(self):
        container = ttk.Frame(master=self, padding=2)
        container.place(relx=0.78, rely=0.5, anchor=CENTER)
        display = ttk.Label(
            master=container,
            font=("Verdana", 20, "bold"),
            justify=CENTER,
            textvariable=self.project_textDisplay,
            anchor=E,
        )
        display.pack(fill=X)
        
    def pop_SEffect(self):
        sound_effect = pygame.mixer.Sound("ui/sounds/scream cut.mp3")
        sound_effect.play()
        sound_effect.set_volume(0.2)
    
    def push_SEffects(self):
        sound_effect = pygame.mixer.Sound("ui/sounds/aughh shorter.mp3")
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
        self.push_SEffects()
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
        8
    def isEmpty(self):
        if len(self.disks) > 0:
            check = ("FALSE")
        elif len(self.disks) <= 0:
            check = ("TRUE")
        self.text_display.set(check)
        self.canvas.after(3000, lambda: self.text_display.set(""))
        
    def dialog(self):
        confirmation = messagebox.askyesno(title="WARNING!", message="You are about to terminate the program\n\nCONTINUE?" )
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
        self.custom_style.configure('danger.TButton', font=('Arial', 15))
        pygame.mixer.music.unload()
        pygame.mixer.music.load("ui/sounds/main_background_music.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        self.parent.destroy()
        
    def switch_toHanoi(self):
        self.custom_style.configure('danger.TButton', font=('Arial', 15))
        self.on_hanoi_switch()
        self.parent.destroy()
    
    def switch_toBinary(self):
        self.custom_style.configure('danger.TButton', font=('Arial', 15))
        self.on_binary_switch()
        self.parent.destroy()
        
    def switch_toCounting(self):
        self.custom_style.configure('danger.TButton', font=('Arial', 15))
        self.on_counting_switch()
        self.parent.destroy()
        
    def switch_toInsertion(self):
        self.custom_style.configure('danger.TButton', font=('Arial', 15))
        self.on_insertion_switch()
        self.parent.destroy()
        
        
    def exit_full(self):
        self.parent.attributes("-fullscreen", False)
        
        
if __name__ == "__main__":
    window = ttk.Window(
        themename="vapor",
        title="Stack",
        resizable=(FALSE, FALSE)
    )
    pygame.init()
    pygame.mixer.init()
    window.attributes("-fullscreen", True)
    test_window = stack_ui(window)
    test_window.pack(fill="both", expand=True)
        
    window.mainloop()
