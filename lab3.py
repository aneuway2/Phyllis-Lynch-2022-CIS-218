""" Phyllis Lynch lab 3 - first attempt"""

VOWELS = 0
CHAR = 0
UP = 0
LO = 0
SPAC = 0
DIGI = 0
PUNC = 0
my_string = (input("What is your question? "))
for c in my_string:
    if c in "AEIOUaeiou":
        VOWELS += 1
    if c:
        CHAR += 1
    if c == " ":
        SPAC += 1
    if c .isupper():
        UP += 1
    if c .islower():
        LO += 1
    if c .isdigit():
        DIGI += 1
    if c in "?/!=+-_)(*#@$%'.,&":
        PUNC += 1
print("There are",VOWELS,"vowels,\n",CHAR,"characters,\n",LO,"lower case \
characters,\n",UP,"upper case \
characters,\n",SPAC,"spaces,\n",DIGI,"digits\nand",PUNC,"punctuation marks")

