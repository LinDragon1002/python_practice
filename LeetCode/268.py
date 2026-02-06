nums = [9,6,4,2,3,5,7,0,1]

if len(nums)-1 == max(nums):
    print(max(nums)+1)
else:
    for i in range(max(nums)+1):
        if i not in nums:
            print(i)

# 最佳解用算現在nums裡面有多少個數字+1的數字總和 - 現在缺少數字的nums的數字總和