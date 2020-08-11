from contextlib import contextmanager
import tempfile
import shutil
import os


@contextmanager
def tempdir(filename):
    try:
        dir_name = "tmp"
        print(f"Created temp directory: {dir_name}")

        filename = os.path.join(dir_name, filename)

        # Do some fake processing
        with open(filename, 'w') as f:
            print(f"Opened file: {filename}")
            # f.write("dummy text")
            yield f

    finally:
        print(f"Deleting directory: {dir_name}")
        shutil.rmtree(dir_name)

with tempdir("xyz.txt") as f:
    print("Doing something with the file ... ")
    f.write("dummy text")