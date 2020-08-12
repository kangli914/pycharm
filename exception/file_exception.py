#!/usr/bin/env python3

import logging
import time

"""read binary file and measure time requried then return the data"""

# Create logger
logging.basicConfig(filename = "exception.log", level= logging.DEBUG)
logger = logging.getLogger()

def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""

    start_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except FileNotFoundError as e:
        logger.error(f"file not found: {e}")
        # detect/log error first and re-raise/pass along the error to the user again
        raise
        # or raise a customed error msg same as above
        # raise FileNotFoundError("customed file not found msg")
    else:
        # this else-block only execute when no error in try-block
        # note we can not close the file in the finally block since if file is not existed, there will be no file object (e.g. f) to close
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - start_time
        logger.info(f"Time requried for {path} was {dt}")


data = read_file_timed("null.log")
# data = read_file_timed("exception.log")
# print(data)