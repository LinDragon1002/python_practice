def exchange():
    st = [i for i in input()]
    temp = "abcdefghijklmonpqrstuvwxyz"
    for i in range(len(st)):
        if i < len(st) - 1 and st[i].islower() and st[i+1].isdigit():
            number = temp.find(st[i])
            # if number+int(st[i+1]) >= 26:
            #     st[i+1] = temp[number+int(st[i+1])-26]
            # else:
            st[i+1] = temp[number+int(st[i+1])]
    return "".join(st)


print(exchange())
