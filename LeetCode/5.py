s = "ac"
ans = ""
for i in range(len(s),0,-1):
    for j in range(max(len(s) - i,2)+1):
        temp = s[j:i+j]
        if temp == temp[::-1] and len(ans) < len(temp):
            ans = temp
            break
    if len(ans) == i:
        break
print(ans)