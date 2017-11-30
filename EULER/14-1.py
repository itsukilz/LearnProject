#coding=utf-8
#暴力法，38s
def link(num):
	count = 0
	while num != 1:
		
		if num % 2 == 0:
			num = num/2
		else:
			num = num * 3 + 1
		count += 1
	return count

def main():
	maxlink = 1
	maxnum = 1
	num = 1000000-1
	while num > 1:
		linkcount = link(num)
		if linkcount > maxlink:
			maxlink = linkcount
			maxnum = num

		print num,linkcount
		num -= 1
	print maxnum,maxlink

print link(3)