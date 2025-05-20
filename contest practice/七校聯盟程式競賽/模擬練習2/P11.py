nums = list(map(int,input().split()))
temp = nums.copy()
ans = []
for _ in range(0,len(nums),2):
    temp = sorted(temp)
    ans.append(abs(temp[0] - temp[-1]))
    temp.pop()
    temp = sorted(temp,reverse=True)
    temp.pop()
print(sum(ans))