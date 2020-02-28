import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print(f'event type: {event.event_type}, path: {event.src_path}')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path='/Users/Honzor/Downloads/', recursive=False)
    observer.start()

    try:
        while True:

            source = os.listdir('/Users/Honzor/Downloads/')
            destination = '/Users/Honzor/Desktop/AUDIO/MIXES & PLAYLISTS/'
            min_size = 20000000

            for files in source:
                if files.endswith(".mp3"):
                    if os.path.getsize(os.path.join('/Users/Honzor/Downloads/', files)) > min_size:
                        shutil.move(os.path.join('/Users/Honzor/Downloads/', files), os.path.join(destination, files))
                    else:
                        print(files + ' - This is under 20mb and is not a music mix.')
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
