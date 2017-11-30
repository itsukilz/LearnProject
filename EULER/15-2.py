#coding=utf-8

NUM = 20
l = [[1,1]]
level = 1

while level <= NUM-1:
	previous = l[level-1]
	temp = [1]

	for i in range(len(previous)-1):
		temp.append(previous[i]+previous[i+1])
	temp.append(1)
	print temp
	l.append(temp)

	level += 1

count = 0
for i in l[-1]:
	count+= i*i

print count