"""Phyllis Lynch Lab 4"""
my_dict = {"winter":"a cold season", "spring":"a wet season",
           "summer":"the only season worth talking about"}
while True:
    response = (input( "What season are you looking for? "))
    if response in my_dict:
        print("that is in the dictionary")
        continue
    else: response = (input("That is not found do you want to add it? yes or no "))
    if response ==("no"):
        print("don't bother me")
    elif response == ("yes"):
        '''my_dict.update'''
    key = (input("type the season name "))
    value = (input("type the season description "))
    my_dict[key]=(value)
    print(my_dict)
