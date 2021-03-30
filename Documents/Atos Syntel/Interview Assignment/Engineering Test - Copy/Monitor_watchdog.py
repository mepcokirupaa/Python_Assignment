import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import glob
import ntpath

path = r'C:/Users/Lenovo/Documents/Atos Syntel/Interview Assignment/Engineering Test - Copy/Engineering Test Files' # use your path
all_files = glob.glob(path + "/*.csv")
li = []
class Watcher:
    DIRECTORY_TO_WATCH = "C:/Users/Lenovo/Documents/Atos Syntel/Interview Assignment/Engineering Test - Copy/Engineering Test Files"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print ("Error")

        self.observer.join()



class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
           print ("Received created event - %s." % event.src_path)
           filename_created = ntpath.basename(event.src_path)
           print(filename_created)
           
           for filename in all_files:
                  df = pd.read_csv(filename, index_col=None, header=0,error_bad_lines=False)
                  df['Environment'] =ntpath.basename(filename)
                  li.append(df)
          
           frame = pd.concat(li, axis=0, ignore_index=True)
           
           frame.to_csv('Engineering Test - Copy/Engineering Test Files/Combined_New.csv', mode='a', columns=['Source IP','Environment'],header=True,index=False)
           print(frame)
   
			
        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print ("Received modified event - %s." % event.src_path)
            
        elif event.event_type == 'deleted':
            # Taken any action here when a file is deleted.
            print ("Received deleted event - %s." % event.src_path)
        


if __name__ == '__main__':
    w = Watcher()
    w.run()

