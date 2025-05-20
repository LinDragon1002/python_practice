st = input()
ans = 0
temp = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":34,"J":18,"K":19,"L":20,"M":21,"N":22,"O":35,"P":23,"Q":24,"R":25,"S":26,"T":27,"U":28,"V":29,"W":32,"X":30,"Y":31,"Z":33}
if len(st) == 10 and 1 <= int(st[1]) <= 2 and st[0].isupper():
    temp2 = str(temp[st[0]])
    ans += int(temp2[0]) + 9 * int(temp2[1]) + 8 * int(st[1]) + 7 * int(st[2]) + 6 * int(st[3]) + 5 * int(st[4]) + 4 * int(st[5]) + 3 * int(st[6]) + 2 * int(st[7]) + int(st[8]) + int(st[9])
    if ans % 10 == 0:
        print(1)
    else:
        print(0)
else:
    print(0)