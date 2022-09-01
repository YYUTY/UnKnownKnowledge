__author__ ='Yatsuha'

import os
import sys
import data
import tkinter as tk

def main():
    root.title('UnKnownKnowledge')
    root.geometry('600x150')
    root.mainloop()

if __name__=='__main__':
    root=tk.Tk()
    data.Menu(root)
    if len(sys.argv) >= 0:
        data.Converts(root,'C:\\Users\\moya-hs1134\\github\\UnKnownKnowledge\\BossIntro.mp3')

    main()
