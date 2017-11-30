#coding=utf-8

fo = open('13.txt')
numbers = fo.readlines()

sumlist = [0]*100

for i in range(49,-1,-1):
	for everyline in numbers:
		sumlist[i] += int(everyline[i])

	if sumlist[i] > 0 and i > 0:
		sumlist[i-1] += sumlist[i]/10
		sumlist[i] = sumlist[i] % 10


length =len(str(sumlist[0]))
string = ''
for k in range(10-length+1):
	string += str(sumlist[k])

print string