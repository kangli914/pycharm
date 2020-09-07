import os

def all_lines(path):
    # for root, dirs, files in os.walk(path):
    #     for file in files:
    #         print("file name:", os.path.join(root, file))
    #     for dir in dirs:
    #         print("dir name:", os.path.join(root, dir))
    for fname in os.listdir(path):
        ffile = os.path.join(path, fname)
        try:
            with open(ffile) as f:
                # for line in f.readlines():
                for line in f:
                    yield line
        except FileNotFoundError as e:
            print(f"file {fname} not found: {e}")

for line in all_lines("tmp"):
    print(line, end="")


