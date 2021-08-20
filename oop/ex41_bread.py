#/usr/bin/env phthon3

"""Simple bread class."""

class Bread():

    def __init__(self, calories=10, carbohydrates=10, sodium=10, sugar=10, fat=10):
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.sodium = sodium
        self.sugar = sugar
        self.fat = fat

    def get_nutrition(self, slices):
        # receive a dict whose key-value with new slices added
        # The vars() function returns the __dict__ attribute of the given object

        # return {k:v*slices for k,v in vars(self).items()}

        new_dict = {k:v*slices for k,v in vars(self).items()}
        print(f"----- {self.__class__.__name__} -----")
        for k,v in new_dict.items():
            print("{0:15} {1:3}".format(k, v))
        return new_dict


class WholeWheatBread(Bread):

    def __init__(self, calories=20, carbohydrates=20, sodium=20, sugar=20, fat=20):
        # refer tyo page 180
        # inplicitly involking Parents class __init__ via super()
        super().__init__(calories=calories, carbohydrates=carbohydrates, sodium=sodium, sugar=sugar, fat=fat)



if __name__ == "__main__":
    bread = Bread()
    # for k,v in bread.get_nutrition(3).items():
    #     print (k, v)
    bread.get_nutrition(3)

    whole_bread = WholeWheatBread()
    whole_bread.get_nutrition(1)

