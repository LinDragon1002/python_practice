s = input()
temp1 = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
temp2 = []
ans = []
temp3 = []
for i in s:
    if i.isupper():
        temp2.append(temp1[i])
    else:
        temp2.append(-temp1[i.upper()])
for i in range(len(temp2)):
    temp = 0
    for j in range(i, len(temp2)):
        temp = sum(temp2[i:j+1])
        ans.append(temp)
print(max(ans))