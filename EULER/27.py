#!/usr/bin/env python
# encoding: utf-8
# 第一种思路：暴力法，遍历所有的a,b，找出此刻能产生质数的最大值
# 改进第一种思路：n = 0 时，b是素数； n=1是，a+b+1 是素数。
def isPrime(x):
	if x < 0 :
		return False
	for i in range(2,x):
		if x % i == 0:
			return False
	return True


def f(a,b):
	n = 0
	while True:
		r = n*n + a*n + b
		#print n,r,isPrime(r) 
		if isPrime(r) != True:
			return n
		n += 1

def main():
	maxab = (0,0)
	maxnum = 0

	for a in range(-999,1000):
		for b in range(1,1001,2):
			if isPrime(b) == False or isPrime(a+b+1) == False:
				continue
			else:
				num = f(a,b)
				print a,b,num
				if num > maxnum:
					maxnum = num
					maxab = (a,b)

	print maxnum,maxab

import cProfile
cProfile.run('main()')