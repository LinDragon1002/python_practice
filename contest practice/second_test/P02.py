st = [int(i) for i in input().split()]
temp = st.copy()
number=0
for i in range(len(st)):
    temp.pop(i)
    for j in range(len(temp)-1):
        if temp[j] >= temp[j+1]:
            break
    else:
        number += 1
    temp = st.copy()

if number >= 1:
    print(1)
else:
    print(0)