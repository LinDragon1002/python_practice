def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

cnt = int(input())
for i in range(cnt):
    num1 = input().split()
    print(to_base(int(num1[0]),int(num1[1])))