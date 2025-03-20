st = [i for i in input().split(",")]
temp1 = []
temp2 = []
for i in range(len(st)):
    temp1.append(sorted(set(st[i])))
temp1 = sorted(temp1)
for i in temp1[0]:
    temp = 0
    for j in range(len(st)):
        temp += st[j].count(i)
    temp2.append(temp)

ans = {}
for i in temp2:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1
if len(ans) > 1:
    print(0)
else:
    print(1)
