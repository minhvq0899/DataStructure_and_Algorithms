import sys
import queue

line = sys.stdin.readline()
line = line.split()
size = int(line[1])
n_command = int(line[0])

class fifo_queue:
    q = queue.Queue()
    def __init__(self, size):
        self.size = size
    
    def offer(s):
        if self.q.qsize() < self.size:
            self.q.put(s) # O(1)
            print("true")
        else:
            print("false")
    
    def take():
        if not self.q.empty():
            print(self.q.get()) #O(1)
            
    def size():
        print(self.q.qsize())
        


q = fifo_queue(size)
for i in range (n_command): #O(n)
    line = sys.stdin.readline()
    line = line.split() #O(n)
    print(line)
    if line[0] == 'OFFER': 
        q.offer( line[1] )
    elif line[0] == 'TAKE':
        q.take()
    else:
        q.size()

