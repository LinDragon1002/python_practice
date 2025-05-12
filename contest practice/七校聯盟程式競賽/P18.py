num = int(input())
total = 0
for i in range(1,num+1):
    total += i
avg = total / 2
if total % 2 == 0:
    temp = [i for i in range(1,num+1)]
    temp1 = []
    for i in range(num,0,-1):
        if avg - i >= 0:
            avg -= i
            temp1.append(i)
    temp = set(temp)
    temp1 = set(temp1)
    ans = temp - temp1 
    print(f'YES,{str(sorted(temp1)).replace(" ","")},{str(sorted(ans)).replace(" ","")}')
else:
    print("NO")