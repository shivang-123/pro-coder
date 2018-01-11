import re

pat = r'^\d+$'

n = input()

if bool(re.match(pat, n)):
    ar = list(input().split())
    d = dict()
    flag = True
    for i in ar:
        if bool(re.match(pat, i)):
            val = int(i)
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        else:
            print("Invalid")
            flag = False
            break
    if flag:
        keys = sorted(d.keys())
        ans = []
        for i in keys:
            if d[i] > 1:
                ans.append(i)
        if len(ans) == 0:
            print('unique')
        else:
            print(*ans)
else:
    print("Invalid")
