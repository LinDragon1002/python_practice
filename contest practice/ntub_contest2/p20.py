def distance():
    st1,st2 = input(),input()
    temp = []
    ans = []
    for i in range(len(st1)):
        if st1[i] == st2:
            temp.append(i)
    for i in range(len(st1)):
        temp1 = []
        for j in range(len(temp)):
            temp1.append(abs(temp[j] - i))
        ans.append(min(temp1))
    return ans
print(distance())