import string
st = input()
temp_uper = string.ascii_uppercase
temp_lower = string.ascii_lowercase
st2 = []
ans = []
for i in st:
    if i in temp_uper:
        temp = temp_uper.index(i)
        st2.append(temp+1)
    else:
        temp = temp_lower.index(i)
        st2.append(temp+1)
for i in range(len(st2)):
    for j in range(len(st2)):
        temp = sum(st2[i:j+1])
        if temp % 10 == 0:
            temp2 = [st[i:j+1],len(st[i:j+1])]
            ans.append(temp2)
ans = sorted(ans,key=lambda x:x[1],reverse=True)
# print(ans)
print(ans[0][1])