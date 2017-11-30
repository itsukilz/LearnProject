#!/usr/bin/env python
# encoding: utf-8

def d(n):
    if n % 2 == 0 or n % 5 == 0:
        return 0
    else:
        fenzi = 10
        fenmu = n
        l = []
        while True:
            temp = fenzi % fenmu
            if temp in l:
                return len(l) - l.index(temp)
            else:
                l.append(temp)
                fenzi = temp * 10

maxd = 0
maxi = 0
for i in range(2,1000):
    k = d(i)
    if k > maxd:
        maxd = k
        maxi = i
print maxi
