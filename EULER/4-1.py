#coding=utf-8
#暴力法求两个三位数乘积中最大的回文数
#答案为：906609

def isPalindrome(n):
	s1 = str(n)
	s2 = s1[::-1]
	if s1 == s2:
		return True
	else:
		return False

def productList():
	count = 0
	maxPalindrome = 10000
	for n in range(999,99,-1):
		for m in range(n,99,-1):
			product = n*m
			count += 1
			if isPalindrome(product):
				if product > maxPalindrome:
					maxPalindrome = product
	print count
	return maxPalindrome

if __name__ == '__main__':
	print productList()