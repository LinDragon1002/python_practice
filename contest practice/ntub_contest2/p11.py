def exchange():
    st = [i for i in input()]
    temp = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(st) - 1):
        if st[i].islower() and st[i+1].isdigit():
            number = temp.index(st[i])
            st[i+1] = temp[(number+int(st[i+1])) % 26]
    return "".join(st)
print(exchange())
