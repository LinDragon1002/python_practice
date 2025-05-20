def isPrimeNumber(num):
    if num % 2 == 0:
        return True if num == 2 else False
    for i in range(3,int(num**0.5)+1,2):
        if num%i == 0:
            return False
    else:
        return True
num = int(input())
ans = []
ans.append(str(num))
while True:
    temp = num
    if int(ans[-1]) == 1 or int(ans[-1]) == 0:
        break
    temp1 = []
    temp2 = []
    for i in range(num,1,-1):
        if isPrimeNumber(i) and i not in temp2:
            b = temp - i
            if isPrimeNumber(b):
                temp3 = [i,temp-i,abs(i - b)]
                temp1.append(temp3)
                temp2.append(b)
    temp1 = list(sorted(temp1,key= lambda x:x[2]))
    if len(temp1) > 0:
        num = temp1[0][2]
        ans.append(str(num))
    else:
        break
print(",".join(ans))