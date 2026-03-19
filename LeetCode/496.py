nums1 = [1,3,5,2,4]
nums2 = [6,5,4,3,2,1,7]
ans = [-1] * len(nums1)
for i in range(len(nums1)):
    num_index = nums2.index(nums1[i])
    if num_index < len(nums2)-1:
        for j in range(num_index+1,len(nums2)):
            if nums2[num_index] < nums2[j]:
                ans[i] = nums2[j]
                break
print(ans)

# 另解

'''
hm = {}
greater = deque()
for i in range(len(nums2) - 1, -1, -1):
    hm[nums2[i]] = -1

    while len(greater) > 0 and greater[-1] < nums2[i]:
        greater.pop()

    if len(greater) > 0:
        hm[nums2[i]] = greater[-1]
        
    greater.append(nums2[i])

result = []
for num in nums1:
    result.append(hm[num])

return result
'''