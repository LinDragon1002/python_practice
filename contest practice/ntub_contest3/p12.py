def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True

for i in range(10,int(input())+1):
    if not isPrimeNumber(i):
        print(i)