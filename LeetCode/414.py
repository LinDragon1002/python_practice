nums = [3,2,1]
nums = list(set(nums))
ans = 0
if len(nums) > 2:
    for i in range(3):
        ans = max(nums)
        nums.remove(max(nums))
    print(ans)
else:
    print(max(nums))
    