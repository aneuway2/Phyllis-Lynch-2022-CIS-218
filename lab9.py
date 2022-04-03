"""Phyllis Lynch Boat class"""

class Boat(object):
    def __init__(self):
        print("This is a new boat for sale")
        self.__size = 10
        self.__price = 100

    def ppf(self):
        #calculates price per foot
        return self.__price / self.__size

    def set_size(self, si):
        if si >= 100:
            print("That's a yacht!")
        if si <= 5:
            print("That is a dingy!")
        self.__size = si

    def get_size(self):
        return self.__size

    def set_price(self, pi):
        if pi >= 1500000:
            print("That is too much!")
        if pi <= 0:
            print("That is not a valid price.")
        self.__price = pi

    def get_price(self):
        return self.__price
    def __str__(self):
        return "What is the price per foot for this boat? " + str(self.ppf())
class Brand(Boat):
    def __init__(self, size=15, price=1500, mpg=2, horsepower=300):
        self.size = size
        self.price = price
        self.mpg = mpg
        self.horsepower = horsepower
    
    def __str__(self):
        return "How many horses? " + str(self.horsepower) + " and mpg is "+str(self.mpg)
        
