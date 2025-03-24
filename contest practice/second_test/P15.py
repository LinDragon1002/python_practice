st = [format(int(i),'b') for i in input().split(",")]
ans = [0,0]

for i in st:
    temp = ""
    for j in range(len(i)-1):
        if i[j] != i[j+1]:
            temp += i[j] + ","
        elif i[j] == i[j+1]:
            temp += i[j]
    temp += i[-1]
    temp = temp.split(",")
    for j in range(len(temp)):
        temp3 = len([j for j in temp[j]])
        if "0" in temp[j]:
            ans[0] = max(ans[0],temp3)
        elif "1" in temp[j]:
            ans[1] = max(ans[1],temp3)
print(abs(ans[0]-ans[1]))