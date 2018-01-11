import re

pat = r'^\d+$'

n = input()

if bool(re.match(pat, n)):
    n = int(n)
    flag = True
    ar = list(input().split())
    for i in ar:
        if not bool(re.match(pat, i)):
            print("Invalid")
            flag = False
            break
    if flag:
        ans = 0
        for i in ar:
            ans ^= int(i)
        print(ans)
else:
    print("Invalid")
