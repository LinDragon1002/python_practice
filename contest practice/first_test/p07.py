def strings():
    st = [[]] * 3
    temp = []
    ans = ""
    for i in range(3):
        st[i] = [i for i in input()]
        temp.append(len(st[i]))
    temp = sorted(temp,reverse=True)
    for i in range(len(temp)):
        if len(st[i]) < temp[0]:
            for j in range(i,temp[0]-len(st[i])+i):
                st[i].append("")
    for i in range(temp[0]):
        if i % 2 == 0:
            ans += st[0][i] + st[1][i] + st[2][i]
        else:
            ans += st[2][i] + st[1][i] + st[0][i]
    return ans
print(strings())