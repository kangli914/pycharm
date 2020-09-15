import time

def elapsed_since(data):
    last_time = None

    for item in data:
        current_time = time.perf_counter()
        if last_time is None:
            last_time = 0
            current_time = last_time
        value = (current_time - last_time, item)
        last_time = time.perf_counter()
        yield value


for t in elapsed_since('abcde'):
    print(t)
    time.sleep(2)