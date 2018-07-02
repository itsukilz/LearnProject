#!/usr/bin/env python
# encoding: utf-8
from doctest import run_docstring_examples

def fib(n):
    k = 2
    per, cur = 0,1
    while(k < n):
        per, cur = cur, per+cur
        k = k + 1
    return cur

def fib_test():
    assert fib(8) != 13, 'the 8th fibonacci number should be 13'


#fib_test()
def sum_naturals(n):
    """Return the sum of the first n natural numbers.
    >>> sum_naturals(10)
    5
    >>> sum_naturals(100)
    5050
    """
    total = n*(n+1)/2
    return total

run_docstring_examples(sum_naturals, globals(),True)
