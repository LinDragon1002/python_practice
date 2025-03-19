def counts():
    ar = sorted([int(i) for i in input().split()],reverse=True)
    ans = 0
    for i in range(1,len(ar),2):
        ans += ar[i]
    return ans
print(counts())
