def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True

num1 = int(input())
num2 = int(input())
factors = []
for i in range(min(num1,num2),max(num1,num2)+1):
    if isPrimeNumber(i):
        if str(i) == str(i)[::-1]:
            factors.append(i)

print(len(factors))