num = int(input())
ans = [[] for _ in range(num)]
for i in range(1,num+1):
    if i == 1:
        ans[i-1].append("1")
    elif i == 2:
        ans[i-1].append("1")
        ans[i-1].append("1")
    else:
        for j in range(i):
            if j == 0 or j == i-1:
                ans[i-1].append("1")
            else:
                ans[i-1].append(str(int(ans[i-2][j-1])+int(ans[i-2][j])))
for i in ans:
    print(" ".join(i))