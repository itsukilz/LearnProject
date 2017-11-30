#coding=utf-8

def f(a):
	return (1000*a-500000-a*a)/(a-1000)

for i in range(1,1000):
	c = f(i)
	b = (1000-c-i)
	if i < (1000-c-i) and (1000-c-i) < c :
		if i*i + b*b == c*c:
			print i,b,c
			print i*b*c