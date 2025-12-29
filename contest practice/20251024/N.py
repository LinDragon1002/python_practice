num = int(input())
for i in range(num):
    rounds = int(input())
    if rounds == 0:
        break
    else:
        moneys = list(map(int,input().split(' ')))
        dp = moneys
        for i in range(1,len(moneys)):
            dp[i] = max(moneys[i], moneys[i] + dp[i-1])

        # 暴力解
        # ans = max(ans,max(moneys))
        # for i in range(len(moneys)):
        #     temp_n = 0
        #     for j in range(i,len(moneys)):
        #         temp_n += moneys[j]
        #         ans = max(ans,temp_n)
    if max(dp) > 0:
        print(f"The maximum winning streak is {max(dp)}.")
    else:
        print("Losing streak.")