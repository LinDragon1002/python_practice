st = [i for i in input()]
num = [int(i) for i in input().split()]
temp = []
ans = ""
for i in range(num[1],num[0]-1,-1):
    temp.append(st[i])
number = 0
for i in range(len(st)):
    if num[0] <= i <= num[1]:
        ans += temp[number]
        number += 1
    else:
        ans += st[i]
print(ans)