st1 = input()
st2 = input()
cnt = 1
temp = st1[cnt-1]
for i in range(len(st2)):
    if temp == st2[i]:
        cnt += 1
        temp = st1[cnt-1]
print(cnt)
        