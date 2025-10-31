player = input().split(' ')
m = input().split(' ')
ans = int(player[1])
for i in m:
    if ans > int(i):
        ans += int(i)
    else:
        break
print(ans)