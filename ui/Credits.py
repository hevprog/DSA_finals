import ttkbootstrap as ttk

class credits(ttk.Frame):
    label_pad = 5
    
    def __init__(self, parent):
        super().__init__(parent)

        font_size =15
        bgframe = ttk.Frame(self,width=1000,height=600)
        
        self.parent = parent
        title = ttk.Label(self,text="Programmers",font=('Verdana', font_size*2), style="secondary")
        ToH = ttk.Label(self,text="Kent Andrew Parejas - Tower of Hanoi",font=('Verdana', font_size))
        CountingS = ttk.Label(self,text="Henry Singzon - Counting sort",font=('Verdana', font_size))
        InsertS = ttk.Label(self,text="Nico Timothy Babaylan - Insert sort",font=('Verdana', font_size))
        BinSearch = ttk.Label(self,text="Michael Andre Pacheco - Binary Search",font=('Verdana', font_size))
        Stacks = ttk.Label(self,text="John Reymark Binghoy - Stack",font=('Verdana', font_size))

        DSA = ttk.Label(self, text="Data Structure and Algorithms",font=('Verdana', font_size*2),style="warning")
        instructor = ttk.Label(self, text="Sir Ricky James Nuevas- DSA instructor",font=('Verdana', font_size))
        back = ttk.Button(self,text="Back to menu",command=self.back_button,style="danger")

        
        title.pack(pady= self.label_pad)
        ToH.pack(pady= self.label_pad)
        CountingS.pack(pady= self.label_pad)
        InsertS.pack(pady= self.label_pad)
        BinSearch.pack(pady= self.label_pad)
        Stacks.pack(pady= self.label_pad)
        back.pack(side="bottom",pady= 10)
        instructor.pack(pady=10, side="bottom")
        DSA.pack(side="bottom",pady=self.label_pad)
        
        bgframe.pack()

    def back_button(self):
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu