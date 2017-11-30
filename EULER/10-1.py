#coding=utf-8
def shaixuan(N):
	
	flag = [True] * N
	
	#even is false
	for i in range(4,N):
		if i % 2 == 0:
			flag[i] = False

	k = 3
	primeList = [2]

	while k < N:
		if flag[k]:
			primeList.append(k)
		for prime in primeList:
			if prime*k >= N:
				break
			flag[prime*k] = False
			if k % prime == 0:
				break
		k += 2
	return sum(primeList)
if __name__ == '__main__':
	N = 2000000
	print shaixuan(N)