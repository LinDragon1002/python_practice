st = [i for i in input().replace(";",",;,").split(",")]
temp1 = []
temp2 = []
for i in st:
    if i == ";":
        temp2.append(temp1)
        temp1 = []
    else:
        temp1.append(int(i))
temp2.append(temp1)
for i in range(1,len(temp2)):
    for j in range(len(temp2[0])):
        temp2[i][j] += temp2[i-1][j]
    

print(temp2)