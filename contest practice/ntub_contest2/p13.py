def sorts():
    now = 0
    temp = [i for i in input()]
    ans = ""
    while len(temp) > 0:
        if now % 2 == 0:
            temp1 = sorted(set(temp))
            for i in range(len(temp1)):
                ans += temp1[i]
                temp.remove(temp1[i])
        else:
            temp1 = sorted(set(temp),reverse=True)
            for i in range(len(temp1)):
                ans += temp1[i]
                temp.remove(temp1[i])
        now += 1
    return ans
print(sorts())
