"""Phyllis Lynch Lab 4"""
my_dict = {
    "winter": "a cold season",
    "spring": "a wet season",
    "summer": "the only season worth talking about",
}
while True:
    response = input("What season are you looking for? ")
    if response in my_dict:
        print("that is in the dictionary")
    else:
        response = input("That is not found do you want to add it? yes or no ")
    if response == ("yes"):
        my_dict.update
        key = input("type the season name ")
        value = input("type the season description ")
        """my_dict.update({"key name": "key value"})"""
    elif response == ("no"):
        print("what do you want?")
    print(my_dict)
