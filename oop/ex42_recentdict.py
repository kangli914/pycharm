#!/usr/bin/env python3

class RecentDict(dict):

    def __init__(self, max):
        super().__init__()
        self.max = max

    def __setitem__(self, key, value):

        super().__setitem__(key, value)
        if len(self) > self.max:
            self.pop(list(self.keys())[0])

r = RecentDict(3)

r["a"] = 1
r["b"] = 2
r["c"] = 3
print(r)
r["d"] = 4
print(r)
