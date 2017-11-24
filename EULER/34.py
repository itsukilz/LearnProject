import math
def f():
	l = []
	for n in range(1,10):
		r = 1
		for i in range(2,n+1):
			r *= i
		l.append(r)
	print l

# maxnum = 10^7
def maxnum():
	n = 2
	r = f(9)
	while True:
		if n * r < int('9'*n):
			return n
		else:
			n += 1

def main():
	allsum = 0
	l = [1,1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
	for i in range(11,362880*7):
		tempsum = 0
		templist = list(str(i))
		if l[int(max(templist))] >= i or l[int(min(templist))] >= i:
			continue
		else:
			for j in str(i):
				tempsum += l[int(j)]
			print i,tempsum
			if tempsum == i:
				allsum += i
	print allsum
main() 