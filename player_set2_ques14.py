import re

pat = r'^[a-zA-Z]+$'

s = input()

if bool(re.match(pat, s)):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = ""
    for i in s[::-1]:
        if i not in vowels:
            ans += i
    print(ans)
else:
    print("Invalid")
