#coding=utf-8
#带记忆
def link(num,dic):
	start = num

	if dic.get(start,-1) != -1:
		return dic.get(start,-1),dic
	else:
		count = 0
		while num != 1:
			flag = dic.get(num,-1)
			if flag != -1:
				count += flag
				break
			else:	
				if num % 2 == 0:
					num = num/2
				else:
					num = num * 3 + 1
				count += 1
		dic[start] = count
		return count,dic

def main():
	maxlink = 1
	maxnum = 1
	num = 2
	dic = {}
	while num < 1000000:
		linkcount,dic = link(num,dic)
		if linkcount > maxlink:
			maxlink = linkcount
			maxnum = num
		print num,linkcount
		num += 1
	print maxnum,maxlink

main()