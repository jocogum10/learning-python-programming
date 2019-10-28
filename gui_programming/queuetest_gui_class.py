# GUI that displays data produced and queued by worker threads (class-based)

import threading, queue, time
from tkinter.scrolledtext import ScrolledText

class ThreadGui(ScrolledText):
    threadPerClick = 4
    
    def __init__(self, parent=None):
        ScrolledText.__init__(self, parent)
        self.pack()
        self.dataQueue = queue.Queue()              # infinite size
        self.bind('<Button-1>', self.makethreads)   # on left mouse click
        self.consumer()                             # queue loop in main thread
        
    def producer(self, id):
        for i in range(5):
            time.sleep(0.1)
            self.dataQueue.put('[producer id=%d, count=%d]' % (id, i))
            
    def consumer(self):
        try:
            data = self.dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            self.insert('end', 'consumer got => %s\n' % str(data))
            self.see('end')
        self.after(100, self.consumer)              # 10 times per sec
        
    def makethreads(self, event):
        for i in range(self.threadPerClick):
            threading.Thread(target=self.producer, args=(i,)).start()
            
if __name__ == '__main__':
    root = ThreadGui()                              # in main thread: make GUI, run timer loop
    root.mainloop()                                 # pop-up window, enter tk event loop