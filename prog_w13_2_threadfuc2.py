'''
Threading modules in Python:
1. thread: depreciated a while ago.
2. _thread: function-based programming.
3. threading: OOP based programming.
'''
import _thread 
import time 
# Define a function for the thread 
def func( threadName, delay, val): 
	count = 0 
	val1=0 
	while count < 15: 
		time.sleep(delay)
		val1 = val1 + val 
		#print ("val1: ", val1) 
		count += 1 
		print ("%s: %d" % (threadName, val1)) 

# Create two threads as follows 
try:
	_thread.start_new_thread( func, ("Thread-1",0.05, 9 ) ) 
	_thread.start_new_thread( func, ("Thread-2",0.05, 19) ) 
except: 
	print ("Error: unable to start thread") 
while 1: 
	pass