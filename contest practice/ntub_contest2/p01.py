def samenumber():
    response = [i for i in input().lower()]
    ans = [0] * 2
    temp = ["a","e","i","o","u"]
    for i in range(len(response) // 2):
        if response[i] in temp:
            ans[0] += 1
    for i in range(len(response)-1, len(response) // 2 - 1, -1):
        if response[i] in temp:
            ans[1] += 1
    if ans[0] == ans[1]:
        return True
    return False
print(samenumber())