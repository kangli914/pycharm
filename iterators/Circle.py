"""EX #47 - iterator example of workout
Define a class, Circle , that takes two arguments when defined: a sequence and
a number. The idea is that the object will then return elements the defined number
of times. If the number is greater than the number of elements, then the repeats as necessary

sepearting: 
    - iterator in class CircleIterator has __next__
    - ieartable class return interator __iter__

"""

class CircleIterator():

    def __init__(self, data, max, index=0):
        self.data = data
        self.max = max
        self.index = index

    def __next__(self):
        if self.index >= self.max:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value

class Circle():

    def __init__(self, sequence, max):
        self.sequence = sequence
        self.max = max

    def __iter__(self):
        # return self
        return CircleIterator(self.sequence, self.max)

if __name__ == "__main__":
    c = Circle("abc", 5)
    print(type(c))
    print(list(c))

    # c = Circle(["a", 'b', "c", "d"], 3)
    print(type(c))
    print(list(c))
