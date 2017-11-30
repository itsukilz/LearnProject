#coding=utf-8

import sys
import math
import cProfile
NUM = 500


def primelist(k):
	primelist = []
	while k % 2 == 0:
		k  = k/2
		primelist.append(2)

	for i in range(3,k,2):
		while k % i == 0:
			k  = k/i
			primelist.append(i)

	if k != 1:
		primelist.append(k)
	
	return primelist


def countfactor(plist):
	countlist = []
	i = 0
	while i < len(plist):
		fmove = plist.count(plist[i])
		countlist.append(fmove)
		i += fmove

	count = 1
	for j in countlist:
		count *= (j+1)
	return count

def main():
	n = 8
	while True:
		
		count = test(n)
		if count >= NUM:
			print n
			break
		n += 1

def test(n):
	if n % 2 == 0:
		a = n/2
		b = n+1
	else:
		a = (n+1)/2
		b = n

	plist = primelist(a) + primelist(b)
	count = countfactor(plist)
	print n,a*b,count,plist
	return count


def debug():
	n = int(sys.argv[1])
	k = n*(n+1)/2
	plist = primelist(k)
	count = countfactor(plist)

	test(n)
	print n,k,plist,count

cProfile.run('main()')