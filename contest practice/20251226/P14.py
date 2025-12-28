from typing import Counter

def prime_factorization(n):
    factors = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                factors.append(i)
                n = n // i
    if n > 1:
        factors.append(n)
    return factors

ans = []
num = int(input())
temp = Counter(prime_factorization(num))
for i in temp:
    if temp[i] > 1:
        ans.append(str(i) + "^" + str(temp[i]))
    else:
        ans.append(str(i))
print(" * ".join(ans))