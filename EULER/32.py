#coding=utf-8
import math

def check_pandigital(a,b,n):
	x = ['1','2','3','4','5','6','7','8','9']
	l = list(str(a)) + list(str(b)) + list(str(n))
	if len(l) != 9:
		return False
	else:
		l.sort()
		if l != x:
			return False
		else:
			return True

def combination(n):
	r = []
	maxnum = int(math.sqrt(n))
	for i in range(1,maxnum+1):
		if n % i == 0:
			r.append((i,n/i,n))
	return r

# 4-5位数肯定不行
def boundaries():
	i = 1
	while True:
		
		r = combination(i)
		for x in r:
			length_combination = 0
			length_combination += len(str(x[0])) +  len(str(x[1]))+ len(str(x[2]))
			if length_combination < 9:
				print  len(str(i))
		i += 1


def main():
	result = 0
	for n in range(1000,10000):
		r = combination(n)
		for x in r:
			if check_pandigital(x[0],x[1],x[2]) == True:
				result += n
				break
	print result
main()