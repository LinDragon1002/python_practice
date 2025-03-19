def counts():
    ar = [int(i) for i in input().split()]
    temp = {}
    ans = {}
    for i in range(len(ar)):
        if ar[i] not in temp:
            temp[ar[i]] = 1
        else:
            temp[ar[i]] += 1
    for i in temp:
        if temp[i] not in ans:
            ans[temp[i]] = 1
        else:
            ans[temp[i]] += 1
    if max(ans.values()) > 1:
        return False
    return True
print(counts())