def sorts():
    ar = [int(i) for i in input().split()]
    temp = sorted(ar)
    ans = 0
    for i in range(len(temp)):
        if ar[i] != temp[i]:
            ans += 1
    return ans
print(sorts())