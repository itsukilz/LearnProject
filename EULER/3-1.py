#coding=utf-8
#暴力判断素数，暴力求最大素因子
#算法不行，运算量太大，速度太慢

def isPrime(N):
	for i in range(2,N):
		if N % i == 0:
			return False
	return True

def biggestPrimeFactor(NUM):
	if isPrime(NUM):
		return NUM
	else:
		for i in range(NUM-1,1,-1):
			if NUM % i == 0:
				if isPrime(i) :
					return i

if __name__ == '__main__':
	print biggestPrimeFactor(600851475143)


