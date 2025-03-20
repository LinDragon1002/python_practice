st = [int(i) for i in input().split()]
number=[]
for i in range(len(st)-1):
    if st[i] >= st[i+1]:
        number.append(st[i])
    if len(number) > 1:
        print(0)
        break

if len(number) == 1:
    st.remove(number[0])
    for i in range(len(st)-1):
        if st[i] >= st[i+1]:
            print(0)
            break
    else:
        print(1)