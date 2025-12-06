st = input()
ans = 0
for i in range(len(st)-1):
    if st[i] == st[i+1]:
        ans += 1
print(ans)