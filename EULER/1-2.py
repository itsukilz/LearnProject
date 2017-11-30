#!/usr/bin/env python
# encoding: utf-8
def countfun(base,target):
    num = target / base
    return base*(num+1)*num/2

print countfun(5,999) + countfun(3,999) - countfun(15,999)
