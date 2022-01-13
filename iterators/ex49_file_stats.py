#! /usr/bin/env python3

import os
from os import stat

"""A ex49 a generaor function that return files stats. 
Good example of open file with simple exception handle
"""


def file_usage_timing(dir):
    # get complete file paths into a list
    files = [os.path.join(dir, f) for f in os.listdir(dir)]
    for file in files:
        try:
            with open(file) as f:
                # you do need explicitely put () around to make it as tuple
                yield file, stat(file).st_atime, stat(file).st_mtime, stat(file).st_ctime
        
        except OSError:
            print(f"something wrong openning the file {file}")
            return None



if __name__ == "__main__":
    for one_file in file_usage_timing("iterators"):
        print(one_file)
'''
sample output:
/pycharm/.venv/bin/python /home/kangli/repo/personal/pycharm/tmp.py

('iterators/enumerate.py', 1641911236.8264124, 1610373951.5491354, 1610373951.5491354)
('iterators/enumerate_generator.py', 1641911236.8264124, 1610373951.5491354, 1610373951.5491354)
('iterators/MyChain.py', 1641911236.8264124, 1610373951.5491354, 1610373951.5491354)
('iterators/token_generator.py', 1641911236.8304124, 1610373951.5691352, 1610373951.5691352)
...
