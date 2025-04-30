def counts():
    st1 = [int(i) for i in input().split(" ")]
    temp1 = []
    for i in range(st1[0]):
        st2 = list(map(int, input().split()))
        temp1.append(st2)

    st3 = [int(i) for i in input().split(" ")]
    temp2 = []
    for i in range(st3[0]):
        st4 = list(map(int, input().split()))
        temp2.append(st4)

    if st1[1] != st3[0]:
        return
    ans = [[0] * st3[1] for _ in range(st1[0])]

    for i in range(st1[0]):
        for j in range(st3[1]):
            for k in range(st1[1]):
                ans[i][j] += temp1[i][k] * temp2[k][j]
    for i in ans:
        for j in i:
            print(j,end=' ')
        print()
counts()