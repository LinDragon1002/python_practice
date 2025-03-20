st = [int(i) for i in input().split(",")]
temp = [[] for _ in range(len(st))]
for i in range(2,len(st)):
    for j in range(1,st[i]):
        if st[i]%j==0:
            temp[i].append(j)
            st[i]//=j

print(temp)
