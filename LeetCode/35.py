nums = [1,3,5,6]
target = 7
try:

    print(nums.index(target))
except:
    for i in range(len(nums)):
        if nums[i] > target:
            print(i)
            break
    else:
        print(i+1)