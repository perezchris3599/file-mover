from watchdog import*
from watchdog.observer import observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + filename
            os.rename(src, new_destination)

folder_to_track = "/Users/#/Desktop/myfolder"
folder_destination = "/Users/#/Desktop/newFolder"
event_handler = MyHandler()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterupt:
    observer.stop()
observer.join()