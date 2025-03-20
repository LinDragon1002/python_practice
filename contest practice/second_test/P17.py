s = sorted([int(i) for i in input()],reverse=True)
temp1 = []
temp2 = []
for i in range(len(s)):
    if i < len(s) // 2:
        temp1.append(s[i])
    else:
        temp2.append(s[i])
temp3 = temp1[0]
temp4 = temp2[0]
for i in range(1,len(temp1)):
    temp3 *= temp1[i]
    temp4 += temp2[i]
print(temp3-temp4)