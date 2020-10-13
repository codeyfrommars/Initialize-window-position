from ahk import AHK
from ahk.window import Window
import threading
#import time

#start = time.perf_counter() #timer to measure time to complete task
ahk = AHK()
#top of second monitor is (1920, -407)
apps = ['Discord', 'Spotify'] #list of apps to move


#function maximizes window to second monitor
def maxWin(title):
    win = ahk.win_get(title)
    while win.id == '': #until win is active
        win = ahk.win_get(title)
    win.move(x=1920, y=-407) 
    win.move(x=1920, y=-407) 
    win.maximize()


#implement multithreading
threads = []

for app in apps:
    t = threading.Thread(target = maxWin, args = [app])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

#finish = time.perf_counter()
#print(f'Finished in {round(finish-start, 2)} seconds(s)')