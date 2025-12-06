while True:
    n = int(input())
    if n == 0:
        break
    while True:
        temp = 0
        if len(str(n)) == 1:
            break
        for i in str(n):
            temp += int(i)
        n = temp
    print(n)