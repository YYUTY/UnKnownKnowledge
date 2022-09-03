__author__  = 'Yatsuha'

import os
import sys
import json
import data
import tkinter as tk
from tkinter import messagebox

def update(master):
    master.after(20,update,master)
    if data.va.fin[len(data.va.fin)-1]:
        sys.exit()

def main():
    root.after(20,update,root)
    root.iconbitmap(default=os.path.join(data.va.path, 'resource\\icon.ico'))
    root.title('UnKnownKnowledge')
    root.geometry('600x150')
    root.mainloop()

if __name__ == '__main__':
    data.va.path = os.path.dirname(sys.argv[0])
    root=tk.Tk()
    data.Menu(root)
    try:
        extension = os.path.splitext(sys.argv[1])[1]
    except:
        root.withdraw()
        messagebox.showerror('エラー', '変換するファイルが選択されていません。')
    if not len(sys.argv) == 0:
        if extension in data.va.music:
            data.MusicConverts(root, sys.argv[1])
        if extension in data.va.movies:
            data.MovieConverts(root, sys.argv[1])
    main()
