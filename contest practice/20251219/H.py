from typing import Counter

def prime_factorization(n):
    ans = ""
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                ans += str(i)
                n = n // i
    if n > 1:
        ans += str(n)
    return ans

import sys
input = sys.stdin.readline

MAX = 10**6
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False


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

for i in range(int(input())):
    num = input().strip()
    while True:
        num = str(int(num) + 1)
        temp = 0
        temp2 = 0
        temp1 = prime_factorization(int(num))
        for j in num:
            temp += int(j)
        for k in temp1:
            temp2 += int(k)
        if not isPrime(int(num)) and temp == temp2:
            print(num)
            break

