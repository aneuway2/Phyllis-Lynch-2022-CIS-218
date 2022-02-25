'''Phyllis Lynch lab 5'''
def ce_to_fa(celsius):
    '''calc celcius to fahreheit'''
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit
def test_ce_to_fa():
    """check the input"""
    assert ce_to_fa(0) == (32)
    assert ce_to_fa() == (0)
temp = float(input("what is the temperature in celcius? "))
print("temp in fahrenheit is", ce_to_fa(temp))
hi_low ={"32": "fahrenheit freezing", "212":"farenheit boiling"}
value = (hi_low.get(temp,"nope"))
print(value)
if ce_to_fa(temp) == 32:
    print("that is freezing")
elif ce_to_fa(temp) == 212:
    print("that is boiling")
else:
    print("that is not boiling or freezing")
