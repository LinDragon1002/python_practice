nums = [0,1,2,2,3,0,4,2]
val = 2

while True:
    if nums.count(val) > 0:
        nums.remove(2)
    else:
        break
ans_num = len(nums)
