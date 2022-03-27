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
