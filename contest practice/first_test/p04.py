def counts():
    st = [i for i in input()]
    ans = [0,0]
    for i in range(len(st)):
        if st[i] == "1" and st[i+1] == "1":
            ans[1] += 1
        else:
            
        if st[i] == "0" and st[i+1] == "0":
            ans[0] += 1