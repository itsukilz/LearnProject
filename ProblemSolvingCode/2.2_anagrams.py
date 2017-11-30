def if_anagrams(string1,string2):
    
    sl1 = [0]*26
    sl2 = [0]*26
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for ch in string1:
        for i in range(26):
            if ch == alpha[i]:
                sl1[i] += 1
                break

    for ch in string2:
        for i in range(26):
            if ch == alpha[i]:
                sl2[i] += 1
                break
    flag = 0
    for j in range(26):
        if sl1[j] != sl2[j]:
            flag = 1
            break

    if flag == 0:
        return True
    else:
        return False

#test

print if_anagrams('python','typhon')
print if_anagrams('heart','earth')
print if_anagrams('kkkwe','wkwke')


