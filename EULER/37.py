#coding=utf-8
def main():
	f = open('prime.txt')
	primes = f.readlines()
	dic = dict.fromkeys(primes,0)

	count = 0
	result = []
	for prime in primes:
		prime = prime.strip()
		temps = list(str(prime))
		length = len(temps)
		
		if length == 1:
			continue
		else:
			flag = 0
			for i in range(1,length):
				stage1 = ''.join(temps[i:])
				stage2 = ''.join(temps[:-i])

				if dic.get(stage1+'\n',-1) != -1 and dic.get(stage2+'\n',-1) != -1 :
					continue
				else:
					flag = 1
					break
				
			if flag == 0:
				result.append(int(prime))
				count += 1
	print sum(result)
	print count

main()