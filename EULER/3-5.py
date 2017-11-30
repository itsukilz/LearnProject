#!/usr/bin/env python
# encoding: utf-8
import sys
def factorlist(NUM):
    while NUM % 2 == 0:
        NUM = NUM /2
    if NUM == 1:
        return 2
    else:
        f = 3
        while f*f <= NUM:
            if NUM % f == 0:
                NUM = NUM/f
            else:
                f += 2
        return NUM
if __name__ == '__main__':
    NUM = int(sys.argv[1])
    print factorlist(NUM)
