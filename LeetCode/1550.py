arr = [2,6,4,1]
count = 0
for i in arr:
    if i % 2 != 0:
        count += 1
    else:
        count = 0
    if count == 3:
        print()
#         return True
# return False