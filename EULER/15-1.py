#coding=utf-8
#递归法找规律，14以上速度就慢
global dic
global count
def makedic(NUM):
	dic = {}
	for i in range(NUM+1):
		for j in range(NUM+1):
			point = str(i)+str(j)

			if i == NUM and j < NUM:
				ndown = str(i)+str(j+1)
				dic[point] = [ndown]
			elif i < NUM and j == NUM:
				nright = str(i+1) + str(j)
				dic[point] = [nright]
			elif i < NUM and j < NUM:
				ndown = str(i)+str(j+1)
				nright = str(i+1) + str(j)
				dic[point] = [ndown, nright]
			elif i == NUM and j == NUM:
				dic[point] = 'end'
	return dic

def getNext(point):
	global dic
	global count
	nextpoint = dic[point]
	#print point, nextpoint
	if nextpoint == 'end':
		count += 1
	else:
		for i in nextpoint:
			getNext(i)


def main():
	global dic
	global count
	for i in range(1,16):	
		dic = makedic(i)
		count = 0
		getNext('00') 
		print i,count

print makedic(3)