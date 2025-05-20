st1 = input()
st2 = input()
ans = []
for i in range(len(st1)):
    temp = abs(ord(st1[i]) - ord(st2[i]))
    ans.append(temp)
ans = sorted(ans,reverse=True)
print(ans[0])
