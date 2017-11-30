#!/usr/bin/env python
# encoding: utf-8

import math

def proper_divisor(n):
    maxnum = int(math.sqrt(n))
    divisor = [1]
    for i in range(2,maxnum+1):
        if n % i == 0:
            divisor.append(i)
            if n/i != i:
                divisor.append(n/i)
    return sum(divisor)

def main():
    abundant_num_list = []
    for i in range(2,28124):
        if proper_divisor(i) > i:
            abundant_num_list.append(i)

    length = len(abundant_num_list)
    allsum =[0]+ [1]*(28123)
    for i in range(length):
        for j in range(i,length):
            k = abundant_num_list[i]+abundant_num_list[j]
            if k > 28123:
                continue
            else:
                allsum[k] = 0
    result = 0
    for i in range(1,28124):
        if allsum[i] != 0:
            result += i
    print result
main()
