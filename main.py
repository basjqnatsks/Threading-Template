class read(object):
    def __new__(cls, filename: str, delim: str = None) -> open:
        if delim != None:
            return cls.fileread(cls, filename).split(delim)
        return cls.fileread(cls, filename)
    def fileread(self, filename: str) -> [open]:
        with open(filename, "rb") as f:
            var = f.read().decode("ISO-8859-1").replace("\r", "").replace("\t", "")
        return var
    
import requests
import threading
from queue import Queue



class Threadit:
    ThreadedArray = []

	
    #function Requires 
    def __init__(self, FunctionPointer, WorkLoadArray, ThreadCount = 1) -> None:
        self.ThreadCount = ThreadCount
        print(ThreadCount)
        self.WorkLoadArray = WorkLoadArray
        def threader():
            while True:
                a = queue.get()
                if a == None:
                    break
                FunctionPointer(a[0], a[1])
                queue.task_done()
                
        queue = Queue()
        for x in range(self.ThreadCount):
            t = threading.Thread(target=threader)
            t.daemon = True
            self.ThreadedArray.append(t)
            t.start()
            
        for x in range(len(self.WorkLoadArray)):
            queue.put([self.WorkLoadArray[x], x])

        for i in range(self.ThreadCount):
            queue.put(None)
        for t in self.ThreadedArray:
            t.join()



def __ThreadedFunction(WorkLoad, ThreadId):
        
    while True:
        __R = requests.get("https://google.com")
        print(str(__R.status_code) + " Id: " + str(ThreadId))


Threadit(__ThreadedFunction, range(100), ThreadCount=100)