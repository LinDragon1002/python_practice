rowIndex = 1

ans = []
temp = 3
ans.append([1])
ans.append([1,1])
while temp <= rowIndex+1 and rowIndex+1 > 2:
    temp_list = [1]
    for i in range(1,temp-1):
        temp_list.append(ans[temp-2][i-1]+ans[temp-2][i])
    temp_list.append(1)
    temp += 1
    ans.append(temp_list)
if rowIndex == 0:
    print(ans[0])
elif rowIndex == 1:
    print(ans[1])
else:
    print(ans[rowIndex])