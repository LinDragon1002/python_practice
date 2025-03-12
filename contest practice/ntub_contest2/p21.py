def counts():
    st1,st2 = sorted(input()),sorted(input())
    temp1,temp2 = sorted(list(set(st1))), sorted(list(set(st2)))
    if len(temp1) != len(temp2):
        return False
    for i in range(len(temp1)):
        temp3 = 0
        for j in range(len(temp2)):
            if temp1[i] == temp2[j]:
                if st1.count(temp1[i]) == st2.count(temp2[j]):
                    break
                else:
                    return False
            else:
                temp3 += 1
        if temp3 == len(temp2):
            return False
            
    return True
print(counts())

