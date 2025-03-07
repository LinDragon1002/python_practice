def counts():
    st = [i for i in input()]
    ans = {}
    for i in range(len(st)):
        if st[i] not in ans:
            ans[st[i]] = 1
        else:
            ans[st[i]] += 1
    ans = sorted(ans.items(),key= lambda x:x[0])
    ans = dict(ans)
    ans = sorted(ans.items(),key= lambda x:x[1],reverse=True)
    for i in range(len(ans)):
        for j in range(1,len(ans[i])):
            print(ans[i][0]+","+str(ans[i][j])) 
counts()