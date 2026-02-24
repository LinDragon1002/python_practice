n = -1

if n == 0:
    print(False)
else:
    while True:
        if n % 3 == 0:
            n//=3
        else:
            print(False)
            break
        if n == 1:
            print(True)
            break


if n <= 0:
    # return False
    print()

while n % 3 == 0:
    n = n // 3

if n == 1:
    # return True
    print()
else:
    # return False
    print()