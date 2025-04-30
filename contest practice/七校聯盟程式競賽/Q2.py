st = input()
temp = []
for i in range(len(st)):
    for j in range(i+1,len(st)):
        temp1 = st[i:j+1]
        if temp1 == temp1[::-1]:
            temp.append(len(st[i:j+1]))
temp = sorted(temp,reverse=True)
if len(temp) > 1:
    print(temp[0])
else:
    print(0)