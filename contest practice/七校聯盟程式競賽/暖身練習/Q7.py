num = int(input())
nums = list(map(int,input().split()))
ans = []
for i in range(len(nums)):
    for j in range(len(nums)):
        temp = nums[i:j+1]
        ans.append(sum(temp))
ans = sorted(ans,reverse=True)
print(ans[0])