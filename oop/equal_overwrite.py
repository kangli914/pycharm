import random

class Dice:
    """Purpose: use keywoard arg as default and overwrite  __eq__ method.
    
    - keyword arg
    - rewrite magic method __eq__: this method is invoked whenever testing equality using operators == and != on objects 
    """

    def __init__(self, side=6):
        self.side = side

    # custom __eq__ by object type
    def __eq__(self, other):
        return type(self) == type(other)

    def roll(self):
        return random.randint(1, self.side)


d12 = Dice(side=12)
d6 = Dice()
print(d12.roll())
print(d6.roll())

# w/o overwrite __eq__
# output:
# 10
# 4
# object d6 is Not equal to d12
if (d6 == d12):
    print(f"object d6 is equal to d12") 
else:
    print(f"object d6 is Not equal to d12") 


# with overwrite __eq__
# def __eq__(self, other):
#     return type(self) == type(other)
# output:
# 4
# 6
# object d6 type is equal to d12 type
if (d6 == d12):
    print(f"object d6 type is equal to d12 type") 
else:
    print(f"object d6 type is Not equal to d12 type") 
