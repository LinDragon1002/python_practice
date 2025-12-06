from typing import Counter
st = input()
odd_TF = 0
temp = Counter(st).items()
temp = sorted(temp, key=lambda x:x[0])
for a,b in temp:
    if b % 2 != 0 and odd_TF == False:
        print(a,b)
        odd_TF = True
    elif b % 2 == 0:
        print(a,b)
