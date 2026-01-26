arr = [3,8,-10,23,19,-4,-14,27]
temp = sorted(arr)
dp = [0] * (len(arr)-1)
min_num = 10 ** 6
ans = []
for i in range(len(arr)-1):
    dp[i] = temp[i+1] - temp[i]
    min_num = min(dp[i],min_num)
for i in range(len(dp)):
    if dp[i] == min_num:
        ans.append([temp[i],temp[i+1]])
print(ans)


'''
[4,2,1,3]
[1,3,6,10,15]
[3,8,-10,23,19,-4,-14,27]
'''