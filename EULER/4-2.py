#coding=utf-8
#思路：利用回文数的特性，把所有回文数从大到小去判断是否为两个三位数的乘积

##是否是两个三位数的乘积
def isTwoThree(n):
	f = 101
	while f*f <= n:
		if n % f == 0 and (n/f >= 100 and n/f <= 999):
			return 1
		else:
			f += 1
	return -1

def main():
	A = ['9','8','7','6','5','4','3','2','1']
	B = ['9','8','7','6','5','4','3','2','1','0']
	C = ['99','88','77','66','55','44','33','22','11','00']
	D = ['9','8','7','6','5','4','3','2','1','0']

##6位数
	for a in A:
		for b in B:
			plist = []
			for c in C:
				string = a+b+c+b+a
				plist.append(int(string))

			for p in plist:
				f = isTwoThree(p)
				if f != -1:
					return p
##5位数
	for a in A:
		for b in B:
			plist = []
			for d in D:
				string = a+b+d+b+a
				plist.append(int(string))

			for p in plist:
				f = isTwoThree(p)
				if f != -1:
					return p


if __name__ == '__main__':
	print main()