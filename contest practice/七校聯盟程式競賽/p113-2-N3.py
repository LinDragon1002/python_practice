st = input()
temp = []
for i in range(0,len(st)-1):
    if st[i] > st[i+1]:
        temp.append(1)
    else:
        temp.append(0)

for i in range(len(temp)-1):
    if temp[i] == temp[i+1]:
        print('0')
        break
else:
    print('1')      
