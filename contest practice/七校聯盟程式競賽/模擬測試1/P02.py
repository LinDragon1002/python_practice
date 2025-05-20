st = input()
cnt = [0,0]
for i in range(len(st)-1):
    if i == 0 and int(st[i]) > int(st[i+1]):
        cnt[1] += 1
        break
    if int(st[i]) > int(st[i+1]):
        for j in range(i,len(st)-1):
            if int(st[i]) < int(st[j]):
                cnt[1] += 1
                break
        else:
            cnt[0] += 1
if cnt[1] > 0 or cnt[0] == 0 and cnt[1] == 0:
    print(0)
else:
    print(1)
