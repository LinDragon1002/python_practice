nums = [6]
ans = [-1] * len(nums)
for i in range(len(nums)):
    temp = 0
    while temp < nums[i]:
        if (temp | temp + 1) == nums[i]:
            ans[i] = temp
            break
        temp += 1
print(ans)