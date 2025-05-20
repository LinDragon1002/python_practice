st = input()
ans = ''
temp = []
temp2 = ''
for i in range(len(st)):
    if i == 0:
        temp.append(st[i])
    elif st[i].isupper() or st[i].islower():
        temp.append(temp2)
        temp.append(st[i])
        temp2 = ''
    elif st[i].isdigit():
        temp2 += st[i]
temp.append(temp2)
for i in range(0,len(temp),2):
    if temp[i].isupper() or temp[i].islower():
        ans += int(temp[i+1]) * temp[i]
print(ans)