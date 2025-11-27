import ttkbootstrap as ttk
from ui.ToH_ui import Hanoi_ui


#basic operations with the frame
#get_frame()**returns a frame of the inherited class
class frame_ops: 
    frame:ttk.Frame
    def get_frame(self):
        return self.frame
    def unshow(self,frame:ttk.Frame):
        frame.forget()
    def show(self, frame:ttk.Frame):
        frame.pack()
        frame.tkraise()

class Main_window(ttk.Window,frame_ops):
    def __init__(self):
        super().__init__(themename="superhero") # puydi kita mag darkly or cyborg na theme, kamo bahala
        self.title("Testing")
        self.geometry("800x600") # or mas duro dako pa like 1000x650 or 1200×700?
        self.resizable(False, False)
        self.frame = ttk.Frame(master=self)

    def widgets(self):
        self.label1 = ttk.Label(self.frame, text="Main menu")
        self.button1 = ttk.Button(self.frame, text="Tower of Hanoi")
        self.button2 = ttk.Button(self.frame, text="Counting sort")
        self.button3 = ttk.Button(self.frame, text="Insertion sort")
        self.button4 = ttk.Button(self.frame, text="Stacks")
        self.button5 = ttk.Button(self.frame, text="Binary search")
        self.button6 = ttk.Button(self.frame, text="Quit", bootstyle="outline button")
        self.frame.pack()
        self.label1.pack()
        pad= 5
        self.button1.pack(pady=pad);self.button2.pack(pady=pad);self.button3.pack(pady=pad)
        self.button4.pack(pady=pad);self.button5.pack(pady=pad);self.button6.pack(pady=pad)
    
    #accessors to the clickable widgets
    def is_clicked_ToH(self):
        return self.button1
    def is_clicked_Count(self):
        pass
    def is_clicked_Insert(self):
        pass
    def is_clicked_Stacks(self):
        pass
    def is_clicked_Binary(self):
        pass
    def is_clicked_quit(self):
        return self.button6
    

#change window scenes
def switchHanoi(): #change the window to Hanoi UI
    hanoi = Hanoi_ui(window)
    window.show(hanoi)
    window.unshow(window.get_frame())
def switchBinary(): #change tp Binary UI
    pass
def switchCounting(): #change to counting UI
    pass
def switchInsert(): #change to Insert UI
    pass
def switchStacks(): #change to Stacks UI
    pass

if __name__ == "__main__":
    window = Main_window()
    window.widgets()
    window.is_clicked_ToH().configure(command=switchHanoi)
    window.is_clicked_quit().configure(command=window.quit)
    window.mainloop()