def to_base(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result
m,n,num = input().split()
try:
    to_10 = int(num,int(m))
    ans = to_base(to_10,int(n))
    print(f'{num} base {m} = {ans} base {n}')
except:
    print(f"{num} is an illegal base {m} number")