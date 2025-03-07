def exchange():
    st = [i for i in input().split(" ")]
    ans = []
    for i in range(len(st)):
        ans.append(st[i].upper())
    print(" ".join(ans))
    ans.clear()
    for i in range(len(st)):
        temp = [i for i in st[i]]
        temp[0] = temp[0].upper()
        ans.append("".join(temp))
    print(" ".join(ans))
exchange()