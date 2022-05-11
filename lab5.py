"""Phyllis Lynch lab 5"""


def celsius_to_fahrenheit(celsius=0):
    """calc celcius to fahreheit"""
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def test_celsius_to_fahrenheit():
    """check the input"""
    assert celsius_to_fahrenheit(0) == (32)
    assert celsius_to_fahrenheit() == (0)
    assert celsius_to_fahrenheit(1 <= temp <= 99), "not freezing or boiling"
    assert celsius_to_fahrenheit(101 <= temp <= 200), "steaming"


temp = float(input("what is the temperature in celsius? "))
print("temp in fahrenheit is", celsius_to_fahrenheit(temp))
hi_low = {"32": "fahrenheit freezing", "212": "farenheit boiling"}
value = hi_low.get("32") or hi_low.get("212")
print(value)
