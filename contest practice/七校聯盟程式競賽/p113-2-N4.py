st = input()
ans = ""
for i in range(0,len(st),2):
    ans += st[i] * int(st[i+1])
print(ans)