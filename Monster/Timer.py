import time

seconds = 30

class Timer(object):
        def __init__(self):
                global seconds
                time.sleep(1)
                seconds -= 1
        def printtime(self):
                while (seconds >= 0):
                        time.sleep(1)
                        seconds -= 1
                        global seconds
                        print (seconds)
 
mytime = Timer()

mytime.printtime()
