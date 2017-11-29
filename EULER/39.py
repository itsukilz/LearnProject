#coding=utf-8
import math
def square():
	string = ''
	for i in range(0,1000):
		string += str(i*i) + '\n'
	f = open('square.txt','w')
	f.write(string)
	f.close()

def main():
	f = open('square.txt')
	flines = f.readlines()
	f.close()

	dic = dict.fromkeys(flines,0)
	result = {}
	for i in range(1,1000):
		for j in range(i,1000):
			a2 = int(flines[i].strip())
			b2 = int(flines[j].strip())
			c2 = a2+b2

			if dic.get(str(c2)+'\n',-1) != -1:
				p =  math.sqrt(c2)+ i + j
				if p <= 1000:
					if result.get(p,-1) == -1:
						result[p] = 1
					else:
						result[p] += 1

	k = sorted(result.items(), lambda x, y: cmp(x[1], y[1]), reverse=True) 
	print k[0][0]
	print k

main()
