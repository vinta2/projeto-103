import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileSystemEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"ola,{event,src_path}foi criado")

    def on_deleted(self,event):
        print(f"opa alguem exclui{event.src_path}!")

try:
    while True:
        time.sleep(2)
        print("excutando...")
    except KeyboardInterrupt:
        print("intenrronpido")
        observer.stop()