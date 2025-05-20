def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True
num = int(input())
cnt = 0
for i in range(num-1,1,-1):
    if isPrimeNumber(i):
        print(i,end=" ",sep=" ")
        break
while True:
    cnt += 1
    if isPrimeNumber(num+cnt):
        print(num+cnt,end=" ",sep=" ")
        break