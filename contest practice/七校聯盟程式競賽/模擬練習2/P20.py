def find_factors(n):
    factors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            factors.append(i)
            if i !=n //i:
                factors.append(n//i)
    return sorted(factors)
num = int(input())
ans = []
for i in range(1,num+1):
    if num == sum(find_factors(i)):
        ans.append(i)
ans = sorted(ans,reverse=True)
if len(ans) > 0:
    print(ans[0])
else:
    print(0)