def to_base_f(n, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

num_str,from_base,to_base = input().split()
print(to_base_f(int(num_str,int(from_base)),int(to_base)))