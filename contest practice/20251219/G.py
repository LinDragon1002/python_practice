def prime_factorization(n):
    ans = []
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            while n % i == 0:
                ans.append(i)
                n = n // i
    if n > 1:
        ans.append(n)
    return ans

from typing import Counter
num = int(input())
temp = prime_factorization(num)
temp1 = Counter(temp)
ans = 0
for value in temp1:
    ans += temp1[value]
print(f"{sum(set(temp))} {ans}")