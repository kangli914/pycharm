import logging
import threading
import time

"""
# without join()
19:07:12: Main    : before creating thread
19:07:12: Main    : before running thread
19:07:12: Thread 1: starting
19:07:12: Main    : wait for the thread to finish
19:07:12: Main    : all done
19:07:14: Thread 1: finishing

# without join() and set it as daemon thread (daemon thread got killed when main thread exited)
19:11:54: Main    : before creating thread
19:11:54: Main    : before running thread
19:11:54: Thread 1: starting
19:11:54: Main    : wait for the thread to finish
19:11:54: Main    : all done

# with join, doesnt matter if thread 1 is daemon or not
19:16:22: Main    : before creating thread
19:16:22: Main    : before running thread
19:16:22: Thread 1: starting
19:16:22: Main    : wait for the thread to finish
19:16:24: Thread 1: finishing
19:16:24: Main    : all done
"""

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
