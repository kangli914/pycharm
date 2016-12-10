'''
Threading modules in Python:
1. thread: depreciated a while ago.
2. _thread: function-based programming.
3. threading: OOP based programming.
'''
'''
threading module has a parent class (Thread). Some common methods provided by Thread are: 
	start(): it starts a thread by calling run() method. 
	run(): the starting point of a thread. 
	join(): waits for threads to terminate.
	append(): adds thread to a list of threads.
'''
import threading 
import time 

# 'threading.Thread' here is 'threading module has a parent class (Thread)'
class MyThread (threading.Thread): 
	def __init__(self, threadID, name, counter): 
		threading.Thread.__init__(self) 
		self.threadID = threadID 
		self.name = name
		self.counter = counter 

'''
	To create a thread using threading module, you need to define a new subclass of Thread class, overriding the _init_ method and then implementing the run() method.
'''		
	def run(self): 
		print ("Starting Python " + self.name) 
		print_time(self.name, self.counter, 5) 
		print ("Exiting " + self.name) 
		
def print_time(threadName, delay, counter): 
	while counter: 
		time.sleep(delay) 
		print ("%s: %s" % (threadName, time.ctime(time.time()))) 
		counter -= 1 

# create an empty 'List' (data structure) to contain thread		
threads = [] 
# Create new threads 
thread1 = MyThread(1, "Thread-1", 1) 
thread2 = MyThread(2, "Thread-2", 2) 

# Start new Threads  # it starts a thread by calling run() method. 
thread1.start()
thread2.start() 

threads.append(thread1) 
threads.append(thread2) 


'''
advantage of using OOP 'threading' over fucntion based '_thread'
comparing to using '_thread: function-based programming' which you need terminate the program by killing cmd window,
using OOP 'threading' threads will terminate itself without explicily killing the thread.
'''
thread1.join() 
thread2.join() 

print ("Exiting Main Thread")