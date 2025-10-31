while True:
    rounds = int(input())
    ans = -1
    if rounds == 0:
        break
    else:
        moneys = list(map(int,input().split(' ')))
        ans = max(ans,max(moneys))
        for i in range(len(moneys)):
            temp_n = 0
            for j in range(i,len(moneys)):
                temp_n += moneys[j]
                ans = max(ans,temp_n)
    if ans > 0:
        print(f"The maximum winning streak is {ans}.")
    else:
        print("Losing streak.")