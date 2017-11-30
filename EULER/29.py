#!/usr/bin/env python
# encoding: utf-8
import math

l = []
for i in range(2,101):
    for j in range(2,101):
        k = math.pow(i,j)
        l.append(k)
print len(set(l))
