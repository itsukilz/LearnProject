#!/usr/bin/env python
# encoding: utf-8
import sys
def factorlist(NUM):
    f = 2
    while f*f <= NUM:
        if NUM % f == 0:
            NUM = NUM/f
        else:
            f += 1
    return NUM
if __name__ == '__main__':
    NUM = int(sys.argv[1])
    print factorlist(NUM)
