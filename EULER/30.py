#!/usr/bin/env python
# encoding: utf-8

import math
def fifth_power(n):
    digits = str(n)
    allsum = 0
    for i in digits:
        allsum  += math.pow(int(i),5)
    return int(allsum)

def biggest():
    nine_fifth = int(math.pow(9,5))
    count= 2
    while True:
        product = nine_fifth * count
        
        if len(str(product)) < count:
            return count
        else:
            count += 1
count = biggest() 
i = 10
result = 0
while i < math.pow(10,count-1):
    if fifth_power(i) == i:
        result+= i
    i += 1

print result