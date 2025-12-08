import ttkbootstrap as ttk
from logic.insertion import insertion
import random as r
import pygame

class InsertionUi(ttk.Frame):
    MIN = 0
    MAX = 9

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        pygame.mixer.init()
        self.valid_move = pygame.mixer.Sound('ui/sounds/select.wav')
        try:
            self.notif_random = pygame.mixer.Sound('ui/sounds/notify.wav')
        except Exception:
            self.notif_random = None
        pygame.mixer.music.pause()

        ttk.Label(self, text="This is the Insertion sort").pack(pady=10)
        ttk.Button(self, text="back to menu", command=self.back_button).pack()
        ttk.Button(self, text="Sort", command=self.sorting).pack(side="bottom", pady=10)
        ttk.Label(self, text="Insertion Sort").pack(side="bottom")
        self.Label1 = ttk.Label(self)
        self.Label1.pack(pady=5, side="bottom")
        ttk.Button(self, text="Randomize", command=self.Shuffle).pack(side="bottom", pady=20)

        self.canvas = ttk.Canvas(self, width=1000, height=500)
        self.canvas.pack(pady=5)

        self.labelCounts = []
        self.labelCountsStr = []
        self.sortedArr = []
        self.coins = ["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"]

        self.coin_values = [63, 22, 12, 23, 45, 34, 11, 23, 78, 99]

        # visual positions
        self.coin_pos_x = []
        self.coin_pos_y = []

        x_start = 50
        y_pos = 100
        self.coin_size = 50
        gap = 20
        self.base_y = y_pos

        for i, value in enumerate(self.coin_values):
            x1 = x_start + i * (self.coin_size + gap)
            y1 = y_pos
            x2 = x1 + self.coin_size
            y2 = y_pos + self.coin_size
            tag = self.coins[i]

            self.canvas.create_oval(x1, y1, x2, y2,
                                    fill="pink" if value % 2 == 0 else "lightgreen",
                                    width=2, tags=(tag, tag + "_shape"))
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2
            self.canvas.create_text(center_x, center_y, text=str(value),
                                    font=("Helvetica", 16, "bold"),
                                    tags=(tag, tag + "_txt"))

            self.sortedArr.append({"x": x1, "coin": tag})
            self.coin_pos_x.append(x1)
            self.coin_pos_y.append(y1)

        self.xslots = self.coin_pos_x[:]

        self.positions = self.coins[:]

        self.current_time = 0
        self.step_dt = 200 

        self.color_key = "yellow"
        self.color_compare = "orange"
        self.color_sorted = "lightgreen"
        self.color_default_even = "pink"
        self.color_default_odd = "lightgreen"

    def play_sound(self):
        try:
            self.valid_move.play()
        except Exception:
            pass

    def play_sound2(self, n=0):
        if self.notif_random:
            try:
                self.notif_random.play(loops=n)
            except Exception:
                pass

    def back_button(self):
        pygame.mixer.music.unpause()
        self.parent.unshow(self)
        main_menu = self.parent.get_frame()
        self.parent.show(main_menu)
        self.parent.current_shown_frame = main_menu

    def reset_colors(self):
        for idx, tag in enumerate(self.positions):
            value = self.coin_values[idx]
            fill = self.color_default_even if value % 2 == 0 else self.color_default_odd
            try:
                self.canvas.itemconfig(tag + "_shape", fill=fill, outline="black")
            except Exception:
                # fallback if only tag exists
                self.canvas.itemconfig(tag, fill=fill, outline="black")

    def schedule(self, func, dt=None):
        if dt is None:
            dt = self.step_dt
        self.canvas.after(self.current_time, func)
        self.current_time += dt

    def moveto_tag(self, tag, x, y):
        try:
            self.canvas.moveto(tag, x, y)
        except Exception:
            try:
                bbox = self.canvas.bbox(tag)
                if bbox:
                    current_x = bbox[0]
                    current_y = bbox[1]
                    dx = x - current_x
                    dy = y - current_y
                    self.canvas.move(tag, dx, dy)
                else:
                    items = self.canvas.find_withtag(tag)
                    if items:
                        self.canvas.move(items[0], x, y)
            except Exception:
                pass

    def lift_and_place(self, tag, slot_idx):
        target_x = self.xslots[slot_idx]
        lift_y = self.base_y - 60

        def lift():
            self.moveto_tag(tag, target_x, lift_y)

        def drop():
            self.moveto_tag(tag, target_x, self.base_y)
            self.play_sound()

        self.schedule(lambda: lift())
        self.schedule(lambda: drop())


    def Shuffle(self):
        self.Label1.config(text="Randomized")

        new_order = self.coins[:]
        r.shuffle(new_order)

        self.current_time = 0
        for idx, tag in enumerate(new_order):
            target_x = self.xslots[idx]
            def make_move(t=tag, tx=target_x, i=idx):
                self.moveto_tag(t, tx, self.base_y - 60)
            self.schedule(lambda t=tag, tx=target_x: self.moveto_tag(t, tx, self.base_y - 60))
            self.schedule(lambda t=tag, tx=target_x: self.moveto_tag(t, tx, self.base_y))
            self.schedule(lambda: self.play_sound())

        tag_to_value = {}
        for i, t in enumerate(self.positions):
            tag_to_value[t] = self.coin_values[i]
        new_values = [tag_to_value[t] for t in new_order]
        def commit():
            self.positions = new_order[:]
            self.coin_values = new_values[:]
            self.reset_colors()
            self.play_sound2()
        self.schedule(commit)

        self.current_time += 50

    def sorting(self):
    
        self.Label1.config(text="Sorting (animated)")
        insertionC = insertion(self.coin_values[:])  
        insertionC.sort()
        self.animate_insertion()

    def animate_insertion(self):

        self.current_time = 0
        self.reset_colors()

        n = len(self.coin_values)
        arr = self.coin_values[:]     
        pos = self.positions[:]      

        # Helper to mark a tag's shape color
        def color_shape(tag, color):
            try:
                self.canvas.itemconfig(tag + "_shape", fill=color)
            except Exception:
                self.canvas.itemconfig(tag, fill=color)

        if n > 0:
            color_shape(pos[0], self.color_sorted)

        for i in range(1, n):
            key_val = arr[i]
            key_tag = pos[i]

            def lift_key(tag=key_tag, idx=i):
                color_shape(tag, self.color_key)
                self.moveto_tag(tag, self.xslots[idx], self.base_y - 60)
            self.schedule(lift_key)

            j = i - 1
            while j >= 0 and arr[j] > key_val:
                arr[j+1] = arr[j]

                tag_shift = pos[j]

                def mark_compare(t=tag_shift):
                    color_shape(t, self.color_compare)
                self.schedule(mark_compare)

                def move_shift(t=tag_shift, dest=j+1):
                    self.moveto_tag(t, self.xslots[dest], self.base_y)
                    self.play_sound()
                self.schedule(move_shift)

                def unmark(t=tag_shift, idxj=j):
                    pass
                self.schedule(lambda: None)

                pos[j+1] = tag_shift

                j -= 1

            insert_idx = j + 1
            arr[insert_idx] = key_val
            pos[insert_idx] = key_tag

            def drop_key(tag=key_tag, idx=insert_idx):
                self.moveto_tag(tag, self.xslots[idx], self.base_y)
                self.play_sound()
                color_shape(tag, self.color_sorted)
            self.schedule(drop_key)

            def recolor_sorted(up_to=i):
                for k in range(0, up_to + 1):
                    try:
                        ttag = pos[k]
                        color_shape(ttag, self.color_sorted)
                    except Exception:
                        pass
            self.schedule(lambda up=i: recolor_sorted(up))

        def commit_final():
            self.coin_values = arr[:]
            self.positions = pos[:]
            self.Label1.config(text="Sorted")
            for t in self.positions:
                try:
                    color_shape(t, self.color_sorted)
                except Exception:
                    pass
        self.schedule(commit_final)

        self.schedule(lambda: self.play_sound2() if self.notif_random else self.play_sound(), dt=300)