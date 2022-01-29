"""Phyllis Lynch, website https://www.thekitchn.com/medium-large-jumbo-how-egg-sizes-actually-measure-up-ingredient-intelligence-200891
"""

while (True):

    egg = -1
    while (egg < 1.5):
        egg = float(input("Enter the egg weight in ounces"))

    if egg <= 1.5:
        size = "small"
    elif egg <= 1.75:
        size = "medium"
    elif egg <= 2.00:
        size = "large"
    elif egg <= 2.25:
        size = "xlarge"
    elif egg <=2.5:
        size = "jumbo"
    else:
        size = "not an egg"
        
    print ("Congratulations! your egg is ",size )
    

        
