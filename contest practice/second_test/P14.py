from math import gcd

st = [int(i) for i in input().split(",")]
ans = st[0]
for i in st:
    ans = gcd(ans,i)

print(ans)
