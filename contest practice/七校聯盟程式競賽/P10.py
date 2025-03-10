def counts():
    st = sorted([int(i) for i in input().split(",")])
    for i in range(len(st)-1):
        if st[i+1] % st[0] == 0:
            ans = 1
        else:
            ans = 0
            break
    return ans
print(counts())