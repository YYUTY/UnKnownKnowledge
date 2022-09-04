__author__  = 'Yatsuha'

import subprocess

music = ['.mp3','.ogg','.wav']
image = ['.png','.jpg','.gif']
movies = ['.mp4','.avi']
movie = ['.mp4','.avi','.ogg','.mp3','.wav']
path = None
fin = [False]
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
