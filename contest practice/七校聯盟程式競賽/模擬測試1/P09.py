def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result
num = input().split(',')
temp1 = int(num[0],3)
temp2 = int(num[1],6)
ans = temp1 + temp2
print(to_base(ans,5))