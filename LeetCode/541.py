s = "abcdefg"
k = 1
# num = len(s) // (2 * k)
ans = ""
for i in range(0,len(s),2*k):
    temp = s[i:i+2*k]
    if len(temp) == 2 * k or k < len(temp) <= 2*k:
        ans += temp[:k][::-1] + temp[k:]
    else:
        ans += temp[::-1]

print(ans)