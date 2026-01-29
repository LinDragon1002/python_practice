nums1 = [-1,0,0,3,3,3,0,0,0]
nums2 = [1,2,2]

m = 6
n = 3
temp = 0


for i in range(nums1.count(0)):
    if temp >= n:
        break
    nums1[nums1.index(0)] = nums2[temp]
    temp += 1

nums1.sort()
print(nums1.copy())







'''
[1,2,3,0,0,0]
[2,5,6]

[1]
[]

[0]
[1]

[1,0]
[2]

[2,0]
[1]

[-1,0,0,3,3,3,0,0,0]
[1,2,2]
'''
