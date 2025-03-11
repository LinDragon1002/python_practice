def x():
    st = [i for i in input()]
    ans = ""
    for i in range(len(st)):
        if st[i] != "=":
            ans += st[i]
        else:
            temp = ""
            for j in range(i+1,len(st)):
                temp += st[j]
            break

    for i in range(1,101):
        if eval(ans,{"X":i}) == eval(temp,{"X":i}):
            print(i)
            break

x()