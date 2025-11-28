n = int(input())
s = list(map(int,input().split()))
dp = s
for i in range(1,n):
    dp[i] = max(s[i], s[i] + dp[i-1])
print(max(dp))
