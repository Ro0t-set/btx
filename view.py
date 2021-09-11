import tkinter as tk
import controller


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        

    def create_widgets(self):
        self.next = tk.Button(self)
        self.next["text"] = "next"
        self.next["command"] = controller.connection("MediaPlayer1.Next")
        self.next.pack(side="top")




root = tk.Tk()
root.geometry("400x400")
app = Application(master=root)
app.mainloop()
