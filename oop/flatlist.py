#!/usr/bin/env python3

class FlatList2(list):
    def append(self, new_value):
        try:
            for one_item in new_value:
                list.append(self, one_item)
        except TypeError:
            list.append(self, new_value)


class FlatList(list):

    def __init_(self):
        super().__init__()

    def append(self, *arg):
        for item in arg:
            super().append(item)


if __name__ == "__main__":
    l = FlatList();
    l.append(*[10,11,12])
    l.append(13)
    print(l)

    l2 = FlatList2();
    l2.append([20,21,22])
    l2.append(23)
    print(l2)
