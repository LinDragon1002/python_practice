def check(a):
    for i in a:
        if 65 <= ord(i) <= 90:
            ans = True
        else:
            ans = False
            break
    if len(a) >= 2:
        ans = True
    else:
        ans = False
    for i in range(1,len(a)):
        if ord(a[i]) >= ord(a[i-1]):
            ans = True
        else:
            ans = False
            break
    return ans

a = input()
print(check(a))

