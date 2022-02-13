"""Phyllis Lynch Lab 4"""
my_dict = {"winter":"a cold season", "spring":"a wet season", "summer":"the only season worth talking about"}
while True:
    response = (input( "What season are you looking for? "))
    if response in my_dict:
        print("that is in the dictionary")
    else:
        question = (input("That is not found do you want to add it? yes or no "))
    if question == ("yes"):
        my_dict.update(input("add season and description "))
    elif question ==("no"):
        print("what do you want?")
    print(my_dict)