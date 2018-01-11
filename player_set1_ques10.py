import re

pat = r'^[a-zA-Z]+$'

s1, s2 = input().split(' ')

if bool(re.match(pat, s1)) and bool(re.match(pat, s1)):
    d = dict()
    count = 0
    flag = False
    for i in s1:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    for i in s2:
        if i not in d.keys() or d[i] == 0:
            if not flag:
                flag = True
            else:
                flag = False
                break
        else:
            d[i] -= 1
    if flag:
        print("yes")
    else:
        print("no")
else:
    print("Invalid")
