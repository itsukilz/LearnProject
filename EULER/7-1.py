#coding=utf-8
#求第10001个素数

def main():
	primelist = [2,3,5,7,11,13]
	n = 14
	while True:
		flag = 0
		for prime in primelist:
			if n%prime == 0:
				flag = 1
				break
			else:
				continue

		if flag == 0:
			primelist.append(n)

		if len(primelist) == 10001:
			return n
			break
		else:
			n = n + 1
			while n % 2 == 0:
				n = n + 1

		print len(primelist)
if __name__ == '__main__':
	print main()