import re

pat = r'[a-zA-Z]+'
n = input()

if bool(re.match(pat, n)):
    print(n + ".")
else:
    print("Invalid")
