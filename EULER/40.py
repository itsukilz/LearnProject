#coding=utf-8

i = 1
s = ''
result = 1
while True:
	s += str(i)
	length = len(s)
	if len(s) >= 1000000:
		break
	i += 1

for j in [1,10,100,1000,10000,100000,1000000]:
	result *= int(s[j-1])
	print s[j-1]
print result