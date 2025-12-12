def prime_factorization(n):
    factors = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

print(*prime_factorization(int(input())))


n = int(input())
ans = []
for i in range(2,n+1):
    if n % i == 0:
       while n % i == 0:
           ans.append(i)
           n = n // i
print(*sorted(ans))