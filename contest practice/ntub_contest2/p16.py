def contest():
    n = int(input())
    ans = 0
    while n > 1:
        if n % 2 == 0:
            temp = n / 2
        else:
            temp = (n-1) / 2
        n -= int(temp)
        ans += int(temp)
    return ans
print(contest())
