#coding=utf-8

def traigle_number():
	i = 1
	s = ''
	value = 0
	while value <= 2600:
		value = (i+1)*i/2
		s += str(value)+'\n'
		i += 1
	f = open('traigle_number.txt','w')
	f.write(s)
	f.close()

def word_value():
	f = open('p042_words.txt')
	fline = f.readlines()[0].split(',')
	
	
	alpha_dic = {}
	for i,p in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
		alpha_dic[p] = i+1

	traigle_dic = {}
	f2 = open('traigle_number.txt').readlines()
	traigle_dic = dict.fromkeys(f2,0)
	#print traigle_dic

	count = 0
	for i in fline:
		value = 0
		word = i[1:-1]

		for char in word:
			value += alpha_dic[char]
			#print value
		if traigle_dic.get(str(value)+'\n',-1) != -1:
			count += 1
	print count
word_value()