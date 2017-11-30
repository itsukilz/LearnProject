#!/usr/bin/env python
# encoding: utf-8

from time import ctime

print ctime()
sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print sum
print ctime()
