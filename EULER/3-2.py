#!/usr/bin/env python
# encoding: utf-8

import sys

def biggestPrimeFactor(NUM):
    flag = [True] * (NUM+1)
    for i in range(2,NUM+1):
        if flag[i]:
            for j in range(i, NUM/i):
                flag[i*j] = False

    for i in range(NUM-1,2,-1):
        if flag[i]:
            if NUM % i == 0:
                return i

if __name__ == '__main__':
    NUM =  int(sys.argv[1])
    print biggestPrimeFactor(NUM)

