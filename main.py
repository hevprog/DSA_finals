import ttkbootstrap as ttk
from ui.ToH_ui import Hanoi_ui
from ui.Insertion_ui import InsertionUi 
from ui.Counting_ui import Counting_ui
from ui.Binary_ui import binary_ui
from ui.Stacks_ui import stack_ui

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
        self.attributes('-fullscreen', True)

        self.frame = ttk.Frame(master=self)
        self.current_frame = self.get_frame() #get the current active frame
        self.frame.pack()
        self.custom_style = ttk.Style()
        self.custom_style.configure('primary.TButton', font=('Arial', 25))
        self.custom_style.configure('danger.TButton', font=('Arial', 25))

        self.widgets()

    def widgets(self):
        self.label1 = ttk.Label(self, text="Data Structures and Algorithms Simulator", font=("Arial", 40, "bold")).place(relx=0.5, rely=0.1, anchor="center")

        self.button1 = ttk.Button(self, text="Tower of Hanoi", bootstyle="primary", width=25, padding=10)
        self.button2 = ttk.Button(self, text="Counting sort", bootstyle="primary", width=25, padding=10)
        self.button3 = ttk.Button(self, text="Insertion sort", bootstyle="primary", width=25, padding=10)
        self.button4 = ttk.Button(self, text="Stacks", bootstyle="primary", width=25, padding=10)
        self.button5 = ttk.Button(self, text="Binary search", bootstyle="primary", width=25, padding=10)
        self.button6 = ttk.Button(self, text="Quit", bootstyle="Danger", width=25, padding=10)

        self.button1.place(relx=0.3, rely=0.3, anchor="center")
        self.button2.place(relx=0.7, rely=0.3, anchor="center")
        self.button3.place(relx=0.3, rely=0.5, anchor="center")
        self.button4.place(relx=0.7, rely=0.5, anchor="center")
        self.button5.place(relx=0.3, rely=0.7, anchor="center")
        self.button6.place(relx=0.7, rely=0.7, anchor="center")
    
    #accessors to the clickable widgets
    def is_clicked_ToH(self):
        return self.button1
    
    def is_clicked_Count(self):
        return self.button2
    
    def is_clicked_Insert(self):
        return self.button3
    def is_clicked_Stacks(self):
        return self.button4

    def is_clicked_Binary(self):
        return self.button5

    def is_clicked_quit(self):
        return self.button6

#change window scenes
def switchHanoi(): #change the window to Hanoi UI
    hanoi = Hanoi_ui(window)
    window.unshow(window.get_frame())
    window.show(hanoi)
    # window.unshow_widgets() # bug
    window.current_frame = hanoi

def switchBinary(): #change to Binary UI
    binary = binary_ui(window) # bin keyword is a function
    window.show(binary)
    window.unshow(window.get_frame())
    window.current_frame = binary

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
    stack = stack_ui(window)
    window.show(stack)
    window.unshow(window.get_frame())
    window.current_frame= stack_ui


if __name__ == "__main__":
    window = Main_window()
    window.is_clicked_ToH().configure(command=switchHanoi)
    window.is_clicked_Count().configure(command=switchCounting)
    window.is_clicked_Insert().configure(command=switchInsert)
    window.is_clicked_Binary().configure(command=switchBinary)
    window.is_clicked_Stacks().configure(command=switchStacks)
    window.is_clicked_quit().configure(command=window.quit)
    window.mainloop()



    