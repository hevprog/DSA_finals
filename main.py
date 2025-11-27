import ttkbootstrap as ttk

window = ttk.Window(themename="superhero") # puydi kita mag darkly or cyborg na theme, kamo bahala
window.title("Testing")
window.geometry("800x600") # or mas duro dako pa like 1000x650 or 1200×700?
window.resizable(False, False)

label1 = ttk.Label(master=window, text="Tower of Hanoi")
label1.pack()

button1 = ttk.Button(master=window, text="Click meee")
button1.pack()

if __name__ == "__main__":
    window.mainloop()    