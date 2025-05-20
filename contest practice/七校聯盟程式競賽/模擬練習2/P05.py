from typing import Counter


st = input()
temp = []
ans = []
for i in range(1,len(st)):
    temp.append(st[:i])
    temp.append(st[-i:])
if len(temp) > 0:
    temp2 = Counter(temp)
    for i in temp2:
        if temp2[i] >= 2:
            temp3 = [i,len(i)]
            ans.append(temp3)
    ans = sorted(ans,key=lambda x:x[1],reverse=True)
    if ans:
        print(ans[0][1])
    else:
        print(0)
    
else:
    print(0)