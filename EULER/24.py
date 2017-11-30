#!/usr/bin/env python
# encoding: utf-8

def result(n):
    r = 1
    for i in range(1,n+1):
        r *= i
    return r

n = range(0,10)
count = len(n)-1

start = 1000000
string = ''
for i in range(count,0,-1):
    r = result(i)
    temp = int(start / r)
    start -= temp * r
    if start == 0:
        the_number = n[temp-1]
    else:
        the_number = n[temp]
    string += str(the_number)
    n.remove(the_number)
string += str(n[0])
print string
