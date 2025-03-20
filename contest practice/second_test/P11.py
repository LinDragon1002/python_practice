d1 = [i for i in input().split("-")]
d2 = [i for i in input().split("-")]
if d1[1] > d2[1] or d1[1] == d2[1] and d1[2] > d2[2]:
    age = int(d2[0]) - int(d1[0]) - 1
else:
    age = int(d2[0]) - int(d1[0])
if 0 <= age <= 10:
    print(1)
elif 11 <= age <= 17:
    print(2)
elif 18 <= age <= 44:
    print(3)
elif 45 <= age <= 64:
    print(4)
elif age >= 65:
    print(5)