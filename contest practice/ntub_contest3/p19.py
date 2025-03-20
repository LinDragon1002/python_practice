def fiter():
    st = [i for i in input().split()]
    fiters = ["fucking","fucker","fuck","shit","hello"]
    for i in range(len(st)):
        if st[i] in fiters:
            st[i] = "-"*len(st[i])
        else:
            for j in fiters:
                st[i] = st[i].replace(j,"-"*len(j))

        
    return " ".join(st)
print(fiter())