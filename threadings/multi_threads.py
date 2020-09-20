import logging
import threading
import time
"""
[10:24:46]: Main    : create and start Thread-1.
[10:24:46]: Thread-1: starting
[10:24:46]: Main    : create and start Thread-2.
[10:24:46]: Thread-2: starting
[10:24:46]: Main    : create and start Thread-3.
[10:24:46]: Thread-3: starting
[10:24:46]: Main    : before joining Thread-1
[10:24:56]: Thread-2: finishing
[10:24:56]: Thread-3: finishing
[10:24:56]: Thread-1: finishing
[10:24:56]: Main    : Thread-1 done
[10:24:56]: Main    : before joining Thread-2
[10:24:56]: Main    : Thread-2 done
[10:24:56]: Main    : before joining Thread-3
[10:24:56]: Main    : Thread-3 done
"""


def thread_function(name):
    logging.info("Thread-%s: starting", name)
    time.sleep(10)
    logging.info("Thread-%s: finishing", name)

if __name__ == "__main__":
    format = "[%(asctime)s]: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = []
    # for index in range(3):
    #     logging.info("Main    : create and start thread %d.", index)
    #     x = threading.Thread(target=thread_function, args=(index,))
    #     threads.append(x)
    #     x.start()

    # for index, thread in enumerate(threads):
    #     logging.info("Main    : before joining thread %d.", index)
    #     thread.join()
    #     logging.info("Main    : thread %d done", index)

    for index in range(3):
        logging.info("Main    : create and start Thread-%d", index+1)
        t = threading.Thread(target=thread_function, args=(index+1,))
        threads.append(t)
        t.start()

    for thread in threads:
        logging.info("Main    : before joining %s", thread.getName())
        thread.join()
        logging.info("Main    : %s done", thread.getName())