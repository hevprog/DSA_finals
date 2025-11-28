import ttkbootstrap as ttk


class Counting_ui(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        
        ttk.Label(self, text="This is counting sort").pack(pady= 10)
        ttk.Button(self,text="back to menu",command=self.back_button).pack()
        self.canvas = ttk.Canvas(self, width= 750,height= 500)
        self.canvas.pack(pady=5)


        self.coin_values = [1,1,5,2,4,4]
        self.coin_items = []
        x_start = 50
        y_pos = 100
        coin_size = 50
        gap = 20
        
        #to create and desplay coins
        for i, value in enumerate(self.coin_values):
            x1 = x_start + i * (coin_size + gap)
            y1 = y_pos
            x2 = x1 + coin_size
            y2 = y_pos + coin_size
            
            oval_id = self.canvas.create_oval(x1, y1, x2, y2, fill="gold", width=2)
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            text_id = self.canvas.create_text(center_x, center_y, text=str(value), font=("Helvetica", 16, "bold"))
            self.coin_items.append({"value": value, "oval_id": oval_id, "text_id": text_id})
            
    def back_button(self):
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu
    

if __name__ == "__main__": #pag test or ig run it UI mismo
    root = ttk.Window(themename="superhero")
    root.title("Hanoi UI")
    root.geometry("800x600")
    root.resizable(False, False)

    test_window = Counting_ui(root)
    test_window.pack(fill="both", expand=True) # kaylangan hiya ma pack since frame man it Hanoi_ui
    
    root.mainloop()