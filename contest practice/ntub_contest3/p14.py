def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True

ans = []
for i in range(10,99):
    if isPrimeNumber(i):
        if str(i)[-1] >= str(i)[0]:
            print(i)

