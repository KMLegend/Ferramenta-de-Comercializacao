# main.py

import tkinter as tk
from gui import Application
from backend import Backend

class MainApplication(Application):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.backend = Backend()  # Instancie a classe Backend

if __name__ == "__main__":
    window = tk.Tk()
    app = MainApplication(master=window)
    app.mainloop()