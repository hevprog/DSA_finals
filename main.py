import ttkbootstrap as ttk
from ui.ToH_ui import Hanoi_ui
from ui.Insertion_ui import InsertionUi 
from ui.Counting_ui import Counting_ui
from ui.Binary_ui import binary_ui

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
        super().__init__(themename="vapor") # puydi kita mag darkly or cyborg na theme, kamo bahala
        self.title("DSA Sim")
        self.geometry("1000x600") # or mas duro dako pa like 1000x650 or 1200×700?
        self.resizable(False, False)
        self.frame = ttk.Frame(master=self)
        self.current_frame = self.get_frame() #get the current active frame
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
        self.button6 = ttk.Button(self, text="Quit", bootstyle="outline button", width=25)
        self.label1.pack(pady=20)

        self.button1.place(x=80, y=150)
        self.button2.place(x=600, y=150)
        self.button3.place(x=80, y=300)
        self.button4.place(x=600, y=300)
        self.button5.place(x=80, y=450)
        self.button6.place(x=600, y=450)

    def unshow_widgets(self):
        self.label1.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
    
    #accessors to the clickable widgets
    def is_clicked_ToH(self):
        return self.button1
    
    def is_clicked_Count(self):
        return self.button2
    
    def is_clicked_Insert(self):
        return self.button3
    def is_clicked_Stacks(self):
        pass

    def is_clicked_Binary(self):
        return self.button5

    def is_clicked_quit(self):
        return self.button6

    

#change window scenes
def switchHanoi(): #change the window to Hanoi UI
    hanoi = Hanoi_ui(window)
    window.unshow(window.get_frame())
    window.show(hanoi)
    window.unshow_widgets()
    window.current_frame = hanoi

def switchBinary(): #change to Binary UI
    pass

def switchCounting(): #change to counting UI
    Counting= Counting_ui(window)
    window.show(Counting)
    window.unshow(window.get_frame())
    window.current_frame=Counting

def switchInsert(): #change to Insert UI
    insertion = InsertionUi(window)
    window.show(insertion)
    window.unshow(window.get_frame())
    window.current_frame= InsertionUi
def switchStacks(): #change to Stacks UI
    pass

if __name__ == "__main__":
    window = Main_window()
    window.is_clicked_ToH().configure(command=switchHanoi)
    window.is_clicked_Count().configure(command=switchCounting)
    window.is_clicked_quit().configure(command=window.quit)
    window.mainloop()