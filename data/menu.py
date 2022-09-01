__author__ ='Yatsuha'
import sys
import tkinter as tk

class Menu(tk.Frame):
    def __init__(self,master):
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)

        menubar.add_cascade(label = "ファイル", menu=filemenu)
        #master.config(menu = menubar)

    def exit(self):
        sys.exit()
