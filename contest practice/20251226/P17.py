from collections import deque

def maxSlidingWindow(nums, k):
    if not nums or k == 0:
        return []
    
    dq = deque()
    result = []
    
    for i in range(len(nums)):
        # 1. 移除超出窗口左邊界 (i-k) 的元素
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # 2. 保持單調遞減: 移除比當前元素小的 (索引)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
            
        # 3. 加入當前元素索引
        dq.append(i)
        
        # 4. 記錄結果 (當窗口滿 k 個元素後)
        if i >= k - 1:
            result.append(nums[dq[0]])
            
    return result

n, k = map(int,input().split())
nums = list(map(int,input().split()))
print(*maxSlidingWindow(nums,k))