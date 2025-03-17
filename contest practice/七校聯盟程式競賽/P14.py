def counts():
    ans = []
    st = [i for i in input()]
    temp = ""
    for j in range(len(st)):
        temp += st[j]
    ans.append(temp)
    temp = ""
    for j in range(len(st)-1,-1,-1):
        temp += st[j]
    ans.append(temp)
    return ans
print(counts())