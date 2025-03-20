num = int(input())
total = num
temp = []
for i in range(2,num+1):
    if num%i==0:
        temp.append(i)
        num//=i
if total % sum(temp) == 0:
    print(1)
else:
    print(0)