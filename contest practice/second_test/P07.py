st = [i for i in input()]
ans = []
temp = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0,"L":0,"M":0,"N":0,"O":0,"P":0,"Q":0,"R":0,"S":0,"T":0,"U":0,"V":0,"W":0,"X":0,"Y":0,"Z":0}
for i in st:
    temp[i] += 1

for i in temp:
    if temp[i] == 0:
        ans.append(i)
if len(ans) > 0:
    print("".join(ans))
else:
    print(0)
    