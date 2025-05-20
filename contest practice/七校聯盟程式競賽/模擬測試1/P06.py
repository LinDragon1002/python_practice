st = input()
cnt = 0
for i in range(len(st)):
    for j in range(i,len(st)):
        temp = st[i:j+1]
        if len(temp) >= 4 and st[i] == st[j] and st[i].isupper() and st[j].isupper():
            cnt += 1
print(cnt)