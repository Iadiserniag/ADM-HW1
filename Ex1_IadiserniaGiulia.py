
# INTRODUCTION

# Hello World
# https://www.hackerrank.com/challenges/py-hello-world

print("Hello, World!")


#-------------------------------------------------------------------------

# If else
# https://www.hackerrank.com/challenges/py-if-else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2 == 0:
    if n in range(2, 6):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")  


#------------------------------------------------------------------------


# Arithmetic operators
# https://www.hackerrank.com/challenges/python-arithmetic-operators


if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)


#------------------------------------------------------------------------


# Division
# https://www.hackerrank.com/challenges/python-division


if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)


#-----------------------------------------------------------------------


# Loops
# https://www.hackerrank.com/challenges/python-loops


if __name__ == '__main__':
    n = int(input())
i = 0
while i < n:
    print(i**2)
    i += 1


#-----------------------------------------------------------------------


# Write a function
# https://www.hackerrank.com/challenges/write-a-function


def is_leap(year):
    leap = False
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leap = True
        else:
            leap = True
        
    return leap

year = int(input())
print(is_leap(year))


#-----------------------------------------------------------------------

# print function
# https://www.hackerrank.com/challenges/python-print


if __name__ == '__main__':
    n = int(input())
    i = 1
    out = ""
    while i < n + 1:
        out += str(i)
        i += 1
    print(out)

#------------------------------------------------------------------------

# BASIC DATA TYPES

# List comprehensions
# https://www.hackerrank.com/challenges/list-comprehensions


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = 0
    j = 0
    k = 0
    l = []
    
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                l.append([i, j, k])
    
    lnew = []
    for el in l:
        if sum(el) != n:
            lnew.append(el)
    
    print(lnew)


#---------------------------------------------------------------------


# Find the runner up score
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = [el for el in arr]
    lnew = []
    for x in l:
        if x not in lnew:
            lnew.append(x)
    lnew.sort(reverse=True)
    print(lnew[1])


#----------------------------------------------------------------------


# Nested lists
# https://www.hackerrank.com/challenges/nested-list


if __name__ == '__main__':
    records = []; scores = []; names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record = []
        record.append(name); record.append(score)
        names.append(name); scores.append(score)
        records.append(record)
    scores.sort()
    scores_new = []
    for el in scores:
        if el not in scores_new:
            scores_new.append(el)
    i = 0
    names_new = []
    while i < len(records):
        if records[i][1] == scores_new[1]:
            names_new.append(records[i][0])
        i += 1
    names_new.sort()
    [print(el) for el in names_new]


#---------------------------------------------------------------------


# Finding the percentage
# https://www.hackerrank.com/challenges/finding-the-percentage


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for n in student_marks:
        if n == query_name:
            for num in student_marks[n]:
                sum += num
    avg = sum/len(student_marks[query_name])
    form_avg = "{:.2f}".format(avg)
    print(form_avg)


#---------------------------------------------------------------------


# Lists
# https://www.hackerrank.com/challenges/python-lists


if __name__ == '__main__':
    N = int(input())
    arr = map(input().split())
    for el in arr:
        print(el)


#---------------------------------------------------------------------

# Tuples
# https://www.hackerrank.com/challenges/python-tuples


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = ()
    for el in integer_list:
        t += (el,)
    print(hash(t))

#---------------------------------------------------------------------

# STRINGS

# Alphabet Rangoli
# https://www.hackerrank.com/challenges/alphabet-rangoli



# part of the solution was inspired by the Discussion section of Hackerrank

def print_rangoli(size):
    
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
        sub = letters[:size]
    subR = letters[:size][::-1] # 'abcdefg'
    length = ((size*2)-1) + ((size-1)*2)
    j = (length - 1)//2
    
    for i in range(0, size):
        if i == 0:
            print(("-"*j).ljust(j) + ("-".join(sub[size-i:][::-1])).center(i) + ("-".join(sub[size-i-1:].center(i))) + ("-"*j).rjust(j))
        else:
            print(("-"*j).ljust(j) + ("-".join(sub[size-i:][::-1])).center(i) + "-" + ("-".join(sub[size-i-1:].center(i))) + ("-"*j).rjust(j))
        j -= 2


#-------------------------------------------------------------------------


# Swap Case
# https://www.hackerrank.com/challenges/swap-case


def swap_case(s):
    lst = []
    for ch in s:
        if ch.isupper() == True:
            lst.append(ch.lower())
        else:
            lst.append(ch.upper())
        s1 = ""
    for el in lst:
        s1 = s1 + el
    return s1


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#-------------------------------------------------------------------------

