def isPrimeNumber(num):
    if num % 2 == 0:
        return "T" if num == 2 else "F"
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return "F"
    else:
        return "T"
    
print(isPrimeNumber(int(input())))