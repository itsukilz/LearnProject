#coding=utf-8
import math
import copy

def check_prime(n):
	maxnum = int(math.sqrt(n))
	for i in range(5,maxnum+1):
		if n % i == 0:
			return False
	return True

def numbers_9():	
	anumbers = range(1,n)
	l = []
	s = ''
	for a in anumbers:
		bnumbers = copy.deepcopy(anumbers)
		bnumbers.remove(a)
		for b in bnumbers:
			cnumbers = copy.deepcopy(bnumbers)
			cnumbers.remove(b)
			for c in cnumbers:
				dnumbers = copy.deepcopy(cnumbers)
				dnumbers.remove(c)					
				for d in dnumbers:
					enumbers = copy.deepcopy(dnumbers)
					enumbers.remove(d)
					for e in enumbers:
						fnumbers = copy.deepcopy(enumbers)
						fnumbers.remove(e)						
						for f in fnumbers:
							gnumbers = copy.deepcopy(fnumbers)
							gnumbers.remove(f)							
							for g in gnumbers:
								hnumbers = copy.deepcopy(gnumbers)
								hnumbers.remove(g)
								h = hnumbers[0]
								temps = 'n'
								temps += str(a) + str(b) +str(c) +str(d) +str(e) +str(f) +str(g) + str(h) 
								s += temps + '\n'
	f = open('nine_pandigital.txt','w')
	f.write(s)
	f.close()


def numbers_8():	
	anumbers = range(1,8)
	l = []
	s = ''
	for a in anumbers:
		bnumbers = copy.deepcopy(anumbers)
		bnumbers.remove(a)
		for b in bnumbers:
			cnumbers = copy.deepcopy(bnumbers)
			cnumbers.remove(b)
			for c in cnumbers:
				dnumbers = copy.deepcopy(cnumbers)
				dnumbers.remove(c)					
				for d in dnumbers:
					enumbers = copy.deepcopy(dnumbers)
					enumbers.remove(d)
					for e in enumbers:
						fnumbers = copy.deepcopy(enumbers)
						fnumbers.remove(e)						
						for f in fnumbers:
							gnumbers = copy.deepcopy(fnumbers)
							gnumbers.remove(f)							

							g = gnumbers[0]
							temps = '8'
							temps += str(a) + str(b) +str(c) +str(d) +str(e) +str(f) +str(g)  
							s += temps + '\n'
	f = open('eight_pandigital.txt','w')
	f.write(s)
	f.close()

def numbers_7():	
	anumbers = range(1,7)
	l = []
	s = ''
	for a in anumbers:
		bnumbers = copy.deepcopy(anumbers)
		bnumbers.remove(a)
		for b in bnumbers:
			cnumbers = copy.deepcopy(bnumbers)
			cnumbers.remove(b)
			for c in cnumbers:
				dnumbers = copy.deepcopy(cnumbers)
				dnumbers.remove(c)					
				for d in dnumbers:
					enumbers = copy.deepcopy(dnumbers)
					enumbers.remove(d)
					for e in enumbers:
						fnumbers = copy.deepcopy(enumbers)
						fnumbers.remove(e)						
						f = fnumbers[0]
						temps = '7'
						temps += str(a) + str(b) +str(c) +str(d) +str(e) +str(f)  
						s += temps + '\n'
	f = open('seven_pandigital.txt','w')
	f.write(s)
	f.close()

def main_1():
	f = open('seven_pandigital.txt')
	flines = f.readlines()
	f.close()
	result = []
	for i in flines:
		number = int(i.strip())
		if number % 2 == 0 or number % 3 == 0:
			continue
		elif check_prime(number) == True:
			result.append(number)
	print result
	print max(result)

numbers_7()
main_1()