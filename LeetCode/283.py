nums = [1,0,1,2,13]

counts = nums.count(0)
for i in range(counts):
    nums.pop(nums.index(0))
    nums.append(0)

# left =0


# for right in range(len(nums)):

#     if (nums[right]!=0):

#         nums[left] , nums[right] = nums[right] , nums[left]
#         left+=1

print(nums)