# String Split and join
# https://www.hackerrank.com/challenges/python-string-split-and-join


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#-------------------------------------------------------------------------

# What's your name?
# https://www.hackerrank.com/challenges/whats-your-name


def print_full_name(first, last):
    str1 = "Hello "
    str2 = "! You just delved into python"
    strn = str1 + first + " " + last + str2 + "."
    print(strn)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#-------------------------------------------------------------------------

# Mutations
# https://www.hackerrank.com/challenges/python-mutations


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character # list are mutable
    string = "".join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#-------------------------------------------------------------------------


# Find a string
# https://www.hackerrank.com/challenges/find-a-string


def count_substring(string, sub_string):
    words = []
    count = 0
    string = string.lower()
    i = 0
    j = 0
    for i in range(0, len(string)):
        for j in range(i + 1, len(string) + 1):
            words.append(string[i:j])
    
    print(words)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


#-------------------------------------------------------------------------

# String Validators
# https://www.hackerrank.com/challenges/string-validators


if __name__ == '__main__':
    s = input()
    Out = []
    l1 = []; l2 = []; l3 = []; l4 = []; l5 = []
    for char in s:
        if char.isalnum() == True:
            l1.append("True")
        if char.isalpha() == True:
            l2.append("True")
        if char.isdigit() == True:
            l3.append("True")
        if char.islower() == True:
            l4.append("True")
        if char.isupper() == True:
            l5.append("True")
            
    if "True" in l1:
        print(True)
    else:
        print(False)
    if "True" in l2:
        print(True)
    else:
        print(False)
    if "True" in l3:
        print(True)
    else:
        print(False)
    if "True" in l4:
        print(True)
    else:
        print(False)
    if "True" in l5:
        print(True)
    else:
        print(False)


#-------------------------------------------------------------------------


# Text Alignment
# https://www.hackerrank.com/challenges/text-alignment


#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).______(thickness-1)+c+(c*i).______(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).______(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).______(thickness*2)+(c*thickness).______(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).______(thickness)+c+(c*(thickness-i-1)).______(thickness)).______(thickness*6))


#-----------------------------------------------------------------------

# Text wrap
# https://www.hackerrank.com/challenges/text-wrap


import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#------------------------------------------------------------------------

# Designer Door Mat
# https://www.hackerrank.com/challenges/designer-door-mat


