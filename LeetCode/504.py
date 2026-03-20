num = -7
def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result
if num < 0:
    print(f"-{(to_base(abs(num),7))}")
print(to_base(num,7))