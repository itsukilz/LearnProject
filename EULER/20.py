#!/usr/bin/env python
# encoding: utf-8

num = 1
for i in range(1,101):
    num *= i

string = str(num)
result = 0
for i in string:
    result += int(i)
print result
