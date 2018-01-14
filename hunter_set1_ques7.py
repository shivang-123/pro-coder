import re

pat1 = r'^[1-9][0-9]*$'
pat2 = r'^[0-9]+$'

n = input()

flag = True

def is_even(n):
    return True if n % 2 == 0 else False

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
        for i in range(n):
            val = int(arr[i])
            if (is_even(i) and not is_even(val)) or (not is_even(i) and is_even(val)):
                print(val, end = " ")
else:
    print("Invalid")
