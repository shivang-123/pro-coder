import re

pat1 = r'^[1-9][0-9]*$'
pat2 = r'^[0-9]+$'

n, m = input().split()

flag = True

#Check for validity of n & m
if bool(re.match(pat1, n)) and bool(re.match(pat1, m)):
    ar1 = input().split()
    ar2 = input().split()
    for i in ar1:
        #Checking validity for every element of array 1
        if not bool(re.match(pat2, i)):
            print("Invalid")
            flag = False
            break
    for i in ar2:
        #Checking validity for every element of array 2
        if not bool(re.match(pat2, i)):
            print("Invalid")
            flag = False
            break
    #If all inputs are valid
    if flag:
        ar1 = set(ar1)
        ar2 = set(ar2)
        if ar2 < ar1:
            print("YES")
        else:
            print("NO")
else:
    print("Invalid")
