num = int(input())
ans = [[1],[1,1]]
for i in range(3,num+1):
    temp = []
    for j in range(i):
        if j == 0 or j == i-1:
            temp.append(1)
        else:
            temp.append(ans[i-2][j-1] + ans[i-2][j])
    ans.append(temp)
if num == 1:
    print(*ans[0])
elif num == 2:
    print(*ans[1],sep=' ')
else:
    print(*ans[-1],sep=' ')