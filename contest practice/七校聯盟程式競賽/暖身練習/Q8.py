ans = {}
st = list(map(str,input().replace("?","").replace(".","").replace(",","").split()))
for i in st:
    if i not in ans:
        ans[i] = 1
    else:
        ans[i] += 1
print(ans)