import os
import shutil


source = os.listdir('/Users/Honzor/Downloads/')
destination = '/Users/Honzor/Desktop/AUDIO/MIXES & PLAYLISTS/'
min_size = 20000000

for files in source:
    if files.endswith(".mp3"):
        if os.path.getsize(os.path.join('/Users/Honzor/Downloads/', files)) > min_size:
            shutil.move(os.path.join('/Users/Honzor/Downloads/', files), os.path.join(destination, files))
        else:
            print(files + ' - This is under 20mb and is not a music mix.')
