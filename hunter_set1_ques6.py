import re

pat1 = r'^[1-9][0-9]*$'
pat2 = r'^[0-9]+$'

n = input()

flag = True

#Check for validity of n
if bool(re.match(pat1, n)):
    arr = input().split()
    for i in arr:
        #Checking validity for every element of array
        if not bool(re.match(pat2, i)):
            print("Invalid")
            flag = False
            break
    #If all inputs are valid
    if flag:
        n = int(n)
        d = dict()
        unique = True
        for i in arr:
            val = int(i)
            if val not in d:
                d[val] = val
            else:
                d[val] = d[val] ^ val
            if d[val] == 0:
                print(val)
                unique = False
                break
        if unique:
            print('unique')
else:
    print("Invalid")
