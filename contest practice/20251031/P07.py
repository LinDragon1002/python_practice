from itertools import combinations

st = list(map(int,input().replace(" ", "").split(',')))
tot = sum(st) // 2
if tot % 2 != 0:
    for i in list(combinations(st,len(st)//2)):
        s = sum(i)
        if s == tot:
            print(1)
            exit()
    else:
        print(0)
else:
    print(0)
