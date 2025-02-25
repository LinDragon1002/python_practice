def number():
    response = [i for i in input()]
    ans = 0
    for i in response:
        ans = ans + int(i) ** 2
    print(ans)

number()