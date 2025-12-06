def F(n):
    if n == 1:
        return 1
    else:
        return n**2 + F(n-1)

while True:
    n = int(input())
    if n == 0:
        break
    print(F(n))