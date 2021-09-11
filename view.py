import tkinter as tk
from controller import connection


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.next = tk.Button(self)
        self.next["text"] = "next"
        self.next["command"] = self.next_song
        self.next.grid(row = 0, column = 2, padx = 10, pady= 10)
        
        self.pause_play = tk.Button(self)
        self.pause_play["text"] = "|| >"
        self.pause_play["command"] = self.prev_song
        self.pause_play.grid(row = 0, column = 1, padx = 10, pady= 10)
        
        self.prev = tk.Button(self)
        self.prev["text"] = "prev"
        self.prev["command"] = self.prev_song
        self.prev.grid(row = 0, column = 0, padx = 10, pady= 10)

        
        
    def next_song(self):
        connection("MediaControl1.Next")
        
    def prev_song(self):
        connection("MediaControl1.Previous")
        
    def play_pause(self):
        connection("MediaControl1.Previous")




root = tk.Tk()
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
