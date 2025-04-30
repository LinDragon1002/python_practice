def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

st = input().split()
num1 = int(st[0], int(st[1]))
num2 = to_base(num1,int(st[2]))
print(num2)