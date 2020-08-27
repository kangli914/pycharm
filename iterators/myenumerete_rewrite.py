class MyEnumerete():

    def __init__(self, data, index=0):
        self.data = data
        self.index = index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        tuple_value = (self.index, self.data[self.index])
        self.index += 1
        return tuple_value

for item in MyEnumerete("abcde"):
    print(type(item))
    index, letter = item
    print(f"{index}: {letter}")
