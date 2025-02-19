def total(a):
    ans = 0
    for i in range(len(a)):
        if 65 <= ord(a[i]) <= 90:
            ans = ans + int(ord(a[i])) - 64
        elif 97 <= ord(a[i]) <= 122:
            ans = ans - int(ord(a[i])) + 96
    return ans

a = input()
print(total(a))