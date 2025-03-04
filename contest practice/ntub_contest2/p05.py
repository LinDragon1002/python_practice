def exchange():
    response = [i for i in input()]
    ans = ""
    for i in response:
        if i.isupper():
            ans += i.lower()
        # elif i.islower():
        #     ans += i
        else:
            ans += i
    return ans

print(exchange())