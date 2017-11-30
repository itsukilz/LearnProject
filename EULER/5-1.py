#coding=utf-8
def hebing(a,b):
	length_b = len(b)
	k = 0
	while k < length_b:
		cha = b.count(b[k]) - a.count(b[k])
		if cha > 0:
			for p in range(cha):
				a.append(b[k])
			k += cha + 1
		else:
			k += b.count(b[k]) + 1
	return a


def main():
	primelist = [2,3]
	clist = []
	for n in range(4,21):
		fl = []
		for prime in primelist:
			while n%prime == 0:
				n = n/prime
				fl.append(prime)
			if n == 1:
				clist.append(fl)
				break
		if len(fl) == 0:
			primelist.append(n)

	for fl in clist:
		primelist = hebing(primelist,fl)

	result = 1
	for i in primelist:
		result *= i
	return result

if __name__ == '__main__':
	print main()