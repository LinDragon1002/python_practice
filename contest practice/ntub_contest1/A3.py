def check(a):
    temp = 0
    if len(a) >= 10:
        temp += 1
    for i in a:
        if 48 <= ord(i) <= 57:
            temp += 1
            break
    for i in a:
        if 65 <= ord(i) <= 90:
            temp += 1
            break
    if temp >= 3:
        ans = True
    else:
        ans = False
    return ans

a = input()
print(check(a))