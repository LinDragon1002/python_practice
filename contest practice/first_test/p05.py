def counts():
    st = [i for i in input().split(",")]
    ans = 0
    for i in range(len(st)):
        for j in range(len(st[i])):
            if st[i][j] == "E" and i == 0:
                ans += 500
            elif st[i][j] == "E" and i == 1:
                ans += 400
            elif st[i][j] == "A":
                ans += 800
            elif st[i][j] == "C" and i == 0:
                ans += 200
            elif st[i][j] == "C" and i == 1:
                ans += 100
    if len(st[0])+len(st[1]) >= 20:
        ans *= 0.9
    return int(ans)
print(counts())