a = input().split(' ')
ans = 0
for i in range(int(a[0]),int(a[1])):
    temp = 0
    n = len(str(i))
    for j in str(i):
        temp += int(j) ** n
    if i == temp:
        ans += 1
print(ans)