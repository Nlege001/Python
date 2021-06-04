import ctypes  # provides low-level arrays

import logging, time

logging.basicConfig(format="%(asctime)s: %(message)s",
                    level=logging.INFO, datefmt="%H:%M:%S")

#################

class MyQueue0(object):
    """Circular buffer, no expansion. Queue operations are O(1)"""
    
    def __init__(self, capacity):
        """Create array with given items, or an empty array."""
        # The user thinks of _dataStartIndex as index 0.
        self._dataCount = 0
        self._blockCapacity = capacity
        self._dataStartIndex = 0
        self._block = (capacity * ctypes.py_object)()  # low-level array

    def put(self, obj):
        self._block[(self._dataStartIndex + self._dataCount)%self._blockCapacity] = obj
        self._dataCount += 1
 
    def get(self):
        """Return and delete the first item or raise EmptyError exception."""
        obj = self._block[self._dataStartIndex]
        self._block[self._dataStartIndex] = None
        self._dataStartIndex = (self._dataStartIndex+1) % self._blockCapacity
        self._dataCount -= 1
        return obj

#-------------------------
                
def circBuffer0Demo():
    
    print("Circular buffer demo (repeated get and put operations).")
    q = MyQueue0(3)
    q.put(1)
    q.put(2)
    q.put(3)
    for _ in range(100):
        x = q.get()
        q.put(x+3)

#-----------------------

#circBuffer0Demo()
# executes withut an error.

###########################

import threading
    
class MyJoinableQueue(MyQueue0):
    
    def __init__(self,capacity):
        self.putSem = threading.Semaphore(capacity)
        self.getSem = threading.Semaphore(0)
        super().__init__(capacity)
        
    def put(self, obj):
        self.putSem.acquire()
        super().put(obj)
        self.getSem.release()
    
    def get(self):
        self.getSem.acquire() # decrement
        result = super().get()
        self.getSem.release() # increment
        return result

#Question 1: How do I block the threads if there is no element in self._block(do i use join() or can I do
#it inside the run method)
    #def run(self):
     #   while True:
      #      task1 = super().get()
       #     if task1 is None:
        #        break
         #   elif 
        
    #pass
    # your code here.

#------------------

def circBufferDemo():
    print("Circular buffer demo (repeated get and put operations.")
    q = MyJoinableQueue(3)
    print(q)
    q.put(1)
    q.put(2)
    q.put(3)
    for _ in range(100):
        x = q.get()
        q.put(x+3)

#------------------

#circBufferDemo()
# Make sure it executes without an error.

###########################

def blockingDemo():
    print("Blocking bounds demo.")
    
    def get(aQueue):
        logging.info("Attempting get operation.")
        x = aQueue.get()
        logging.info(f"get opeartion completed: {x}.")

    def put(aQueue, value):
        logging.info("Attempting put operation.")
        aQueue.put(value)
        logging.info(f"put({value}) completed.")

    q = MyJoinableQueue(3)

    t1 = threading.Thread(target=get, args=(q,))
    t1.start() # wants to get an item but blocks
    time.sleep(1)
    # main thread:
    q.put(0)    # thread t2 can get now
    t1.join()

    q.put(1)
    q.put(2)
    q.put(3)    # the queue is full
    t2 = threading.Thread(target=put, args=(q,4))
    t2.start() # wants to get an item but blocks
    time.sleep(1)
    # main thread:
    q.get()    # thread t2 can put now
    t2.join()
    print()

#--------
 
#blockingDemo() # Make sure it runs and gives output like:
# Blocking bounds demo.
# 16:09:16: Attempting get operation.
# 16:09:17: get opeartion completed: 0.
# 16:09:17: Attempting put operation.
# 16:09:18: put(4) completed.

###########################

TASKS = 100
THREADS = 20

class Consumer(threading.Thread):

    def __init__(self, taskSupply, resultList):
        super().__init__(daemon=True)
        self.taskSupply = taskSupply
        self.resultList = resultList

    def run(self):
        while True:
            task = self.taskSupply.get()
            self.resultList.append(task)
            time.sleep(0.1)
            self.taskSupply.task_done() # !!!

#-----------

def joiningQueueDemo():

    print("Joining the queue demo.")
    
    tasks = MyJoinableQueue(TASKS)
    for number in range(TASKS):
        tasks.put(number)

    results = []
    for t in range(THREADS):
        c = Consumer(tasks, results)
        c.daemon = True
        c.start()

    tasks.join() # wait for tasks to finish.
    print(results)

#------------
    
joiningQueueDemo() # Make sure it runs and gives output like:
#Joining the queue demo.
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
# 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
# 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
# 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77,
# 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96,   
# 97, 98, 99]

#=========================
