import re

pat = r'\w+'

s = input()
if bool(re.match(pat, s)):
    print(s[::-1])
else:
    print("Invalid data")
