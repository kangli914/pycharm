#!/usr/bin/env python3

"""A single dictionary to write __getitem__ to access the dictionary element."""

class FlexDict(dict):

    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError as e:
            print(f"can't convert {key} to int: e")
            raise

        return super().__getitem__(key)
        # return dict.__getitem__(self, key)


fd = FlexDict()
fd['a'] = 100
print(fd['a'])

fd[5] = 500
print(fd[5])

fd[1] = 100
print(fd['1'])

fd['1'] = 100
print(fd[1])
