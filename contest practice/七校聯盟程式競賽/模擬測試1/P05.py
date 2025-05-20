st = input()
ans = [0,0,0]
temp=[]
for i in range(len(st)):
    if st[i].isdigit():
        ans[2] += 1
    elif st[i].isupper():
        ans[1] += 1
        temp.append(1)
    elif st[i].islower():
        ans[0] += 1
        temp.append(0)
if 0 not in ans:
    for i in range(len(temp)-1):
        if temp[i] > temp[i+1]:
            print(0)
            break
    else:
        print(1)
else:
    print(0)