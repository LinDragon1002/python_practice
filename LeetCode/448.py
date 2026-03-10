nums = [1,1,2,2]
temp1 = set(nums)
temp2 = set([i for i in range(1,len(nums)+1)])

print(list(temp1 ^ temp2))

n = len(nums)+1
seen = [False]*n
for i in nums:
    seen[i] = True
# return [i for i in range(1,n) if not seen[i]]
print()