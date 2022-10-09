# Birthday Cake Candles
# https://www.hackerrank.com/challenges/birthday-cake-candles

import math
import os
import random
import re
import sys


def birthdayCakeCandles(candles):
    max_h = []
    m = max(candles)
    for c in candles:
        if c == m:
            max_h.append(c)
    return len(max_h)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#-----------------------------------------------------------------------

# Time Conversion
# https://www.hackerrank.com/challenges/time-conversion


import math
import os
import random
import re
import sys


def timeConversion(s):
    if "PM" in s:
        s = s[:-2]
        if s[:2] == "12":
            r = s
        else:
            r = s.replace(s[:2], str(int(s[:2])+12))
    else:
        s = s[:-2]
        if s[:2] == "12":
            r = s.replace(s[:2], "00")
        else:
            r = s
    return r


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    
    fptr.write(result + '\n')

    fptr.close()

#------------------------------------------------------------------------

# Number Line Jumps (kangaroo)
# https://www.hackerrank.com/challenges/kangaroo

import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    # x1 + t*v1 = x2 + t*v2
    # t = (x2 - x1)/(v1 - v2)
    
    if (v1-v2) == 0:
        r = "NO"
    else:
        t = (x2 - x1)/(v1 - v2)
        if (x2-x1)%(v1-v2) == 0 and t >= 0:
            r = "YES"
        else:
            r = "NO"
    return r

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#-----------------------------------------------------------------------


# Strange Advertising
# https://www.hackerrank.com/challenges/strange-advertising


import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    liked = (math.floor(5/2))
    cumulative = liked
    for i in range(n-1):
        shared = liked*3
        liked = (math.floor(shared/2))
        cumulative += liked
    return cumulative
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#-------------------------------------------------------------------------

# Insertion sort 1
# https://www.hackerrank.com/challenges/insertionsort1


import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    t = int(arr[n-1])
    i = n-2
    while i >= 0:
        if t >= int(arr[i]):
            arr[i+1] = t
            print(" ".join(map(str, arr)))
            break
        else:
            arr[i+1] = arr[i]
            print(" ".join(map(str, arr)))
            if i == 0:
                arr[0] = t
                print(" ".join(map(str, arr)))
        i -= 1
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#------------------------------------------------------------------------

# Insertion sort 2
# https://www.hackerrank.com/challenges/insertionsort2


import math
import os
import random
import re
import sys

def insertionSort2(n, arr):

    for i in range(1, n):
        num = arr[i]
        t = i-1 # index
        while t >= 0 and num < arr[t]:
                arr[t+1] = arr[t] # bring num to the left
                t -= 1
        arr[t+1] = num
        print(" ".join(map(str, arr))) # print array for every number (i)
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)


#------------------------------------------------------------------------


# Recursive digit sum
# https://www.hackerrank.com/challenges/recursive-digit-sum


import math
import os
import random
import re
import sys


def superDigit(n, k):
    if len(n) == 1 and k == 1:
        return int(n)
    else:
        l = list(map(int, n))
        r = sum(l)
        return superDigit(str(r*k), 1)
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])
    
    
    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
