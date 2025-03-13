def counts():
    ar = [int(i) for i in input().split(" ")]
    ans = 0
    temp = list(set(ar))
    for i in range(len(temp)):
        if ar.count(temp[i]) == 1:
            ans += temp[i]
    return ans
print(counts())
    