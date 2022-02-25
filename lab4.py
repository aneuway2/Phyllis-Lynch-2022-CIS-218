"""Phyllis Lynch Lab 4"""
my_dict = {"winter":"a cold season", "spring":"a wet season",
           "summer":"the only season worth talking about"}
while True:
    response = (input( "What season are you looking for? "))
    if my_dict.get(response):
        print (my_dict.get(response), "is in the dictionary")
    else: response = (input("That is not found do you want to add it? yes or no "))
    if response ==("no"):
        print (my_dict.get(response), "don't bother me")
    if response == ("yes"):
        key = (input("type the season name "))
        value = (input("type the season description "))
        my_dict[key]=(value)
        print(my_dict)
