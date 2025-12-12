def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True
    
n = int(input())
ans = 0
for i in range(2,n):
    if str(i) == str(i)[::-1] and isPrimeNumber(i):
        ans += i
print(ans)