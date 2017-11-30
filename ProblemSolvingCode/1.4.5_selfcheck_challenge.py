#coding=utf-8

#ProblemSolvingWithAlgorithmsandDataStructures
#CP1_PYTHON_REVIEW_1.4.5_SELF_CHECK_CHALLENGE
#对selfcheck进行改进，思想是，保留命中的字符，在此基础上修改一个，不断的提高命中数，最后达到完全一致。

import random

def generate_string():
    # 26个字母+1个空格
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']

    #需要random出28下
    new_string = []
    for i in range(28):
        #randint(a,b) that a <= N <= b
        new_string.append(alpha[random.randint(0,26)])
    return new_string

def score_2_string(new_string_list,count_list):

    aim = 'methinks it is like a weasel'
    aim_list = [ch for ch in aim]

    count = 0
    
    for i in range(28):
        if aim_list[i] == new_string_list[i]:
            count += 1
            count_list[i] = 1

    #similarity = float(count)/float(27)

    return count,count_list

def change_one(count_list):
    # 26个字母+1个空格
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    change_one_ch = alpha[random.randint(0,26)]
    

    aim = 'methinks it is like a weasel'
    aim_list = [ch for ch in aim]

    flag = (change_one_ch == aim_list[count_list.index(0)])
    return flag, change_one_ch

def repeat(ntimes):
    count = 0
    count_list = [0]*28

    best_string = []
    best_score = 0

    #第一步，生成一个new_string并且保证count>=2
    while 1:
        new_string = generate_string()
        count,count_list = score_2_string(new_string,count_list)
        if count > 1:
            best_string = new_string
            print 'first best_string:',best_string
            print count
            break

    #第二步，在new_string的基础上改一个字符,check new_string改的那个字符怎样
    while count_list.count(1) < ntimes:
        flag,change_one_ch = change_one(count_list)
        if flag :
            best_string[count_list.index(0)] = change_one_ch
            count_list[count_list.index(0)] = 1
            print best_string
            print count_list.count(1)



ntimes = int(raw_input('需要命中多少个？'))

repeat(ntimes)


