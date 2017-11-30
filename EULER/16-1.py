#coding=utf-8
import math

def sumofdigits(n):
	r = 0
	for i in n:
		r += int(i)
	return r
def multiple(base,n):
	string = str(base)
	length = len(string)

	result = [0]*length

	for i in range(length-1,-1,-1):
		temp = int(string[i]) * n
		result[i] += temp
		
		if result[i] >= 10 and i > 0:
			result[i-1] += result[i]/10
			result[i] = result[i] % 10

	final = ''
	for i in result:
		final += str(i)

	return final


def main():
	n = 1024
	
	for i in range(99):
		n = multiple(n,1024)

	print sum([int(digits) for digits in  str(n)])

main()