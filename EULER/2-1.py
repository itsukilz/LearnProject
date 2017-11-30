#coding=utf-8
#project euler 2
#求斐波那契饿数列中小于指定值所有的even（偶数）之和
#纯暴力测试答案，答案为4613732


#一个有记忆功能的f数列生成器
fl = [1,2]
def f(n):
	global fl
	if n-1 < len(fl):
		return fl[n-1]
	else:
		fn = f(n-1)+f(n-2)
		fl.append(fn)
		return fn

sum = 0
i = 1
while True:
	fi = f(i)
	if fi > 4000000:
		break
	if fi % 2 == 0:
		sum += fi
	i += 1
print sum


