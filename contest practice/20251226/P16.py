def max_sum_sliding_window(nums, k):    
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i+k]
        max_sum = max(max_sum, window_sum)
        
    return max_sum

n,k = map(int,input().split())
ns = list(map(int,input().split()))
print(max_sum_sliding_window(ns,k))