import os
import cv2
import sys
import json
import ctypes
import ffmpeg
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog

class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()
        self.get_json()
        self.set_menubar()

        self.fTyp=[
                  (self.lang['all_files'],self.ext['all_files']),
                  (self.lang['picture'],self.ext['picture']),
                  (self.lang['music'],self.ext['music'])
                  ]

        self.master.geometry("640x480")
        self.master.title("UnKnowKnowledge")

        #self.dark_title_bar()
        self.master.config(menu = self.menubar)

    def dark_title_bar(self):
        self.master.update()
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        set_window_attribute = ctypes.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ctypes.windll.user32.GetParent
        hwnd = get_parent(self.master.winfo_id())
        rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
        value = 2
        value = ctypes.c_int(value)
        set_window_attribute(hwnd, rendering_policy, ctypes.byref(value),ctypes.sizeof(value))

    def exit(self):
        sys.exit()

    def get_json(self):
        with open(os.path.join('setting', 'setting.json'), 'r', encoding="utf-8") as f:
            self.setting = json.load(f)
        with open(os.path.join('setting', 'ext.json'), 'r', encoding="utf-8") as f:
            self.ext = json.load(f)
        with open(os.path.join('setting', 'language', self.setting['language']+'.json'), 'r', encoding="utf-8") as f:
            self.lang = json.load(f)

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=self.fTyp, initialdir=self.setting['directory'])
        with open(os.path.join('setting', 'setting.json'), 'w', encoding="utf-8") as f:
            if os.path.dirname(filename) == '':
                pass
            else:
                self.setting['directory'] = os.path.dirname(filename)
            json.dump(self.setting, f, indent=2)
        self.preview(filename)

    def preview(self, files):
        if isinstance(files,list):
            pass
        else:
            self.canvas = tk.Canvas(self.master)
            self.canvas.pack()
            img1 = tk.PhotoImage(file=files)
            self.canvas.create_image(30,30,image=img1, anchor=tk.NW)
            self.update()


    def set_menubar(self):
        self.menubar=tk.Menu(self.master)

        self.filemenu=tk.Menu(self.menubar,tearoff=0)
        self.filemenu.add_command(label = self.lang['Open'], command = self.open_file)
        self.filemenu.add_command(label = self.lang['Exit'], command = self.exit)
        self.menubar.add_cascade(label = self.lang['File'], menu = self.filemenu)

def main():
    root=tk.Tk()
    app=Application(master=root)
    app.mainloop()

if __name__=='__main__':
    main()
