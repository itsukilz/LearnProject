import copy

def nextGreaterElement(findNums, nums):
    """
    :type findNums: List[int]
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for i in findNums:
        temp = copy.deepcopy(nums)
        tempmax = -1
        while True:
            k = temp.pop()
            if k == i:
                break
            else:
                if k>i:
                    tempmax=k
        result.append(tempmax)
    return result

if __name__ == '__main__':
    print nextGreaterElement([2,4],[1,2,3,4])