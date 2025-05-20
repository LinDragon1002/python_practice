st = input()
ans = []
cnt = 0
for i in range(len(st)):
    if st[i] == '{':
        cnt += 1
        ans.append(cnt)
    elif st[i] == '}':
        cnt -= 1
        ans.append(cnt)
if cnt == 0:
    print(max(ans))
else:
    print(-1)