def counts():
    response = [i for i in input()]
    temp = 0
    ans = 0
    for i in response:
        if i == "(":
            temp += 1
            ans = max(ans,temp)
        elif i == ")":
            temp -= 1
    return ans

print(counts())
            