class DatasetIterator():
    """ a simple iterator can be used in for-loop to iterator any iterable"""

    def __init__(self, data, index=0):
        self.index = index
        self.data = data
        print(f"in __init__ and initilize the index to be {self.index}")

    def __iter__(self):
        """retrun a iterator"""

        print(f"in __iter__")
        return self

    def __next__(self):
        """__next__ implementation should either return a value or raise StopIteration"""

        if self.index >= len(self.data):
            print(f"in __next__ and the end of dataset is reached and raised 'StopIteration'")
            raise StopIteration

        item = self.data[self.index]
        self.index += 1
        print(f"in __next__ and current returning item at {self.index} with item {item} to the caller")
        return item

# for i in "abc":
#     print(i)

for item in DatasetIterator("abcd"):
    print(f"this is current item from the dataset from iterator: {item}\n")

for item in DatasetIterator("abcd", index=1):
    print(f"this is current item from the dataset from iterator: {item}\n")
