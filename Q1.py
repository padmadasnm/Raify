import re

n = input("Enter an input:")
x = "([[A-Z]{1}+[a-zA-Z]+\d{1}+\W{1}]{8}+$)"
match = re.fullmatch(x, n)
if match is not None:
    print("valid")
else:
    print("invalid")
