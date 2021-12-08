import re

n = input("Enter an input:")
x = "('^(?=\S{8,20}$)(?=.?\d)(?=.?[a-z])(?=.?[A-Z])(?=.?[^A-Za-z\s0-9])')"
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")
