def exchange():
    st = [i for i in input()]
    st2 = []
    temp = "abcdefghijklmnopqrstuvwxyz"
    ans = ""
    for i in range(len(st)):
        if st[i] == "#":
            st2.pop()
            st2.pop()
            st2.append(st[i-2]+st[i-1])
        else:
            st2.append(st[i])
    for i in st2:
        ans += temp[(int(i)-1) % 26]
    return ans
print(exchange())