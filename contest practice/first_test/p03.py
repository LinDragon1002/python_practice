def numbers():
    number = input()
    ans = [0,0]
    temp2 = []
    for i in range(len(number)):
        ans[0] += int(number[i])
    for i in range(2,int(number)+1):
        if int(number)%i == 0:
            
    if len(temp2) == 0:
        return 0
    for i in range(len(temp2)):
        temp3 = [int(i) for i in str(temp2[i])]
        for j in range(len(temp3)):
            ans[1] += temp3[j]
    if ans[0] == ans[1]:
        return 1
    return 0
    
print(numbers())
