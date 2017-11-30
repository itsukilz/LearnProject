#coding=utf-8
#暴力法，38s

import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


def draw():
	df = pd.read_csv('draw.csv')

	plt.plot(df['num'], df['count'],'ro')
	plt.show()
#bruteforcesolution()
draw()