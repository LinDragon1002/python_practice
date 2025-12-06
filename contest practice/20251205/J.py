while True:
    try:
        n = int(input())
        dp = [1] * n
        if n == 1:
            print(1)
        else:
            for i in range(1,n):
                dp[i] = dp[i-1] + i
            print(dp[-1])
    except:
        break