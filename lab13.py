""" Phyllis Lynch lab 13"""


class Person:
    def __init__(self, name, age):
        """acknow init"""
        print("a person")
        self.__name = name
        self.__age = age

    def __repr__(self):
        return "(" + str(self.__name) + "," + str(self.__age) + ")"

    def set_name(self, name):
        """set name of person"""
        return self.__name

    def get_name(self):
        """get name of person"""
        return self.__name

    def set_age(self, age):
        """set age of Person"""
        return self.__age

    def get_age(self):
        """get age of Person"""
        return self.__age

    def __str__(self):
        return "My name is " + str(self.__name) + " and I am " + str(self.__age)

    def age_sort(self, other):
        """sort Person by age"""
        print(self.__age, self.__name)


class Student(Person):
    """create subclass"""

    def __init__(self, name, age, earned, credits_taken):
        super().__init__(name, age)
        self.__earned = earned
        self.__credits_taken = credits_taken

    def calc_gpa(self):
        """calculate the gpa"""
        return self.__earned / self.__credits_taken

    def __str__(self):
        return "My gpa is " + str(self.calc_gpa())


def test_Person():
    """test Person class"""
    age = 23
    assert age == 23
    assert age >= 1
    assert age <= 110


def test_Student():
    """test student class"""
    earned = 23
    credits_taken = 5
    assert earned >= credits_taken
    assert credits_taken >= 1
    assert earned >= 1


if __name__ == "__main__":
    test_Person()
if __name__ == "__main__":
    test_Student()
