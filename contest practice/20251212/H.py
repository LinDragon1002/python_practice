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


while True:
    try:
        if isPrime(int(input())):
            print("T")
        else:
            print("F")
    except:
        break
