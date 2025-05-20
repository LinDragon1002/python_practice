num = input()
st = 'ABCDEF'
ans = ''
temp = []
for i in range(len(num)):
    if num[i].isdigit():
        temp.append(int(num[i])-1)
for i in range(len(temp)):
    if i > 0:
        st = ans
        ans = ''
    runs = st[0]
    for j in range(1,len(st)):
        if j == int(temp[i]):
            ans += st[j]
            ans += runs
        else:
            ans += st[j]

print(ans)