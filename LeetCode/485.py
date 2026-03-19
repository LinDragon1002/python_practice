nums = [1,0,1,1,0,1]
maxs = 0
count = 0
for i in nums:
    if i == 1:
        count += 1
    else:
        maxs = max(maxs,count)
        count = 0

print(max(maxs,count))