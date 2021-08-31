#!/usr/bin/env python3

"""A flex dictioanry converting key to string automatically."""

from ex42_flex_dict import FlexDict

'''
class FlexDict(dict):

    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            print(f"having issue converting {key} from string to int")
        return super().__getitem__(key)
'''

class StringKeyDict(FlexDict):

    def __setitem__(self, key, value):
        super().__setitem__(str(key), value)


sk = StringKeyDict()
sk[1] = 10

for item in sk.keys():
    print(type(item))
    print(item)
