n = 1
if n == 1:
    print(True)
elif n % 2 == 0:
    temp = 1
    while True:
        temp *= 2
        if temp > n:
            print(False)
            break
        elif temp == n:
            print(True)
            break
else:
    print(False)