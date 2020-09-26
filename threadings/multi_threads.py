import logging
import threading
import time

"""
[2020-09-20 10:57:22]: [INFO]: Main    : create and start Thread-1
[2020-09-20 10:57:22]: [INFO]: Thread-1: starting
[2020-09-20 10:57:22]: [INFO]: Main    : create and start Thread-2
[2020-09-20 10:57:22]: [INFO]: Thread-2: starting
[2020-09-20 10:57:22]: [INFO]: Main    : create and start Thread-3
[2020-09-20 10:57:22]: [INFO]: Thread-3: starting
[2020-09-20 10:57:22]: [INFO]: Main    : before joining Thread-1
[2020-09-20 10:57:32]: [INFO]: Thread-3: finishing
[2020-09-20 10:57:32]: [INFO]: Thread-2: finishing
[2020-09-20 10:57:32]: [INFO]: Thread-1: finishing
[2020-09-20 10:57:32]: [INFO]: Main    : Thread-1 done
[2020-09-20 10:57:32]: [INFO]: Main    : before joining Thread-2
[2020-09-20 10:57:32]: [INFO]: Main    : Thread-2 done
[2020-09-20 10:57:32]: [INFO]: Main    : before joining Thread-3
[2020-09-20 10:57:32]: [INFO]: Main    : Thread-3 done
Finished in 10.01 seoncds
"""


def thread_function(name):
    logging.info("Thread-%s: starting", name)
    time.sleep(10)
    logging.info("Thread-%s: finishing", name)

if __name__ == "__main__":

    format = "[%(asctime)s]: [%(levelname)s]: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d %H:%M:%S")

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

    start = time.perf_counter()

    for index in range(3):
        logging.info("Main    : create and start Thread-%d", index+1)
        t = threading.Thread(target=thread_function, args=(index+1,))
        t.start()
        threads.append(t)

    for thread in threads:
        logging.info("Main    : before joining %s", thread.getName())
        thread.join()
        logging.info("Main    : %s done", thread.getName())

    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seoncds")