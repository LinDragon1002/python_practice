def safe(a):
    temp = 0
    for i in a:
        temp = temp + (ord(i) - 65)
    if temp % 2 == 0:
        return a + "0"
    else:
        return a + "1"

a = input()
print(safe(a.upper()))