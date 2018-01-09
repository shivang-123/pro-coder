import re

pat = r'\d+'
n = input()

if bool(re.match(pat, n)):
    print(n[::-1])
else:
    print("Invalid")
