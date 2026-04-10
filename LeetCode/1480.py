nums = [1,2,3,4]
ans = [0] * len(nums)
for i in range(len(nums)):
    if i > 0:
        ans[i] = ans[i-1] + nums[i]
    else:
        ans[i] = nums[i]
print(ans)

# 另解

"""
for i in range(1, len(nums)):
    nums[i]+= nums[i-1]
return nums
"""