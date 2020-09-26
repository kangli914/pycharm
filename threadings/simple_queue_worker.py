import logging
import time
from queue import Queue
from threading import Thread

format = "[%(asctime)s]: [%(levelname)s]: %(message)s"
logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

def do_stuff(q, thread_no):
    while True:
        item = q.get()
        # print(q.get())
        logging.info(f"Worker Thread-{thread_no} getting item: {item}.")

        time.sleep(10)
        
        q.task_done()
        # logging.info(f"Worker Thread-{thread_no} got the item: {item}.")

q = Queue(maxsize=0)
num_threads = 10


start = time.perf_counter()
logging.info(f"All started.")

for i in range(num_threads):
    worker = Thread(target=do_stuff, args=(q,i+1))
    worker.setDaemon(True)
    worker.start()

for x in range(100):
    q.put(x)

q.join()

finish = time.perf_counter()
logging.info(f"All finished in {round(finish-start, 2)} seoncds")