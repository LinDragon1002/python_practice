columnTitle = "AAA"
ans = 0
temp = 0
for i in range(len(columnTitle)-1,-1,-1):
    if temp > 0:
        ans += (26 ** temp) * (ord(columnTitle[i]) - 64)
    else:
        ans += ord(columnTitle[i]) - 64
    temp += 1
print(ans)