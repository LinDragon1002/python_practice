import sys
input = sys.stdin.readline

MAX = 10**6
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False

primes_table = []
for i in range (2,MAX+1):
    if prime[i]:
        primes_table.append(i)


def isprime(n):
    if n <= MAX:
        return prime[n]
    for p in primes_table:
        if p * p > n:
            break
        elif n % p == 0:
            return n ==  p
    return True

while True:
    try:
        if isprime(int(input())):
            print("T")
        else:
            print("F")
    except:
        break