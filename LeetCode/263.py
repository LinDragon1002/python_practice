# Ugly Number 沒有2,3,5以外的質數

# def isPrime(n):
#     factors = []
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             while n % i == 0:
#                 factors.append(i)
#                 n = n // i
#     if n > 1:
#         factors.append(n)
#     return factors

n = 0
# print(isPrime(n))
ugly = [2,3,5]
if n == 0:
    print(False)
for i in ugly:
    if n % i == 0:
        while n % i == 0:
            n //= i
if n > 1 or n <= -1:
    print(False)
else:
    print(True)
