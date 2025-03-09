def counts():
    st = input()
    st1 = ""
    for i in range(len(st)-1):
        if st[i] != st[i+1]:
            st1 += st[i] + ","
        elif st[i] == st[i+1]:
            st1 += st[i]
    st1 += st[-1]
    st1 = st1.split(",")
    ans = [0,0]
    for i in range(len(st1)):
        temp = len([i for i in st1[i]])
        if "0" in st1[i]:
            ans[0] = max(ans[0],temp)
        elif "1" in st1[i]:
            ans[1] = max(ans[1],temp)
    return abs(ans[0]-ans[1])
print(counts())
