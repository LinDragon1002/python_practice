def number():
    response = int(input())
    ans = 0
    while response != 0:
        if response % 2 == 0:
            response //= 2
        else:
            response -= 1
        ans += 1
    return ans

print(number())