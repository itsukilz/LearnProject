#coding=utf-8
import math
def check_prime(n):
	maxnum = int(math.sqrt(n))
	
	for i in range(2,maxnum+1):
		if n % i == 0:
			return False
	return True

def all_prime():
	n = 2
	l = []
	while n < 1000000:
		if check_prime(n) == True:
			l.append(str(n))
			print n
		n += 1
	f = open('prime.txt','w')
	string = "\n".join(l)
	f.write(string)
	f.close()

def rotation(n):
	templist = list(n)
	l = []
	for i in range(1,len(n)):
		l.append(('').join(templist[i:] + templist[:i]))

	return l

def main():
	f = open('prime.txt')
	allprime = f.readlines()
	f.close()

	r = []
	count = 0
	for i in allprime:
		i = i.strip()

		if len(i) == 1:
			count += 1
			r.append(i)
		else:
			if '0' in i or '2' in i or '4' in i or '6' in i or '8' in i:
				continue
			else:
				l = rotation(i)
				print i,l
				flag = 0
				for j in l:
					if j+'\n' not in allprime:
						flag = 1
						break
				if flag == 0:
					count += 1
					r.append(i)
				else:
					continue
	print r
	print count

main()
