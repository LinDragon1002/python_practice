def find_factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

import math
a = int(input())
b = int(input())
temp = math.gcd(a,b)
print(*find_factors(temp))