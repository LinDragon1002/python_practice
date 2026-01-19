num = input()
step = [1,2,1,2,1,2,4,1]
ans = 0
for i in range(len(num)):
    temp = num[i] * step[i]
    if len(str(temp)) > 1:
        temp2 = 0
        for k in str(temp):
            temp2 += k
        temp = temp2
        