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
        ans = []
        for i in range(n):
            if i == int(ar[i]):
                ans.append(i)
        if len(ans) == 0:
            print(-1)
        else:
            print(*ans)
else:
    print("Invalid")
