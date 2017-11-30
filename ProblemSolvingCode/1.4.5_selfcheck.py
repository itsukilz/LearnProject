#coding=utf-8

#ProblemSolvingWithAlgorithmsandDataStructures
#CP1_PYTHON_REVIEW_1.4.5_SELF_CHECK


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

def score_2_string(new_string_list):

    aim = 'methinks it is like a weasel'
    aim_list = [ch for ch in aim]

    count = 0
    for i in range(27):
        if aim_list[i] == new_string_list[i]:
            count += 1

    similarity = float(count)/float(27)

    return similarity

def repeat(ntimes):
    count = 0
    best_string = []
    best_score = 0
    while  count <= ntimes*1000:
        new_string = generate_string()
        score = score_2_string(new_string)
        
        if score == 1:
            break
        else:
            if score > best_score:
                best_string = new_string
                best_score = score
            if count> 999 and count%1000 == 0:
                print best_score
                print best_string

        count += 1

repeat(5)