def doormat(L):
    L1 = L.split()
    N = int(L1[0])
    M = int(L1[1])
    
    # Top layer
    i = (M-3)//2
    j = 1
    while i >= 3:
        print(("-"*i).ljust(i) + (".|."*j).center(j) + ("-"*i).rjust(i))
        i -= 3
        j += 2
        
    # Middle welcome layer
    m = ((M-3)//2)-2
    print(("-"*m).ljust(m)+ "WELCOME" + ("-"*m).rjust(m))
    
    # Bottom layer
    t = 3
    k = (M-6)//3
    while t <= (M-3)//2:
        print(("-"*t).ljust(t) + (".|."*k).center(k) + ("-"*t).rjust(t))
        t += 3
        k -=2
    
L = input()
doormat(L)


#------------------------------------------------------------------------

# String Formatting
# https://www.hackerrank.com/challenges/python-string-formatting


def print_formatted(number):
    for i in range(1, n+1):
        print(i, end= " ")
        print(oct(i)[2:], end=" ").rjust(" ")
        print(hex(i)[2:], end=" ")
        print(bin(i)[2:])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#-----------------------------------------------------------------------

# Capitalize
# https://www.hackerrank.com/challenges/capitalize


def solve(s):
    fullname = s.split(" ")
    Out = []
    for i in fullname:
        Out.append(i.capitalize())
    return " ".join(Out)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#-----------------------------------------------------------------------

# Merge the tools
# https://www.hackerrank.com/challenges/merge-the-tools


def merge_the_tools(string, k):
    # k is a factor of n
    # split n into n/k substrings t
    # string u = subsequence of the characters in t, any repeat of a character is removed from the string (each character in u is unique)
    # print n/k lines where each line denotes a string u
    # n = len(s)
    
    n = len(string); substrings = []
    i = 0; j = k
    while i <= n-k:
        substrings.append(string[i:j])
        i += k
        j += k
    
    U = []
    for t in substrings:
        u = ""
        for char in t:
            if char not in u:
                u = u + char
        U.append(u)
    
    [print(s) for s in U]


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


#-------------------------------------------------------------------------


# The minion game
# https://www.hackerrank.com/challenges/the-minion-game


def minion_game(string):
    try:
        string = string.lower()
        vowels = ["a", "e", "i", "o", "u"]
        i = 0
        j = 0
        
        Words = []
        while i < len(string): 
            for j in range(i + 1, len(string) + 1):
                sub = string[i:j]
                Words.append(sub)           
                j += 1
            i += 1
        
        # Stuart
        Stuart_words = []
        count_Stuart = 0
        for w in Words:
            if w[0] not in vowels:
                Stuart_words.append(w)
                count_Stuart += 1
        
        # Kevin
        Kevin_words = []
        count_Kevin = 0
        for w in Words:
            if w[0] in vowels:
                Kevin_words.append(w)
                count_Kevin += 1
        
        if count_Stuart > count_Kevin:
            print("Stuart " + str(count_Stuart))
        elif count_Kevin > count_Stuart:
            print("Kevin " + str(count_Kevin))
        else:
            print("Draw")
    except Exception as e:
        print(e)        


#-----------------------------------------------------------------------

# SETS

# Sets

# Introduction to sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets


def average(array):
    s = set(array)
    return sum(s)/len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#-----------------------------------------------------------------------

# No Idea!
# https://www.hackerrank.com/challenges/no-idea


n, m = input().split() # in example n = 3; m = 2
arr = list(map(int, input().split()))
sets = []
for i in range(2):
    s = set(map(int, input().split()))
    sets.append(s)
    
A, B = sets

happiness = 0
for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
    else:
        pass

print(happiness)


#-----------------------------------------------------------------------

# Symmetric difference
# https://www.hackerrank.com/challenges/symmetric-difference


def sets(n1, i1, n2, i2):
    l1 = i1.split()
    l2 = i2.split()
    s1 = set(list(map(int, l1)))
    s2 = set(list(map(int, l2)))
    
    out1 = list(s1.difference(s2))
    out2 = list(s2.difference(s1))
    
    out = out1 + out2
    out.sort()
    [print(num) for num in out]

n1 = input()
i1 = input()
n2 = input()
i2 = input()
sets(n1, i1, n2, i2)


#-----------------------------------------------------------------------

# set.add()
# https://www.hackerrank.com/challenges/py-set-add

import sys

def distinct_stamps(n, countries):
    c = [country.rstrip() for country in countries]
    distinct_countries = set(c)
    
    print(len(distinct_countries))

n = input()
countries = sys.stdin.readlines()
distinct_stamps(n, countries)
    

#----------------------------------------------------------------------


# set.discard/remove/pop
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop


n = int(input())
s = set(map(int, input().split()))
c = int(input())
commands = []
for _ in range(c):
    command, *i = input().split()
    num = list(map(int, i))
    commands.append([command, num])


try:
    for command in commands:
        if command[0] == "pop":
            s.pop()
        elif command[0] == "remove":
            s.remove(command[1][0])
        elif command[0] == "discard":
            s.discard(command[1][0])
    
except KeyError:
    pass

print(sum(s))


#------------------------------------------------------------------------

# set Union
# https://www.hackerrank.com/challenges/py-set-union


n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

S = s1.union(s2)
print(len(S))


#------------------------------------------------------------------------

# set intersection
# https://www.hackerrank.com/challenges/py-set-intersection-operation


n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

S = s1.intersection(s2)
print(len(S))


#------------------------------------------------------------------------

# set difference
# https://www.hackerrank.com/challenges/py-set-difference-operation


n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

S = s1.difference(s2)
print(len(S))


#-----------------------------------------------------------------------

# Symmetic difference
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation


n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))

U = s1.union(s2)
I = s1.intersection(s2)
print(len(U.difference(I)))

# or use symmetric_difference() function of sets

#------------------------------------------------------------------------

# Set mutations
# https://www.hackerrank.com/challenges/py-set-mutations


na = int(input())
a = set(map(int, input().split()))
N = int(input())
l = []
for _ in range(0, 2*N):
    s = input().split()
    l.append(s)


i = 0
while i < len(l):
    if i%2 != 0:
        l[i] = set(l[i])
        l[i] = {int(el) for el in l[i]}
    i += 1
    

for index in range(len(l)):
    if index%2 == 0:
        if l[index][0] == "intersection_update":
            a.intersection_update(l[index+1])
        elif l[index][0] == "update":
            a.update(l[index+1])
        elif l[index][0] == "symmetric_difference_update":
            a.symmetric_difference_update(l[index+1])
        elif l[index][0] == "difference_update":
            a.difference_update(l[index+1])
