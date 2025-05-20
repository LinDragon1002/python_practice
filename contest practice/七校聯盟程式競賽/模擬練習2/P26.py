st=input().split('/')
temp1 = st[0].split('.')
temp2 = st[1].split('.')
ans = []
for i in range(len(temp1)):
    ans.append(int(temp1[i]) & int(temp2[i]))
print(*ans,sep=".")