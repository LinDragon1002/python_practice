st = input()
temp = {}
for i in st:
    if i not in temp:
        temp[i] = 1
    else:
        temp[i] += 1
temp = list(sorted(temp.items(), key=lambda x:x[-1]))
print(temp[0][0])