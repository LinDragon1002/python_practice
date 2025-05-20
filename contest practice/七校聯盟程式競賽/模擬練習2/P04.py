import string
st = input()
temp = string.punctuation
ans = []
for i in range(len(st)):
    cnt = 0
    if st[i] in temp:
        cnt = 1
        for j in range(i+1,len(st)):
            if st[j] in temp:
                cnt += 1
            else:
                break
        ans.append(cnt)
ans = sorted(ans,reverse=True)
if len(ans) > 0:
    print(ans[0])
else:
    print(0)
