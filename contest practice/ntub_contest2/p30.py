def counts():
    ar = [int(i) for i in input().split()]
    cnt = 0
    ans = [0]
    for i in range(len(ar)):
        cnt += + ar[i]
        ans.append(cnt)

    return max(ans)
print(counts())