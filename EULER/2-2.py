#coding=utf-8
#project euler 推导了fobinacci数列的通项公式
#Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed four million.
import math

def f(n):
	return (math.pow(((1+math.sqrt(5))/2),n+1))/math.sqrt(5) - (math.pow(((1-math.sqrt(5))/2),n+1))/math.sqrt(5)

sum = 0
i = 2
NUM = 4000000

while True:
	if f(i) <= NUM:
		sum += f(i)
		i += 3
	else:
		break

print math.floor(sum)