print(sum(a))


#------------------------------------------------------------------------

# The captain's room
# https://www.hackerrank.com/challenges/py-the-captains-room


import operator as op

# tourists:
# * captain (one room)
# * unknown group of k-member families (at least 2 members x family, one room)
# aim: find the captain's room

k = int(input())
room_list = list(map(int, input().split()))

# my take
room_list.sort()

n = len(room_list)
number_of_families = (n-1)//k


for el in room_list:
    count = op.countOf(room_list, el)
    if count < 2:
        print(el)
        
#----------------------------------------------------------------------


# Check subset
# https://www.hackerrank.com/challenges/py-check-subset


# inputs
t = int(input())
for _ in range(t):
    na, a = int(input()), set(map(int,input().split())) # 1st set
    nb, b = int(input()), set(map(int, input().split())) # 2nd set
    if a.intersection(b) == a:
        print(True)
    else:
        print(False)

#-----------------------------------------------------------------------

# Check strict subset
# https://www.hackerrank.com/challenges/py-check-strict-superset

A = set(map(int, input().split()))
n = int(input())
sets = []
for _ in range(n):
    s = set(map(int, input().split()))
    sets.append(s)

results = []  
for s in sets:
    if A.issuperset(s) == False:
        results.append(False)

if len(results) > 0:
    print(False)
else:
    print(True)


#-----------------------------------------------------------------------

# COLLECTIONS

# Collections


# Counter
# https://www.hackerrank.com/challenges/collections-counter


from collections import Counter

X = int(input()) # number of shoes
shoe_sizes = list(map(int, input().split()))
N = int(input()) # number of customers
customer_list = []
for _ in range(N):
    customer_list.append(list(map(int, input().split()))) # shoe size and price
    
count_sizes = Counter(shoe_sizes)
money = 0

for customer in customer_list:
    if customer[0] in count_sizes.keys():
        if count_sizes[customer[0]] > 0:
            money += customer[1]
            count_sizes[customer[0]] -= 1

print(money)

#-------------------------------------------------------------------


# Named tuple
# https://www.hackerrank.com/challenges/py-collections-namedtuple


from collections import namedtuple

N = int(input()) # total number of students
columns = list(input().split())

s = 0
for _ in range(N):
    mark = int(input().split()[columns.index("MARKS")])
    s += mark

average = s/N
print("{:.2f}".format(average))


#------------------------------------------------------------------


# Ordered dict
# https://www.hackerrank.com/challenges/py-collections-ordereddict

N = int(input())
Purchases = {}
for _ in range(N):
    *item_name, net_price = input().split()
    item_name, net_price = " ".join(item_name), int(net_price)
    if item_name in Purchases:
        Purchases[item_name] += net_price
    else:
        Purchases[item_name] = net_price
    
for key in Purchases:
    print(key + " " + str(Purchases[key]))


#------------------------------------------------------------------

# Word order
# https://www.hackerrank.com/challenges/word-order


# words may repeat
# output the number of occurrences of the word
n = int(input())
words = {}
for _ in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))
print(*words.values())


#--------------------------------------------------------------------


# Collections deque
# https://www.hackerrank.com/challenges/py-collections-deque

from collections import deque

N = int(input())
commands = []
for _ in range(N):
    command = input().split()
    commands.append(command)

d = deque()
for c in commands:
    if c[0] == "append":
        d.append(c[1])
    elif c[0] == "pop":
        d.pop()
    elif c[0] == "appendleft":
        d.appendleft(c[1])
    elif c[0] == "popleft":
        d.popleft()

print(*d)


#---------------------------------------------------------------------


# Company logo
# https://www.hackerrank.com/challenges/most-commons


import math
import os
import random
import re
import sys


from collections import Counter # use counter to count the occurrences of each character in the string

if __name__ == '__main__':
    s = input()
    
counter = Counter(sorted(s))
mc_counter = counter.most_common(3) # get the 3 most common key, value pairs, already sorted in descending order

for a, b in mc_counter:
    print(a, b)


#----------------------------------------------------------------------


# Piling up
# https://www.hackerrank.com/challenges/piling-up
# I took inspiration from the Discussion section for this exercise


from collections import deque

