def row():
    ar = [i for i in input().split(" ")]
    ans = 0
    temp = ["qwertyuiop","asdfghjkl","zxcvbnm"]
    for i in range(len(ar)):
        temp1 = list(set(i for i in ar[i].lower()))
        temp2 = [0] * 3
        for j in range(len(temp1)):
            if temp1[j] in temp[0]:
                temp2[0] += 1
            elif temp1[j] in temp[1]:
                temp2[1] += 1
            elif temp1[j] in temp[2]:
                temp2[2] += 1
        if len(temp1) in temp2:
            ans += 1
        
    return ans
print(row())