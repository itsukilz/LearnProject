#coding=utf-8

# 算法的目的是找一列数中的最小值

# quadratic 
def quadratic_findmin (list_of_number):
    
    length = len(list_of_number)
    min_of_list = 0
    
    for i in range(length):
        flag = 0
        for j in range(i+1,length):
            if list_of_number[i] >= list_of_number[j]:
                flag = 1
                break

        if flag == 0:
            min_of_list = list_of_number[i]
            break

    return min_of_list


# linear
def linear_findmin(list_of_number):

    length = len(list_of_number)
    min_of_list = list_of_number[0]

    for i in list_of_number[1:]:
        if i < min_of_list:
            min_of_list = i

    return min_of_list

# test
# k = [random.randint(0,194) for p in range(58)]

import time
import random
#k = [1, 85, 145, 154, 189, 71, 86, 180, 167, 20, 112, 165, 20, 100, 116, 145, 181, 49, 159, 89, 43, 46, 145, 98, 94, 134, 188, 14, 41, 82, 87, 71, 6, 60, 43, 12, 9, 19, 51, 113, 14, 123, 46, 149, 36, 141, 43, 169, 47, 10, 100, 80, 110, 67, 175, 176, 161, 136]


k = [random.randint(0,194) for p in range(5800)]

start1 = time.time()
min1 = quadratic_findmin(k)
end1 = time.time()

start2 = time.time()
min2 = linear_findmin(k)
end2 = time.time()

print 'quadratic time is %14.9f and linear time is %14.9f， quadratic is %d times linear' % (end1-start1, end2-start2, ((end1-start1)/(end2-start2)))




