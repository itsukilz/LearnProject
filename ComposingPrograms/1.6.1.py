#!/usr/bin/env python
# encoding: utf-8

def sum_of_pattern(n, pattern):
    total = 0
    k = 1
    while k <= n:
        total += pattern(k)
        k += 1
    return total

def cube(x):
    return x*x*x

def square(x):
    return x*x

def natural(x):
    return x

def sum_of_cube(n):
    return sum_of_pattern(n, cube)
