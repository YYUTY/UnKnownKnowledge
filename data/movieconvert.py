__author__ = 'Yatsuha'

import os
import re
import sys
import subprocess
import tkinter as tk
import threading as th
from . import variable as va
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk as ttk

class MovieConverts(tk.Frame):
    def __init__(self, master, filepath):
        self.fin = False
        self.path = self.path_get(filepath)
        self.old_path = self.path_get(filepath)
        self.set_dir(master)
        self.set_filename(master)
        self.set_extension(master)
        self.convert_button(master)
        self.changecombo(None)

    def changecombo(self, event):
        old_filename = self.file.get().split('.')[0]
        self.extension = self.combo.get().split('.')[1]
        self.filename = old_filename + '.' + self.extension
        self.file.set(self.filename)

    def convert(self):
        if os.path.isfile(os.path.join(self.dir.get(), self.filename)):
            messagebox.showerror('エラー', '同じファイルがすでに存在しています。')
            return
        if '.'+self.extension in va.music:
            self.convert_mus()

        if '.'+self.extension in va.movies:
            self.convert_mov()

    def convert_button(self, master):
        ConButton = ttk.Button(self.extension_frame, text = '変換', command = self.convert)
        ConButton.pack(side = 'right')

    def convert_mov(self):
        self.prog = tk.IntVar()
        self.win = tk.Toplevel()
        self.win.title('変換中')
        self.win.geometry('300x20')
        p = ttk.Progressbar(self.win,maximum = 100,mode = 'determinate',variable = self.prog,length = 200)
        p.pack()
        ffmpeg_path = os.path.join(va.path, 'ffmpeg\\ffmpeg.exe')
        old_file = self.old_path[0]
        self.frame_n = subprocess.run([os.path.join(va.path,'ffprobe.exe'),'-v','error','-select_streams','v:0','-show_entries','stream=nb_frames','-of','default=nokey=1:noprint_wrappers=1', str(old_file)], capture_output=True, text=True).stdout
        new_file = os.path.join(self.dir.get(), self.filename)
        self.cmd = ffmpeg_path+' '+'-i'+' '+old_file+' '+new_file
        prog_th = th.Thread(target=self.progress_bar)
        prog_th.start()

    def convert_mus(self):
        ffmpeg_path = os.path.join(va.path, 'ffmpeg.exe')
        old_file = self.old_path[0]
        new_file = os.path.join(self.dir.get(), self.filename)
        subprocess.call([str(ffmpeg_path), '-i', old_file, new_file])
        va.fin.append(True)

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

    def progress_bar(self):
        progress = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, startupinfo=va.startupinfo)
        for line in progress.stdout:
            line = line.encode('cp932').decode('utf-8')
            sentence = line.split(' ')
            if sentence[0] == 'frame=':
                if not sentence[2] == '':
                    self.prog.set(int((int(sentence[2])/int(self.frame_n))*100))
                    if int((int(sentence[2])/int(self.frame_n))*100) == 100:
                        self.win.destroy()
                        va.fin.append(True)

    def set_dir(self,master):
        dirframe = ttk.Frame(master)
        dirframe.pack()

        IDirLabel = ttk.Label(dirframe, text = 'フォルダ参照＞＞', padding = (5, 2))
        IDirLabel.pack(pady = 10, anchor = tk.NW, side = 'left')

        self.dir = tk.StringVar()
        self.dir.set(self.path[1])

        IDirEntry = ttk.Entry(dirframe,textvariable=self.dir, width = 70)
        IDirEntry.pack(pady = 11,ipady = 1, anchor = tk.NW, side = 'left')

        IDirButton = ttk.Button(dirframe, text = '参照', command = self.get_filedialog)
        IDirButton.pack(pady = 10, anchor = tk.NW, side = 'left')

    def set_filename(self,master):
        fileframe = ttk.Frame(master)
        fileframe.pack()

        IFileLabel = ttk.Label(fileframe, text = '　ファイル名＞＞', padding = (5, 4))
        IFileLabel.pack(pady = 5, anchor = tk.NW, side = 'left')

        self.file = tk.StringVar()
        self.file.set(self.path[2])

        IFileEntry = ttk.Entry(fileframe,textvariable = self.file, width=90)
        IFileEntry.pack(pady = 6,ipady = 1, anchor = tk.NW, side = 'left')

    def set_extension(self, master):
        self.extension_frame = ttk.Frame(master)
        self.extension_frame.pack(pady = 5, anchor = tk.NW, fill = tk.X)

        extlabel = ttk.Label(self.extension_frame, text = '拡張子', padding = (5, 4))
        extlabel.pack(ipady = 1,anchor = tk.NW, side = 'left')

        self.combo = ttk.Combobox(self.extension_frame, values = va.movie, state = 'readonly')
        self.combo.current(0)
        self.combo.bind('<<ComboboxSelected>>', self.changecombo)
        self.combo.pack(pady = 1, side = 'left')
