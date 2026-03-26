nums = [55]
k = 1

def max_sum_sliding_window(nums, k):    
    window_sum = sum(nums[:k])
    max_sum = window_sum / k
    
    for i in range(len(nums) - k):
        window_sum = window_sum - nums[i] + nums[i+k]
        max_sum = max(max_sum, window_sum / k)
        
    return max_sum

print(max_sum_sliding_window(nums,k))