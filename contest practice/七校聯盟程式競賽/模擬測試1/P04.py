st = input()
words = []
num = []
cnt = 0
for i in range(len(st)-1):
    if i == 0:
        words.append(st[i])
        cnt += 1
    if st[i] == st[i+1]:
        cnt += 1
    else:
        num.append(cnt)
        cnt = 1
        words.append(st[i+1])
num.append(cnt)
for i in range(len(words)):
    print(words[i],num[i],sep='',end='')