def exchange():
    st = [i for i in input()]
    st2 = []
    temp = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for i in range(len(st)):
        if st[i] == "#":
            st2.append(st[i-2]+st[i-1])
        else:
            st2.append(st[i])
    # for i in st:
    #     ans += temp[int(i)-1]
    return st2
print(exchange())