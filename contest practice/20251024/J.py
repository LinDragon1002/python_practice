def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True

while True:
    inputs = int(input())
    if inputs == 0:
        break
    else:
        for i in range(3,inputs,2):
            temp = inputs - i
            if isPrimeNumber(i) and temp % 2 != 0 and isPrimeNumber(temp):
                break
        print(str(inputs) + " = " + str(i) + " + " + str(temp))