T = int(input()) # number of test cases
for _ in range(T):
    n = int(input())
    blocks = deque(map(int, input().split())) # with deque we can pop left as well as right
    
    out = "Yes"
    i = 0
    block = 2**31 # maximum side length
    
    for _ in range(n):
        # let's choose the block with the largest side (left of right)
        if blocks[0] > blocks[-1]:
            next_block = blocks.popleft()
        else:
            next_block = blocks.pop()
        if i > 0:
            if next_block > block: # our next block is larger than the previous one --> impossible
                out = "No"
                break # we can stop here, no need to continue iterating
        block = next_block   
        i += 1
    
    print(out)


#----------------------------------------------------------------------


# Default dict
# https://www.hackerrank.com/challenges/defaultdict-tutorial


from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)
b = defaultdict(list)
for i in range(n):
    a[input().strip()].append(i+1)
for j in range(m):
    b[input().strip()].append(j+1)


for el in b:
    if bool(a[el]):
        print(*a[el])
    else:
        print(-1)

#----------------------------------------------------------------------

# DATE&TIME

# Time and Date

# Calendar Module
# https://www.hackerrank.com/challenges/calendar-module

import calendar

date = list(map(int, input().split()))

# Monday = 0,..., Wednesday = 2,..., Sunday = 6
days = {0: "MONDAY", 1: "TUESDAY", 2: "WEDNESDAY", 3: "THURSDAY", 4: "FRIDAY", 5: "SATURDAY", 6: "SUNDAY"}

day = calendar.weekday(date[2], date[0], date[1]) # year,month,day
print(days[day])

#----------------------------------------------------------------------------


# Time delta
# https://www.hackerrank.com/challenges/python-time-delta


from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    form = '%a %d %b %Y %H:%M:%S %z'

    t1 = datetime.strptime(t1, form) # from string to dt format
    t2 = datetime.strptime(t2, form) 
    
    return abs(int((t1-t2).total_seconds())) # timedelta

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        print(delta)


#------------------------------------------------------------------------

# EXCEPTIONS
# https://www.hackerrank.com/challenges/exceptions


T = int(input()) # number of test cases
for _ in range(T):
    a, b = input().split()
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as err1:
        print("Error Code:", err1)
    except ValueError as err2:
        print("Error Code:", err2)


#-----------------------------------------------------------------------


# BUILT-INS

# # BUILT-INS

# 1) Zipped!
# https://www.hackerrank.com/challenges/zipped


N, X = map(int, input().split()) #N = no. of students, X = no. of subjects

subjects = []
for _ in range(X):
    s = list(map(float, input().split()))
    subjects.append(s)

for i in zip(*subjects):
    print(sum(i)/X)

# ----------------------------------------------------------------


# 2) Athlete Sort
# https://www.hackerrank.com/challenges/python-sort-sort


from operator import itemgetter


if __name__ == '__main__':
    n, m = map(int, input().split())
    # n = number of lines
    # m = number of attributes

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input()) # 0 <= k <= M - 1

sort_arr = sorted(arr, key = itemgetter(k)) # sort (order lists) by the kth attribute

for i in sort_arr:
    print(*i)

# ---------------------------------------------------------------------

# 3) ginosort
# https://www.hackerrank.com/challenges/ginorts


s = input()

# given that s.isalnum() == True

odd = ""; even = ""; upper = ""; lower = ""

for ch in s:
    if ch.isdigit() == True:
        if int(ch) % 2 != 0:
            odd += ch
        else:
            even += ch
    elif ch.islower() == True:
        lower += ch
    else:
        upper += ch

# sort all 

out = "".join(sorted(lower)) + "".join(sorted(upper)) 
+ "".join(sorted(odd))+ "".join(sorted(even))

print(out) # print output

#-------------------------------------------------------------------------

# PYTHON FUNCTIONALS


# Map and Lambda Function
# https://www.hackerrank.com/challenges/map-and-lambda-expression


cube = lambda x: x**3

def fibonacci(n):
    i = 0; f0 = 0; f1 = 1
    if n < 3:
        if n == 0:
            fibonacci_list = []
        elif n == 1:
            fibonacci_list = [f0]
        else:
            fibonacci_list = [f0, f1]
    else:
        fibonacci_list = [f0, f1]
        while i < n-2:
            fnext = f0 + f1
            fibonacci_list.append(fnext)
            f0 = f1
            f1 = fnext
            i += 1
    return fibonacci_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


#-----------------------------------------------------------------------

# REGEX & PARSING


# Detect Floating Point Number
# https://www.hackerrank.com/challenges/introduction-to-regex


T = int(input())

for _ in range(T):
    try:
        result = bool(float(input()))
        print(result)
        # Try to turn string into float
        # If it's possible:
        # if float, print True
        # if not float print False
    except:
        print(False) # if not possible to turn string into float, just print False

