def prime_factorization(n):
    ans = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                ans.append(i)
                n = n // i
    if n > 1:
        ans.append(n)
    return sum(ans)

import sys
input = sys.stdin.readline

MAX = 10**6
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

primes_table = []
for i in range (2,MAX+1):
    if Prime[i]:
        primes_table.append(i)

def isPrime(n):
    if n <= MAX:
        return Prime[n]
    for p in primes_table:
        if p * p > n:
            break
        elif n % p == 0:
            return n ==  p
    return True

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False

for i in range(int(input())):
    num = int(input())
    if isPrime(num):
        print(num)
    else:
        print(prime_factorization(num))
