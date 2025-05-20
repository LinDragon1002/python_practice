st = input().split("=")
for i in range(1,101):
    temp = eval(st[0],{'X':i})
    if temp == int(st[1]):
        print(i)
        break