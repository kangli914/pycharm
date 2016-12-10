'''
Locking mechanism: the threading module allows programmers to synchronize threads. A new lock is created by calling the Lock() method that returns a lock. A thread can be forced to run synchronously by calling acquire() method and then release the lock to another thread by calling release() method.
'''
'''
2 jobs: 2nd jobs wait til 1st job finishes before 2nd job start
'''

import threading 
import time 

class MyThread (threading.Thread): 
	def __init__(self, threadID, name, counter): 
		threading.Thread.__init__(self) 
		self.threadID = threadID 
		self.name = name 
		self.counter = counter 
		
	def run(self): 
		print ("Starting " + self.name) 
		# Get lock to synchronize threads 
		threadLock.acquire() 
		print_time(self.name, self.counter, 3) 
		# Free lock to release next thread 
		threadLock.release() 
		
def print_time(threadName, delay, counter): 
	while counter: 
		time.sleep(delay) 
		print ("%s: %s" % (threadName, time.ctime())) 
		counter -= 1 
		
threadLock = threading.Lock() 
#threads = [] 
print(threading.activeCount()) 
print (threading.currentThread()) 
# Create new threads
thread1 = MyThread(1, "Thread-1", 1) 
thread2 = MyThread(2, "Thread-2", 2) 


# Start new Threads 
thread1.start() 
thread2.start() 
print (threading.currentThread()) 
print (threading.enumerate()) 
# Add threads to thread list 
#threads.append(thread1) 
#threads.append(thread2) 

# Wait for all threads to complete 
thread1.join() 
thread2.join() 

#for t in threads: 
	# t.join() 
	
#print ("Exiting Main Thread")