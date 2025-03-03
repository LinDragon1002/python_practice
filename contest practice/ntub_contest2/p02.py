def number():
    response = [int(i) for i in input().split(',')]
    ans = []
    for i in range(len(response)):
        if i == 0:
            ans.append(response[0])
        else:
            ans.append(ans[i-1]+response[i])
    return ans

print(number())

