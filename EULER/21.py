#!/usr/bin/env python
# encoding: utf-8

import math

def proper_divisor(n):
    maxnum = int(math.sqrt(n))
    divisor = [1]
    for i in range(2,maxnum+1):
        if n % i == 0:
            divisor.append(i)
            divisor.append(n/i)
    return sum(divisor)

def main():
    dic = dict.fromkeys(range(2,10000),0)
    amicable_sum = 0
    amicable_list = []
    for i in range(2,10000):
        if dic[i] == 1:
            continue
        else:
            d = proper_divisor(i)
            if d < 10000 and  d != i and proper_divisor(d) == i:
                amicable_sum += d + i
                amicable_list.append(set([d,i]))
            dic[d] = 1
            dic[i] = 1
    print amicable_sum

main()
