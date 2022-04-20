"""Phyllis Lynch Boat class"""

class Boat():
    """Boat for sale information"""
    def __init__(self,size=10, price=100):
        print("This is a new boat for sale")
        self.__size = size
        self.__price = price
    def ppf(self):
        '''calculates price per foot'''
        return self.__price / self.__size
    def __repr__(self):
        '''
        check input
        '''
        return "("+ str(self.__price) + "," + str(self.__size) +")"
    def set_size(self, siz):
        '''
        changes the size
        '''
        if siz >= 100:
            print("That's a yacht!")
        if siz <= 5:
            print("That is a dingy!")
        self.__size = siz
    def get_size(self):
        '''
        gets the new info
        '''
        return self.__size
    def set_price(self, pri):
        '''
        sets the price
        '''
        if pri >= 1500000:
            print("That is too much!")
        if pri <= 0:
            print("That is not a valid price.")
        self.__price = pri
    def get_price(self):
        '''
        gets new price
        '''
        return self.__price
    def __str__(self):
        '''
        uses size and price to calculate price per ft
        '''
        return "What is the price per foot for this boat? " + str(self.ppf())
    def __eq__(self,other):
        if self is other:
            return True
        elif isinstance (self) != isinstance (other):
            return False
        else:
            return self.ppf() == other.ppf()
    def __lt__(self,other):
        if type (self) != type (other):
            return True
        else:
            return self.ppf() < other.ppf()
    def __ge__(self,other):
        if isinstance (self) != isinstance (other):
            return True
        else:
            return self.ppf() >= other.ppf()
class Brand(Boat):
    '''more boat info'''
    def __init__(self, mpg=2, horsepower=300):
        self.mpg = mpg
        self.horsepower = horsepower
        super().__init__()
    def __str__(self):
        return "How many horses? " + str(self.horsepower) + " and mpg is "+str(self.mpg)
    def __repr__(self):
        return "("+ str(self.mpg) + "," + str(self.horsepower) +")"
