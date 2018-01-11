import re

pat = r'^[a-zA-Z]+$'

s = input()

if bool(re.match(pat, s)):
    n = len(s)
    if n % 2 != 0:
        print("Invalid")
    else:
        for i in range(0, n, 2):
            print(s[i+1] + s[i], end = "")
else:
    print("Invalid")
