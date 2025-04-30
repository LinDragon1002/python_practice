st = input()
cnt = 0
temp = []
for i in range(len(st)):
    for j in range(len(st)+1):
        if len(st[i:j]) >= 3 and st[i] in ("A","E","I","O","U") and st[j-1] in ("A","E","I","O","U"):
            temp.append(st[i:j])
            cnt += 1
print(cnt)