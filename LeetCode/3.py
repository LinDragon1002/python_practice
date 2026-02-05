s = "pwwkew"
ans = 0
temp = ""
for i in s:
    if i not in temp:
        temp += i
    else:
        temp = temp[temp.index(i)+1::]
        temp += i
    ans = max(ans,len(temp))
print(ans)