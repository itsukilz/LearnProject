#coding=utf-8
#暴力法，38s

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model

def link(num):
	count = 0
	while num != 1:
		
		if num % 2 == 0:
			num = num/2
		else:
			num = num * 3 + 1
		count += 1
	return count

def bruteforcesolution():
	maxlink = 1
	maxnum = 1
	num = 1000000-1
	numlist = []
	countlist = []
	df = pd.DataFrame()
	while num > 1:
		linkcount = link(num)
		if linkcount > maxlink:
			maxlink = linkcount
			maxnum = num

		numlist.append(num)
		countlist.append(linkcount)

		num -= 1
	df['num'] = numlist
	df['count'] = countlist
	df.to_csv('14.csv')


def draw():
	df = pd.read_csv('14.csv')

	plt.plot(df['num'], df['count'],'ro')
	plt.show()
#bruteforcesolution()
draw()