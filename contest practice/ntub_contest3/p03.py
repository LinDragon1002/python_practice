def counts():
    ar = [[j for j in i]for i in input().split()]
    ans = [0,0]
    for i in range(4):
        if ar[0][i] == ar[1][i]:
            ans[0] += 1
            ar[0][i],ar[1][i] = ".","."
        else:
            for j in range(4):
                if ar[0][i] == ar[1][j]:
                    ans[1] += 1
                    ar[1][j] = "."
                    break
    return f'{ans[0]}A{ans[1]}B'
print(counts())
