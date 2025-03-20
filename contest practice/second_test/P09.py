s = input()
temp1 = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
temp2 = []
ans = 0
temp3 = 0
num = 0
for i in s:
    if i.isupper():
        num += 1
        ans += temp1[i]
        temp3 += temp1[i]
    else:
        ans -= temp1[i.upper()]
        if num > 1:
            temp2.append(temp3)
        temp3 = 0
        num = 0
    temp2.append(ans)
if temp3 > 0 and num > 1:
    temp2.append(temp3)
print(max(temp2))