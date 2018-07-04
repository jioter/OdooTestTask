# return maximum number of occurrence of the same m-length substring in string
# Arguments:
# sss -  input string
# m -  substring length
# returns - max number of occurrence of the same m-length substring in s
# Example:
# check_num("ababa", 1) == 3
# check_num("aabbaaaaaacc", 2) == 6

# iterate over all m-length substring and add them to dict.
# find max number in dict.

import string
import random

s = list(string.ascii_lowercase)

random.seed(2)
s = [random.choice(string.ascii_lowercase) for i in range(1000000)]
s = ''.join(s)

r = {}
def check_num(s,m):
    for i in range(0,len(s)-1):
        mm = s[i:i+m]
        if mm not in r:	
            r[mm] = 1
        else:
            r[mm] += 1
    #print(r)
    print(max(r.values()))


check_num(s, 3)

