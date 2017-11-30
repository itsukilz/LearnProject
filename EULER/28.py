#!/usr/bin/env python
# encoding: utf-8

def spiral(N):
	num = 1
	p = 2
	l = [1]
	while True :
	    for i in range(0,4):
	        num += p
	        if num > N*N:
	            return sum(l)
	        l.append(num)
	    p += 2

print spiral(1001)