import string
def to_bases(n, base):
    digits = string.digits + string.ascii_uppercase
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return result

num_str,from_base,to_base = input().split()
num1 = int(num_str,int(from_base))
print(to_bases(num1,int(to_base)))