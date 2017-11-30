#coding=utf-8
import math
r = 0
i = 1
while i <= 1000:
	r += math.pow(i,i)
	i += 1

print str(r)[-10:]