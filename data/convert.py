__author__ = 'Yatsuha'
import os
import re
import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk as ttk

class Converts(tk.Frame):
    def __init__(self, master, filepath):
        self.path = self.path_get(filepath)
        self.old_path = self.path_get(filepath)
        self.set_dir(master)
        self.set_filename(master)
        self.set_extension(master)
        #self.convert()

    def convert(self):
        ffmpeg_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'ffmpeg\\ffmpeg.exe')
        old_file = self.old_path[0]
        new_file = os.path.join(str(self.old_path[1]),'intro.wav')
        subprocess.call([str(ffmpeg_path),'-i',old_file,new_file])

    def get_filedialog(self):
        iDir = os.path.abspath(os.path.dirname(self.path[0]))
        iDirPath = filedialog.askdirectory(initialdir = iDir)
        self.dir.set(iDirPath)
        self.path[1] = iDirPath

    def get_filename(self):
        iDir = os.path.abspath(os.path.dirname(self.path[0]))
        filename = os.path.basename(filedialog.askopenfilename(initialdir = iDir))
        self.file.set(filename)
        self.path[2] = filename

    def path_get(self,filepath):
        paths = [filepath,os.path.dirname(filepath), os.path.basename(filepath)]
        return paths

    def set_dir(self,master):
        dirframe = ttk.Frame(master)
        dirframe.pack()
        IDirLabel = ttk.Label(dirframe, text="フォルダ参照＞＞", padding=(5, 2))
        IDirLabel.pack(pady = 10, anchor = tk.NW, side = 'left')

        self.dir = tk.StringVar()
        self.dir.set(self.path[1])

        IDirEntry = ttk.Entry(dirframe,textvariable=self.dir, width=70)
        IDirEntry.pack(pady = 11,ipady = 1, anchor = tk.NW, side = 'left')

        IDirButton = ttk.Button(dirframe, text="参照", command=self.get_filedialog)
        IDirButton.pack(pady = 10, anchor = tk.NW, side = 'left')

    def set_filename(self,master):
        fileframe = ttk.Frame(master)
        fileframe.pack()
        IFileLabel = ttk.Label(fileframe, text="　ファイル名＞＞", padding=(5, 4))
        IFileLabel.pack(pady = 5, anchor = tk.NW, side = 'left')

        self.file = tk.StringVar()
        self.file.set(self.path[2])

        IFileEntry = ttk.Entry(fileframe,textvariable=self.file, width=90)
        IFileEntry.pack(pady = 6,ipady = 1, anchor = tk.NW, side = 'left')

    def set_extension(self, master):
        extension_frame = ttk.Frame(master)
        extension_frame.pack()
        option = ['*.mp3', '*.ogg', '*.ogg']
        combo = ttk.Combobox(extension_frame, values = option,state='readonly')
        combo.current(0)
        combo.pack()
