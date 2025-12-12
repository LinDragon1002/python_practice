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

temp = prime_factorization(int(input()))
temp_set = sorted(set(temp))
ans = []
for i in temp_set:
    temp2 = temp.count(i)
    if temp2 > 1:
        ans.append(str(i) + "^" + str(temp2))
    else:
        ans.append(str(i))
print(" * ".join(ans))