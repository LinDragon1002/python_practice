from typing import Counter
# def counts():
#     st = [i for i in input()]
#     ans = {}
#     for i in range(len(st)):
#         if st[i] not in ans:
#             ans[st[i]] = 1
#         else:
#             ans[st[i]] += 1
#     ans = sorted(ans.items(),key= lambda x:x[0])
#     ans = dict(ans)
#     ans = sorted(ans.items(),key= lambda x:x[1],reverse=True)
#     for i in range(len(ans)):
#         for j in range(1,len(ans[i])):
#             print(ans[i][0]+","+str(ans[i][j])) 
# counts()

st = input()
total = Counter(st)
ans = []
for i in total:
    temp = [i,total[i]]
    ans.append(temp)
ans = list(sorted(ans,key= lambda x:(-x[1],x[0])))
for i in ans:
    print(*i,sep=",")