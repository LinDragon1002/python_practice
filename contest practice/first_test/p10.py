def counts():
    st = [0] * 10
    for i in range(10):
        st[i] = int(input())
    st = sorted(st)
    ans = 0
    for i in range(1,9):
        ans += int(st[i])
    print(ans)
    print(f'{ans/(len(st)-2):.2f}')
counts()