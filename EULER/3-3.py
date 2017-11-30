#!/usr/bin/env python
# encoding: utf-8

import sys

def biggestPrimeFactor(NUM):
    print 'start'
    flag = [True] * (NUM+1)
    print 'end'
    primelist = []
    for i in range(2,NUM):
        if flag[i]:
           primelist.append(i)
        for prime in primelist:
            if i * prime >= NUM:
                break
            flag[i*prime] = False
            if i % prime == 0:
                break
    primelistlength = len(primelist)
    for k in range(primelistlength-1,0,-1):
        if NUM % primelist[k] == 0:
            return primelist[k]


if __name__ == '__main__':
    NUM =  int(sys.argv[1])
    print biggestPrimeFactor(NUM)

