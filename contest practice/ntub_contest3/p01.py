def counts():
    inp = []
    ans = []
    for i in range(6):
        st = [i for i in input().split()]
        inp.append(st)
    for i in range(6):
        height = float(inp[i][1]) / 100
        cnt = float(inp[i][2]) / (height ** 2)
        ans.append(int(cnt))
    temp = max(ans)
    return f'{inp[ans.index(temp)][0]} {temp}'
print(counts())