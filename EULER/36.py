#coding=utf-8

def binary(n):
	b = ''
	while True:
		tempn = n / 2
		b += str(n % 2)
		if tempn == 0:
			break
		n = tempn

	return b == b[::-1]

def main():
	result = 0
	l = []
	n = 1
	while n < 1000000:
		s = str(n)
		if s[::-1] == s:
			if binary(n) == True:
				result += n
				l.append(n)

		n += 1
	print l
	print result

main()