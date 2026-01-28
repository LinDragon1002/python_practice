def removeDuplicates(nums) :
    for i in range(len(nums)-1,0,-1):
        if nums[i] == nums[i-1]:
            nums.pop(i)
    ans_num = len(nums)
    return ans_num


nums = [0,0,1,1,1,2,2,3,3,4]
expectedNums = [1]

k = removeDuplicates(nums)

k == len(expectedNums)
for i in range(k):
    nums[i] == expectedNums[i]
