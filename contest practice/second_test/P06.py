st = [i for i in input().split(",")]
temp1 = []
temp2 = []
for i in range(len(st)):
    temp1.append(sorted(set(st[i])))
temp1 = sorted(temp1,reverse=True)

for i in temp1[0]:
    temp = 0
    for j in range(len(st)):
        temp += st[j].count(i)
    temp /= len(st)
    temp2.append(temp)
ans = list(set(temp2))
if len(ans) == 1:
    temp = ans[0]
    if type(temp) == float:
        print(0)
    else:
        print(1)
else:
    print(0)
