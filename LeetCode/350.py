nums1 = [1,2,2,1]
nums2 = [2,2]

from typing import Counter
temp1 = Counter(nums1)
temp2 = Counter(nums2)
ans = []
if len(temp1) >= len(temp2):
    for i in temp2:
        if temp1[i] != 0 and temp2[i] != 0:
            for j in range(min(temp1[i],temp2[i])):
                ans.append(i)
else:
    for i in temp1:
        if temp1[i] != 0 and temp2[i] != 0:
            for j in range(min(temp1[i],temp2[i])):
                ans.append(i)
print(ans)