import re

pat = r'^[a-zA-Z ]+$'

s = input()

if bool(re.match(pat, s)):
    new = ""
    #new += s[0].upper()
    flag = True
    for i in s:
        if i == " ":
            flag = True
            new += i
        elif flag:
            new += i.upper()
            flag = False
        else:
            new += i
    print(new)
else:
    print("Invalid")
