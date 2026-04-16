arr = [1,2,3,4]
k = 2
count = 0
sums = 1
while True:
    if sums not in arr:
        count += 1
        if count == k:
            break

    sums += 1
print(sums)

#  另解

"""
arr = set(arr)
res = []
i = 1
while True:
if i not in arr:
    res.append(i)
if len(res) == k:
    return res[-1]
i += 1
"""