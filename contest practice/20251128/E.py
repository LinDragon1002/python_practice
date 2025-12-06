s = list(map(int, input().split()))
n = len(s)

if n == 0:
    print(0)
else:
    # 初始化
    max_dp = s[0]  # 當前最大乘積
    min_dp = s[0]  # 當前最小乘積
    result = s[0]  # 全局最大值
    
    for i in range(1, n):
        # 暫存前一個狀態（因為會被覆蓋）
        temp_max = max_dp
        
        # 更新最大和最小乘積
        max_dp = max(s[i], s[i] * max_dp, s[i] * min_dp)
        min_dp = min(s[i], s[i] * temp_max, s[i] * min_dp)
        
        # 更新全局最大值
        result = max(result, max_dp)
    print(max(result, 0))