import re

pat = r'\d+'
n = input()

if bool(re.match(pat, n)):
    ans = 1
    n = int(n)
    for i in range(2, n+1):
        ans *= i
    print(ans)
else:
    print("Invalid")