#----------------------------------------------------------------------------------

# Res.split()
# https://www.hackerrank.com/challenges/re-split


regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))


#-----------------------------------------------------------------------------------

# Group(), Groups() & Groupdict()
# https://www.hackerrank.com/challenges/re-group-groups


import re

S = str(input())

l = re.findall(r"([A-Za-z0-9])\1+", S)
# more than one occurance (1+) of a:
# letter (either upper or lower case)
# number (digit from 0-9)

if len(l) == 0: # if there are no reaccuring characters
    print(-1)
else:
    print(l[0]) 

#------------------------------------------------------------------------


# Re.start() & re.end()
# https://www.hackerrank.com/challenges/re-start-re-end

import re

s = str(input())
k = str(input())


indices = []
for i in range(len(s)):
    m = re.search(k, s[i:len(k)+i])
    if m is not None:
        indices.append((i, len(k)+i-1))


if len(indices) > 0:
    for el in indices:
        print(el)
else:
    print((-1, -1))


#-------------------------------------------------------------------------


# Validating phone number
# https://www.hackerrank.com/challenges/validating-the-phone-number


import re

n = int(input())

for _ in range(n):
    number = str(input())
    if len(number) == 10 and number.isdigit() == True:
        if re.search(r'[7-9]', number[0]):
            print("YES")
        else:
            print("NO")
    else:
            print("NO")


#-------------------------------------------------------------------------

# Validating Named Email Addresses
# https://www.hackerrank.com/challenges/validating-named-email-addresses


import email.utils
import re

n = int(input())

emails = []
for _ in range(n):
    emails.append(email.utils.parseaddr(str(input())))

p = "^[a-zA-Z][a-zA-Z0-9-_.]*[@][a-zA-Z]+[.][a-zA-Z]{1,3}$"
# ^[a-zA-Z] starts with (^) an alphabetical character
# [a-zA-Z0-9-_.] username can contain alphanumeric characters -,.,_ 
# [@][a-zA-Z] domain alphametical characters
# [.][a-zA-Z]{1,3}$ mail needs to end with ($) an extention after the dot
# the extention must be three alphabetical characters or less (2 or 1)

for mail in emails:
    if re.search(p, mail[1]):
        print(email.utils.formataddr((mail[0], mail[1])))


#------------------------------------------------------------------------
    
# Html Parser Part 1
# https://www.hackerrank.com/challenges/html-parser-part-1


from html.parser import HTMLParser

n = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs != "":
            for i in range(len(attrs)):
                print("->", attrs[i][0], ">", attrs[i][1])
    def handle_endtag(self, tag):
        print("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs != "":
            for i in range(len(attrs)):
                print("->", attrs[i][0], ">", attrs[i][1])
        
parser = MyHTMLParser()

for _ in range(n):
    p = str(input())
    parser.feed(p)


#-------------------------------------------------------------------------


# Html Parser Part 2
# https://www.hackerrank.com/challenges/html-parser-part-2


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != "\n":
            if "\n" in data:
                print(">>> Multi-line Comment"  + "\n" + data)
            else:
                print(">>> Single-line Comment"  + "\n" + data)
    def handle_data(self, data):
        if data != "\n":
            print(">>> Data"  + "\n" + data)

        
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


#------------------------------------------------------------------------

# Re.sub (substitution)
# https://www.hackerrank.com/challenges/re-sub-regex-substitution


import re


n = int(input())
for _ in range(n):
    line = str(input())
    if not re.search("#", line):
        line = re.sub(r"(?<=\s)&&(?=\s)", "and", line)
        line = re.sub(r"(?<=\s)\|\|(?=\s)", "or", line)
    print(line)


# ?<=x(y) --> y preceded by x (space)
# (y)?=x --> y followed by x (space)


#-------------------------------------------------------------------------


# Detect Html tags, attributes and attribute values
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values


from html.parser import HTMLParser

n = int(input())

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs != "":
            for i in range(len(attrs)):
                print("->", attrs[i][0], ">", attrs[i][1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs != "":
            for i in range(len(attrs)):
                print("->", attrs[i][0], ">", attrs[i][1])

parser = MyHTMLParser()
                
for _ in range(n):
    p = str(input())
    parser.feed(p)


#-------------------------------------------------------------------------

# Validating IUD
# https://www.hackerrank.com/challenges/validating-uid


import re

n = int(input())
for _ in range(n):
    line = str(input())
    if len(line) == 10 and len(re.findall("[A-Z]", line)) > 1 and len(re.findall("\d", line)) > 2 and len(set(re.findall("\w", line))) == 10:
        print("Valid")
    else:
        print("Invalid")
        
# 1st requirement: length equal to 10
# 2nd requirement: at least 2 upper case letters
# 3rd requirement: at least 3 numbers (digits)
# 4th requirement: 10 UNIQUE alphanumeric character (we want the set to be of length 10 and not less, since set considers only unique elements)


#----------------------------------------------------------------------------


# Re.findall() & Re.finder()
# https://www.hackerrank.com/challenges/re-findall-re-finditer


import re

s = str(input())
check = re.findall(r'(?<=[b-df-hj-np-tv-xzB-DF-HJ-NP-TV-XZ])[AEIOUaeiou]{2,}(?=[b-df-hj-np-tv-xzB-DF-HJ-NP-TV-XZ])',s)
if len(check) > 0:
    [print(el) for el in check]
else:
    print(-1)


#---------------------------------------------------------------------------

# I looked at the Hackerrank Discussion section for this excercise and I tried to understand the solution
# Validating Roman Numerals
# https://www.hackerrank.com/challenges/validate-a-roman-number


regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

# ^: starts with
# Thousands [1000-3000]
# Hundreds (CM = [600-900], CD = [400], D = [500], C = [100-300])
# Tens (XC = [60-90], XL = [40], L = [50], X = [10-30])
# Units (IX = [6-9], IV = [4], V = [5], I = [1-3])
# $ ends with

import re
print(str(bool(re.match(regex_pattern, input()))))



#------------------------------------------------------------------------


regex_integer_in_range = r"[1-9][0-9][0-9][0-9][0-9][0-9]$"

regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)|(?<=\d\1)(\d)"    # Do not delete 'r'.
# lookahead and lookbehind (since we need both occurrences of the repeating digit)


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


#------------------------------------------------------------------------

# Validating Credit Card Numbers
# https://www.hackerrank.com/challenges/validating-credit-card-number

import re

pattern = r"(^[456]{1}\d{15}$)|(^[456]\d{3}[-]\d{4}[-]\d{4}[-]\d{4}$)"

pattern2 = r"([\d])\1\1\1"

n = int(input())

for _ in range(n):
    number = str(input())
    if re.search(pattern, number):
        n = number.replace("-", "")
        if len(re.findall(pattern2, n)) > 0:
            print("Invalid")
        else:
            print("Valid")
    else:
        print("Invalid")


#------------------------------------------------------------------------

# Matrix Script

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    
# special_characters = ['!','@','#','$','%','&']

pattern = r'(?<=\w)[!@#$%&\s]+(?=\w)'
  
output = ""
for index in range(len(matrix[0])):
    for i in range(len(matrix)):
        p = matrix[i][index]
        output += p
        

#print(re.findall(pattern, output))
o = re.sub(pattern, " ", output)
print(o)



# for c in matrix get 1st element of every c until you got through all the list then go to the next position until you get to the end
# special character in between two letters (alphanumeric characters) substitute it with a space


#--------------------------------------------------


# Hex Color Code
# https://www.hackerrank.com/challenges/hex-color-code


import re

n = int(input())

pattern = r"^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})"

for _ in range(n):
    line = input()
    if line[0] not in ["#", "{", "}", "."]:
        line = re.split("\s|[;:,()]", line)
        for el in line:
            if re.search(pattern, el):
                print(el)

#-----------------------------------------------------------------------

# XML


# XML 1
# https://www.hackerrank.com/challenges/xml-1-find-the-score


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    out = 0
    for el in node.iter():
        out += len(el.keys())
    return out

    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


#--------------------------------------------------------------


# XML2
# I took inspiration from the Discussion section in Hackerrank
# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth


import xml.etree.ElementTree as etree

# ElementTree represents the whole XML document as a tree, and Element represents a single node in this tree.

maxdepth = 0
def depth(elem, level):
    global maxdepth

    if level == maxdepth:
        maxdepth += 1

    for child in elem: # child --> go to the next level
        depth(child, level + 1) # recall function until you reach the end

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

#------------------------------------------------------------------------

# XML 1
# https://www.hackerrank.com/challenges/xml-1-find-the-score


import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    out = 0
    for el in node.iter():
        out += len(el.keys())
    return out

    
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
    
    
#------------------------------------------------------------------------

# NUMPY

# Arrays
# https://www.hackerrank.com/challenges/np-arrays


import numpy

def arrays(arr):
    n = numpy.array(arr, float)
    return numpy.flip(n)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#------------------------------------------------------------


# Shape and Reshape
# https://www.hackerrank.com/challenges/np-shape-reshape

import numpy

a = list(map(int, input().split()))

arr = numpy.array(a)
arr.shape = (3,3)
print(arr)


#------------------------------------------------------------


# Transpose and Flatten
# https://www.hackerrank.com/challenges/np-transpose-and-flatten


import numpy

n, m = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
arr = numpy.array(l)

tarr = numpy.transpose(arr)
print(tarr)

farr = arr.flatten()
print(farr)


#---------------------------------------------------------------


# Concatenate
# https://www.hackerrank.com/challenges/np-concatenate


n, m, p = map(int, input().split())
l1 = []
l2 = []
for _ in range(n):
    l1.append(list(map(int, input().split())))
for _ in range(m):
    l2.append(list(map(int, input().split())))
    
arr1 = numpy.array(l1)
arr2 = numpy.array(l2)
print(numpy.concatenate((arr1, arr2), axis = 0))


#----------------------------------------------------------------


# zeroes and ones
# https://www.hackerrank.com/challenges/np-zeros-and-ones


import numpy

l = list(map(int, input().split()))

arr1 = numpy.zeros(l, int)
arr2 = numpy.ones(l, int)
print(arr1, arr2, sep ="\n")


#-----------------------------------------------------------------


# Eye and Identity
# https://www.hackerrank.com/challenges/np-eye-and-identity


import numpy
numpy.set_printoptions(legacy="1.13")

n, m = map(int, input().split())

print(numpy.eye(n, m, k=0))


#------------------------------------------------------------------


# Array Mathematics
# https://www.hackerrank.com/challenges/np-array-mathematics


import numpy

n, m = map(int, input().split())

l1 = []
l2 = []
for _ in range(n):
    l1.append(list(map(int, input().split())))
for _ in range(n):
    l2.append(list(map(int, input().split())))

A = numpy.array(l1)
B = numpy.array(l2)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A** B)


#--------------------------------------------------------------------


# Floor, Ceil and Rint
# https://www.hackerrank.com/challenges/floor-ceil-and-rint


import numpy

numpy.set_printoptions(legacy="1.13")

arr = numpy.array(input().split(), float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))



