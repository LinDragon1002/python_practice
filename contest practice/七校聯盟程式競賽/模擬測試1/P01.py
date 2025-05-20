from typing import Counter


st = input()
ans = Counter(st)
ans1 = []
for i in ans:
    temp = [i,ans[i]]
    ans1.append(temp)
ans = list(sorted(ans1, key=lambda x:x[1],reverse=True))
print(ans[0][0])