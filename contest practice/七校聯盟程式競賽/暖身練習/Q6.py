st = input()
ans = []
cnt = 1
for i in range(len(st)-1):
    if st[i] == st[i+1]:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 1
ans.append(cnt)
ans = sorted(ans,reverse=True)
print(ans[0])