#--------------------------------------------------------------------


# Sum and Prod
# https://www.hackerrank.com/challenges/np-sum-and-prod


import numpy

n, m = map(int, input().split())

l = []
for _ in range(n):
    i = list(map(int, input().split()))
    l.append(i)

arr = numpy.array(l)
sum = numpy.sum(arr, axis = 0)
prod = numpy.prod(sum)
print(prod)


#---------------------------------------------------------------------


# Min and Max
# https://www.hackerrank.com/challenges/np-min-and-max


import numpy

n, m = map(int, input().split())

l = []
for _ in range(n):
    i = list(map(int, input().split()))
    l.append(i)
arr = numpy.array(l)


Min = numpy.min(arr, axis = 1)
print(numpy.max(Min))


#----------------------------------------------------------------------

# Mean, Var and Std
# https://www.hackerrank.com/challenges/np-mean-var-and-std


import numpy

n, m = map(int, input().split())

l = []
for _ in range(n):
    i = input().split()
    l.append(i)
arr = numpy.array(l, int)

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr, axis = None), 11))


#----------------------------------------------------------------------

# Dot and Cross product
# https://www.hackerrank.com/challenges/np-dot-and-cross

import numpy as np

n = int(input())

a = []
for _ in range(n):
    a.append(input().split())
A = np.array(a, int)

b = []
for _ in range(n):
    b.append(input().split())
B = np.array(b, int)

print(np.dot(A, B))


#-----------------------------------------------------------------------


# Inner and Outer
# https://www.hackerrank.com/challenges/np-inner-and-outer


import numpy

A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)

print(numpy.inner(A, B))
print(numpy.outer(A, B))


#-----------------------------------------------------------------------

# Polynomials
# https://www.hackerrank.com/challenges/np-polynomials


import numpy

coeff = list(map(float, input().split()))
x = int(input())

print(numpy.polyval(coeff, x))


#-----------------------------------------------------------------------

# Linear Algebra
# https://www.hackerrank.com/challenges/np-linear-algebra


import numpy

n = int(input())

l = [] 
for _ in range(n):
    l.append(input().split())

arr = numpy.array(l, float)

print(round(numpy.linalg.det(arr), 2))
