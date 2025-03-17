def counts():
    st = [i for i in input().split(".")]
    ans = []
    if len(st[0]) % 2 != 0:
        st[0] = "0" + st[0]
    if len(st[1]) % 2 != 0:
        st[1] = st[1] + "0"
    for i in range(len(st)):
        temp = ""
        for j in range(0,len(st[i]),2):
            temp += str(int(st[i][j]) * 3 + int(st[i][j+1]))
        ans.append(temp)

    return ".".join(ans)
print(counts())