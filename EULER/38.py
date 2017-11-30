#coding=utf-8

i = 2
result = []
while i<10000:
	s = ''
	flag = 0
	for n in range(1,10):
		s += str(n*i)
		if len(s) == 9:
			flag = 1
			break
		elif len(s) > 9:
			flag = 0
			break

	if flag == 1:
		l = list(s)
		l.sort()
		if l == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
			result.append(int(s))
	print i,s
	i += 1


print result
print max(result)