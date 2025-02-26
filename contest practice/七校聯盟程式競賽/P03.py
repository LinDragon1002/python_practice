def trend():
    ans = 0
    response = [ord(i) for i in input()]
    for i in range(len(response)):
        if i < len(response) - 1 and response[i] > response[i+1]:
            ans += 1
        elif i < len(response) - 1 and response[i] < response[i+1]:
            ans += 100
    if ans == len(response) - 1:
        return 2
    elif len(response) -1 == ans // 100 and ans % 100 == 0:
        return 1
    return 3

print(trend())