from typing import Counter
ans = []
def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True
st = Counter(input())
for i in st:
    if isPrimeNumber(st[i]) and st[i] != 1:
        ans.append(i)
if len(ans) > 0:
    ans = sorted(ans)
    print("".join(ans))
else:
    print(-1)