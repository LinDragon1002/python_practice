nums = list(map(int,input().split()))
ans=[]
for i in range(len(nums)):
    for j in range(len(nums)):
        temp = nums[i:j+1]
        if len(temp) > 0:
            temp2 = temp[0]
        for h in range(1,len(temp)):
            temp2 *= temp[h]
        ans.append(temp2)
ans = sorted(ans,reverse=True)
if ans[0] <= 0:
    print(0)
else:
    print(ans[0])