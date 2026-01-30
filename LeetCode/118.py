numRows = 5
ans = []
if numRows == 1:
    ans.append([1])
elif numRows == 2:
    ans.append([1])
    ans.append([1,1])
else:
    temp = 3
    ans.append([1])
    ans.append([1,1])
    while temp <= numRows:
        temp_list = [1]
        for i in range(1,temp-1):
            temp_list.append(ans[temp-2][i-1]+ans[temp-2][i])
        temp_list.append(1)
        temp += 1
        ans.append(temp_list)

print(ans)